resource "google_project_service" "cloudrun" {
  service = "run.googleapis.com"
}

resource "google_project_service" "domains" {
  service = "domains.googleapis.com"
}

# Deploy the initial revision of the service
resource "google_cloud_run_v2_service" "qb-demo" {
  name     = "quickbase"
  location = "europe-north1"

  template {
    scaling {
      max_instance_count = 2
    }
    containers {
      image = "st3ga/quickbase-demo:v1.3.0"
      startup_probe {
        initial_delay_seconds = 3
        timeout_seconds       = 1
        period_seconds        = 3
        failure_threshold     = 2
        tcp_socket {
          port = 8080
        }
      }
      liveness_probe {
        http_get {
          path = "/healthz"
        }
      }
      ports {
        container_port = 8080
      }
    }
  }
  depends_on = [
    google_project_service.cloudrun,
    google_project_service.domains
  ]
}


# Make the service public
resource "google_cloud_run_service_iam_binding" "public" {
  location = google_cloud_run_v2_service.qb-demo.location
  service  = google_cloud_run_v2_service.qb-demo.name
  role     = "roles/run.invoker"
  members = [
    "allUsers"
  ]
}
