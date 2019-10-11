provider "azurerm" {
    version = "=1.33.1"
}

resource "azurerm_resource_group" "eh-rg" {
  name     = "${var.prefix}-rg"
  location = "${var.location}"
}

resource "azurerm_eventhub_namespace" "eh-namespace" {
  name                = "${var.prefix}-eh-namespace"
  location            = "${azurerm_resource_group.eh-rg.location}"
  resource_group_name = "${azurerm_resource_group.eh-rg.name}"
  sku                 = "Standard"
  capacity            = 1
  kafka_enabled       = true
}

resource "azurerm_eventhub" "eh" {
  name                = "${var.prefix}-eh"
  namespace_name      = "${azurerm_eventhub_namespace.eh-namespace.name}"
  resource_group_name = "${azurerm_resource_group.eh-rg.name}"
  partition_count     = 2
  message_retention   = 1
}
