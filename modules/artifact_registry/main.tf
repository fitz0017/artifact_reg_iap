resource "google_artifact_registry_repository" "customer_repo" {
  location      = var.region
  repository_id = "customer_repo"
  description   = "Repository for customer's to download images."
  format        = "DOCKER"
}