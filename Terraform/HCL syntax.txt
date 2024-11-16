
provider "google" {
  /* GCP Credentials set with
    GOOGLE_CREDENTIALS environment variable */

  version = "~> 1.7"
  project = "cloud-academy-terraform"
  region = "us-central1"
}

# Image for the instance to use 
variable "image" {
  default = "debian-cloud/debian8"
}

# resource TYPE NAME
resource "google_compute_instance" "server" {
  name = "test"
  machine_type = "n1-standard-1"
  zone = "us-central-1"

  # Lists
  tags = ["team-a", "demo"]

  # Maps
  boot_disk = {
      initialize_params {
         image = "${var.image}"
      }
  }
  network_instance {
    network = "default"
  }
}

/*

Interpolation
--------------
Variables
${var.name}

Map key value
${var.name["key"]}

List index -> indexing starts at 0
${var.name["key"]}

Resource attributes
${type.name.attribute}

Data Sources
${data.type.name.attribute}

Interpolation conditions
Making branching decisions in configuration
${condition ? true_expr : false_expr}

Equality : == !=
Numerical <, >, <= and >=
Logical && || !
true and false must be valid interpolation and both must be of the same type

machine_type = "${var.environment == "production" ? "n1-highmem-64" : "n1-standard-1"}"

Interpolation Math and Functions
--------------------------------

+,-,/,*,% (modulo)
Built-in Functions Syntax : func_name(arg_1, arg_2, ...)
abs(num)
file(path)
replace(string, search, replace)

Assigning Variable
------------------

Variable Files
--------------

-var-file=../vars.auto.tfvars

env = "staging"
list = []
map = {}

Environment Variables
---------------------

TF_VAR_env = "staging"

Variable Precedence : low -> high
defaults -> Environment variables -> Automatic variable files -> -var-file & -var

*/
