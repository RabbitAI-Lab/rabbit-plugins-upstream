# Padrões de Triagem e Classificação de Leads Inbound no GoHighLevel (GHL)

Este guia orienta a categorização e priorização autônoma de conversas com mensagens inbound pendentes capturadas via GoHighLevel API (`ghl_client.py` / `/conversations/search`).

---

## 1. Categorias de Classificação de Inbound

Ao inspecionar conversas com mensagens não respondidas (`direction: inbound`), classifique os contatos conforme o padrão abaixo:

| Categoria | Descrição / Padrão de Mensagem | Prioridade | Ação Recomendada |
| :--- | :--- | :--- | :--- |
| **🔥 Comercial / Fechamento** | Perguntas diretas sobre propostas, contratação, envio de link de pagamento ou dúvidas sobre valores (*"conseguiu formular a proposta", "como assino o plano"*). | **Alta (Imediata)** | Encaminhar para o vendedor ou responder com a proposta/link de contratação. |
| **⚡ Engajamento / Qualificação** | Respostas diretas a comunicados, reações emoji ou pedidos de explicação (*"Fala pra mim", "Como funciona?", "Onde?"*). | **Média-Alta** | Disparar mensagem de qualificação em 3 passos via WhatsApp/SMS STEVO. |
| **💬 Contato Inicial / Saudação** | Mensagens de abertura sem contexto prévio (*"Olá bom dia", "Tudo bem?"*). | **Média** | Responder cordialmente, apresentar o portfólio (WhatsApp API / Voz com IA) e questionar o objetivo do lead. |
| **🎙️ Áudio / Briefing Operacional** | Mensagens de voz transcritas contendo orientações técnicas, solicitações de suporte ou alinhamentos de grupo. | **Operacional** | Analisar a transcrição e registrar no CRM/Kanban para execução. |
| **🚫 Ruído / Transacional / Broadcast** | Códigos de segurança (ex: 2FA Facebook), disparos em massa recebidos de terceiros ou respostas automáticas de bots. | **Ignorar / Baixa** | Não registrar como lead quente; marcar como lido ou arquivar sem disparar follow-up. |

---

## 2. Execução via `ghl_client.py`

Para automatizar a verificação:
```bash
# Listar conversas pendentes
python3 /root/.hermes/metaads/ghl_client.py --action unanswered
```

Ao processar cada conversa:
1. Obtenha as mensagens ordenadas cronologicamente (`dateAdded`).
2. Se a última mensagem for `direction: inbound`, aplique o filtro de ruído acima antes de classificar.
3. Formate o relatório consolidado destacando Nome, Telefone mascarado, Nível de Prioridade e Ação imediata.
