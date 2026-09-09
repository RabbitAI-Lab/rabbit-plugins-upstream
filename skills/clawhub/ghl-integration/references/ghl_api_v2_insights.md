# GoHighLevel API v2 Integration Insights

## ⚠️ Limitações Importantes de Webhook na API v2
- **Criação Programática de Webhook:** A API v2 do GoHighLevel não permite criar ou assinar Webhooks via endpoint `/webhooks/` com chaves de Location (Private Integration Tokens / PIT).
- **Solução de Automação:** 
  1. **Configuração Visual:** O usuário adiciona a ação HTTP POST de Webhook dentro do Workflow visual do GHL.
  2. **Path Multi-Tenant:** A URL do Webhook deve incluir o Location ID do cliente (`/webhook/<GHL_LOCATION_ID>`) para permitir o roteamento isolado de contatos no servidor `ghl_webhook_server.py`.
  3. **Fallback Polling:** Caso o cliente prefira não criar o Webhook visual, o Cron Job com a ação `--action unanswered` realiza a varredura autônoma via API REST a cada ciclo.
