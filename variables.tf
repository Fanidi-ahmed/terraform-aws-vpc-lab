provider "aws" {
  region = "eu-west-3"
}
variable "project_name" {
  description = "Nom du projet"
  type        = string
  default     = "terraform-vpc-ec2-lab"
}

variable "environment" {
  description = "Environnement"
  type        = string
  default     = "dev"
}

variable "vpc_cidr" {
  description = "CIDR du VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  description = "CIDR du subnet public"
  type        = string
  default     = "10.0.1.0/24"
}

variable "instance_type" {
  description = "Type EC2"
  type        = string
  default     = "t2.micro"
}

variable "key_name" {
  description = "Nom de la key pair AWS pour SSH"
  type        = string
  default     = "terraform-key"
}
