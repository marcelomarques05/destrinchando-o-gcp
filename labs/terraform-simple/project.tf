resource "google_project" "my_project" {
  org_id              = var.org_id
  project_id          = var.project_id
  name                = var.name
  billing_account     = var.billing_account
  auto_create_network = false
}