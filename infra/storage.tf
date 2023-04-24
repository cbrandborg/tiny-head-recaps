resource "google_storage_bucket" "bkt-recap-outputs" {

  name       = var.bkt-outputs
  project    = var.project_id
  location   = var.location
  uniform_bucket_level_access = true
  public_access_prevention = "enforced"

  autoclass  {
    enabled = true
  }
  versioning {
    enabled = true
  }

  depends_on = [
    google_project_service.api_enable-2
    
  ]
}