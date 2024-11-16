
# Plugin Architecture

# Provider Versioning
provider "aws" {
  version = ">= 1.2, < 1.12" # terraform version to use
  region = "us-west-2"
}

#terraform init # to download provider plugin
#terraform init -upgrade # to upgrade provider version

# Provider Alias
# If you have multiple provider instance, alias is used to identify each
# Resources set the provider key

provider "google" {
  project = "cloud-academy-terraform"
  region = "us-central"
}

provider "google" {
  alias = "west"
  project = "cloud-academy-terraform"
  region = "us-west"
}

resource "google_compute_disk" "default" {
  provider = "google.west"
}


