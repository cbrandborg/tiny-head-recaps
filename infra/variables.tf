variable "project_id" {
  description = "Project ID for PubSub Topic and Cloud Functions"
}

variable "billing_account" {
  description = "Main billing account"
}

variable "bkt-sa" {
  description = "Service Account name for Cloud Run"
}

variable "location" {
  description = "Location of deployed cloud services"
}

variable "terraform_sa" {
  description = "General service account for deploying terraform"
}

variable "bkt-outputs" {
  description = "Storage bucket for hosting audio files temporarily"
}