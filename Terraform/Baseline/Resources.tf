
# Meta Parameters : provider, depends_on, count
provider = "google.west"
depends_on = ["google_compute_instance.server"]

count = "${var.num_servers}"
name = "server ${count.index}"
value = "${google_compute_instance.server.0.instance_id}"
value = "${google_compute_instance.server.*.instance_id}"

# Provisioners : Run scripts when created or destroyed 
provisioner "name" {
  when = "create|destroy"
  connection {
    type = "ssh|winrm"
    user = "username"
    password = "${var.password}"
    }
}

# Life cycle
/*
create_before_destroy = true or false (default = false)
prevent_destroy = true or false (default = false)
ignore_changes = list of attributes
*/

# State terraform.tfstate
