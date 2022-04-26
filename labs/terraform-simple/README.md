# Destrinchando o GCP

## Labs

### Terraform Simple

---

Objetivo:

Utilizar o [Terraform](terraform.io) para criar um projeto, uma VPC com uma subnet e uma instância.

---

#### Utilização

1. Mova o arquivo `terraform.tfvars.example` para `terraform.tfvars` e altere os valor com suas informações.

```bash
mv terraform.tfvars.example terraform.tfvars
```

2. Inicialize o Terraform

```bash
terraform init
```

3. Valide o terraform usando o `terraform plan` e em seguida, aplique as modificações propostas.

```bash
terraform apply
```

*NOTA*: Ao finalizar essa criação, não esqueça de excluir os recursos, pois o mesmo poderá te cobrar (estaremos criando uma instância virtual). Para destruir, basta executar o comando:

```bash
terraform destroy
```
