variable "org_id" {
  description = "GCP Organization ID"
  type        = string
}

variable "billing_account" {
  description = "The ID of the billing account to associate projects with."
  type        = string
}

variable "default_region" {
  description = "Default region to create resources where applicable."
  type        = string
  default     = "us-central1"
}

variable "default_zone" {
  description = "Default zone to create resources where applicable."
  type        = string
  default     = "us-central1-a"
}

variable "name" {
  description = "Name of the project"
  type        = string
}

variable "project_id" {
  description = "ID of the Project - It should be globally unique"
  type        = string
}

variable "vpc_name" {
  description = "ID of the Project - It should be globally unique"
  type        = string
}