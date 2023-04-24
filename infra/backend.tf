terraform {
  backend "gcs" {
    bucket = "bkt-recap-statefile"
    prefix = "terraform/state"
  }
}