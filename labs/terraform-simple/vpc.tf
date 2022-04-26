# Criar a VPC usando como base o projeto que está sendo criado.
resource "google_compute_network" "vpc_network" {
  project                 = var.project_id
  name                    = var.vpc_name
  auto_create_subnetworks = false
}

# Criando a subnet usando a VPC criada anteriormente.
resource "google_compute_subnetwork" "subnetwork-with-private-secondary-ip-ranges" {
  name          = "first-subnetwork"
  ip_cidr_range = "10.2.0.0/16"
  region        = var.default_region
  network       = google_compute_network.vpc_network.id
  secondary_ip_range {
    range_name    = "secondary-range-subnetwork"
    ip_cidr_range = "192.168.10.0/24"
  }
}