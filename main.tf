provider "google" {
  project     = var.project_id
  region      = var.region
}


module "artifact_registry" {
    source = "./modules/artifact_registry"
    
}

