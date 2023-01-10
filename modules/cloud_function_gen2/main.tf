resource "google_cloudfunctions_function" "function" {
  name        = "artifact-registry-print-token"
  description = "Print OAuth token for client download."
  runtime     = "python37"

  available_memory_mb          = 128
  source_archive_bucket        = google_storage_bucket.bucket.name
  source_archive_object        = google_storage_bucket_object.archive.name
  trigger_http                 = true
  https_trigger_security_level = "SECURE_ALWAYS"
  timeout                      = 60
  entry_point                  = "/print_token"
  labels = {
    env = "prod-images"
  }

  environment_variables = {
    MY_ENV_VAR = "my-env-var-value"
  }
}