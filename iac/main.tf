resource "google_project_service" "cloudrun" {
  service = "run.googleapis.com"
}

resource "google_project_service" "domains" {
  service = "domains.googleapis.com"
}

# Deploy the initial revision of the service
resource "google_cloud_run_service" "qb-demo" {
  name     = "quickbase"
  location = "europe-north1"

  template {
    spec {
      containers {
        image = "st3ga/quickbase-demo:1.1.0"
        startup_probe {
          initial_delay_seconds = 0
          timeout_seconds       = 1
          period_seconds        = 3
          failure_threshold     = 1
          tcp_socket {
            port = 80
          }
        }
        liveness_probe {
          http_get {
            path = "/healthz"
          }
        }
        ports {
          container_port = 80
        }
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

# Make the service public
resource "google_cloud_run_service_iam_member" "public" {
  service  = google_cloud_run_service.qb-demo.name
  location = "europe-north1"
  role     = "roles/run.invoker"
  member   = "allUsers"
}
