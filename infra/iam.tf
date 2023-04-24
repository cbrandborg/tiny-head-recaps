resource "google_service_account" "sa-bkt-output-steps" {
  account_id   = var.bkt-sa
  display_name = "Cloud Storage Bucket Service Account for Text Embeddings Bucket"

  depends_on = [
    google_project_service.api_enable-2
  ]
}

