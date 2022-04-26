output "project_id" {
  description = "Project where service accounts and core APIs will be enabled."
  value       = google_project.my_project.id
}
