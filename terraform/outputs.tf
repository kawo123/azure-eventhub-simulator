output "eventhub_namespace_primary_connection_string" {
  value = "${azurerm_eventhub_namespace.eh-namespace.default_primary_connection_string}"
}
