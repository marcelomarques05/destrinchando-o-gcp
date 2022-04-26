resource "google_compute_firewall" "default" {
  name    = "default-rules"
  network = google_compute_network.vpc_network.id

  source_ranges = ["0.0.0.0/0"]

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }

}
