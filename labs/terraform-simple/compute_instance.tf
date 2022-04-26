resource "google_compute_instance" "default" {
  name         = "test-instance"
  machine_type = "e2-medium"
  zone         = var.default_zone

  tags = ["destrinchando-o-gcp"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.subnetwork-with-private-secondary-ip-ranges.id

    access_config {
        
    }
  }

  metadata_startup_script = "echo destrinchando-o-gcp > /test.txt"
}