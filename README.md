# Azure Event Hub Simulator

Python utility for simulating events to Azure Event Hub using predefined dataset.

## Pre-requisite

- [Terraform](https://www.terraform.io/downloads.html)
- [Python 3](https://www.python.org/downloads/) or [Anaconda with Python 3](https://www.anaconda.com/distribution/)

## Getting Started

- Clone the repository

- In `./terraform`:
  - Change `prefix` in `variables.tf` because Azure Event Hubs Namespace name has to be globally unique
    - For the remainder of the documentation, the prefix `azure-eh` **WILL BE ASSUMED**
  - Run `terraform init`
  - Run `terraform plan -out=out.tfplan`
  - Run `terraform apply out.tfplan`
  - Note the outputs of `terraform apply`

---

### PLEASE NOTE FOR THE ENTIRETY OF THIS REPOSITORY AND ALL ASSETS

1. No warranties or guarantees are made or implied.
2. All assets here are provided by me "as is". Use at your own risk. Validate before use.
3. I am not representing my employer with these assets, and my employer assumes no liability whatsoever, and will not provide support, for any use of these assets.
4. Use of the assets in this repo in your Azure environment may or will incur Azure usage and charges. You are completely responsible for monitoring and managing your Azure usage.

---

Unless otherwise noted, all assets here are authored by me. Feel free to examine, learn from, comment, and re-use (subject to the above) as needed and without intellectual property restrictions.

If anything here helps you, attribution and/or a quick note is much appreciated.