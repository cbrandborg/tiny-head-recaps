resource "google_project_service" "api_enable-0" {
  project = var.project_id

  for_each = toset([
    "cloudresourcemanager.googleapis.com"
  ])
  service = each.key

  timeouts {
    create = "30m"
    update = "40m"
  }
}

resource "google_project_service" "api_enable-1" {
  project = var.project_id

  for_each = toset([
    "cloudapis.googleapis.com",
    "iam.googleapis.com",
    "billingbudgets.googleapis.com",

  ])
  service = each.key

  timeouts {
    create = "30m"
    update = "40m"
  }

  depends_on = [
    google_project_service.api_enable-0
  ]
}

resource "google_project_service" "api_enable-2" {
  project = var.project_id

  for_each = toset([
    "speech.googleapis.com",
    "storage.googleapis.com"

  ])
  service = each.key

  disable_dependent_services = true

  timeouts {
    create = "30m"
    update = "40m"
  }

  depends_on = [
    google_project_service.api_enable-1
  ]
}