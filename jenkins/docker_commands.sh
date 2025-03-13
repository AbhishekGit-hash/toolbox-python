
# To list all Docker images on your system
docker image ls

# If you want to see dangling images (untagged images that take up space), run
docker images -f "dangling=true"

# Run Jenkins in detached mode (-d) with port mapping (-p) so you can access it via the browser
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts-jdk17

# To get initial password
docker exec my-jenkins cat /var/jenkins_home/secrets/initialAdminPassword

# To get list of running containers
docker ps -a