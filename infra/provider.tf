terraform {

  # cloud {
  #   organization = "cbrandborg"

  #   workspaces {
  #     name = "billing-slack-notification-service"
  #   }
  # }

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.66.0"
    }
  }
}