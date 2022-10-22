terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "3.5.0"
    }
  }
}

provider "google" {
  credentials = file("../../../../.env/gcp-dmp-service-account.json")

  project = "data-mesh-platform"
  region  = "us-central1"
  zone    = "us-central1-c"
}

resource "google_storage_bucket" "state-bucket" {
  name     = "dmp-product-catalog"
  location = "US"
  versioning {
    enabled = true
  }
}