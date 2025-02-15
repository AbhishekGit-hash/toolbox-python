import multiprocessing as mp
import threading
import requests
import time
import pandas as pd

# Constants
API_URL = "https://your-api.com/data"
TOTAL_RECORDS = 402000
BATCH_SIZE = 400
TOTAL_BATCHES = TOTAL_RECORDS // BATCH_SIZE  # 1005 batches

CORES_TO_USE = 4  # Using 4 out of 6 available cores
THREADS_PER_PROCESS = 20  # 20 threads per process
BATCHES_PER_PROCESS = TOTAL_BATCHES // CORES_TO_USE  # 252 batches per process

# Simulated DataFrame (replace with actual data)
df = pd.DataFrame({"unique_values": range(TOTAL_RECORDS)})


def fetch(url, batch):
    """Make an API request for a batch of IDs and return JSON response."""
    try:
        response = requests.get(url, params={"ids": batch}, timeout=5)
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def worker(batch_queue, results):
    """Thread worker function to process API requests."""
    while True:
        try:
            batch = batch_queue.get(timeout=2)  # Get a batch
        except Exception:
            break  # Exit if queue is empty

        batch_results = fetch(API_URL, batch)  # Send batch request
        results.append(batch_results)  # Store results in shared list
        batch_queue.task_done()


def process_worker(batch_list, results):
    """Process worker: creates threads to fetch API data."""
    batch_queue = mp.JoinableQueue()

    # Fill queue with batches assigned to this process
    for batch in batch_list:
        batch_queue.put(batch)

    # Start threads
    threads = []
    for _ in range(THREADS_PER_PROCESS):
        t = threading.Thread(target=worker, args=(batch_queue, results))
        t.start()
        threads.append(t)

    batch_queue.join()  # Wait for all tasks to complete

    for t in threads:
        t.join()


if __name__ == "__main__":
    start_time = time.time()

    manager = mp.Manager()
    results = manager.list()  # Shared list for storing API responses

    # Create batch list from the DataFrame (without dictionary transformation)
    all_batches = [
        df["unique_values"].iloc[start:start + BATCH_SIZE].tolist()
        for start in range(0, TOTAL_RECORDS, BATCH_SIZE)
    ]

    # Distribute batches among processes
    processes = []
    for i in range(CORES_TO_USE):
        batch_subset = all_batches[i * BATCHES_PER_PROCESS : (i + 1) * BATCHES_PER_PROCESS]
        p = mp.Process(target=process_worker, args=(batch_subset, results))
        p.start()
        processes.append(p)

    # Wait for all processes to finish
    for p in processes:
        p.join()

    print(f"Fetched {len(results)} batch responses in {time.time() - start_time:.2f} seconds")
