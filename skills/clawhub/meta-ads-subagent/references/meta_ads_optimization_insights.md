# Meta Ads API — Insights e Comportamentos Documentados

## Conta Ramel: act_327126129438619
- **Business:** Ramel Tecnologia e Desenvolvimento (ID: 100754338860752)
- **Page:** Ramel Segurança E Tecnologia (actor_id: 112665111651993) | Limite: 250 anúncios ativos.
- **Moeda:** BRL | **Timezone:** America/Sao_Paulo (-3)

---

## 📊 Desempenho Real da Campanha PAPI (2026-08-31)
- **Campanha Ativa:** `[PAPI] API WhatsApp & Voz com IA - Brasil 2026` (`120253513047410154`)
- **Status Financeiro:** `spend_cap`: R$ 354,83 | `amount_spent`: R$ 315,90 | **Saldo restante:** ~R$ 38,93 antes da pausa automática por limite de gastos.
- **Métricas Globais:**
  - Gasto: R$ 4,99 | Alcance: 6.132 | Impressões: 8.984 (Freq: 1.47)
  - Cliques: 60 no link (63 total) | CPC Médio: R$ 0,08 | CPM: R$ 0,56 | CTR Médio: 0,70%
- **Comparativo de Públicos:**
  - `02 - IA & Automação`: CTR 1,54% | CPC R$ 0,05 (Público de alta afinidade e menor custo por lead/clique).
  - `01 - Devs & Software`: CTR 0,49% | CPC R$ 0,10 (Volume bruto maior, porém menor CTR).
- **Comparativo de Criativos:**
  - `AD 02 (Voz IA R$ 49,90)`: CTR de 1,96% (IA) e 1,27% (Devs) com CPC de **R$ 0,04** — criativo com altíssimo apelo e curiosidade.
  - `AD 01 (WhatsApp R$ 14,90)`: CTR de 1,52% (IA) e 0,45% (Devs) com CPC de R$ 0,06 a R$ 0,11.

---

## 🔴 Spend Cap / Saldo Esgotado (2026-08-12)
- `spend_cap`: 31090 (R$ 310,90)
- `amount_spent`: 31091 (R$ 310,91) — excedeu por R$ 1,00 por latência
- `balance`: 0 | `funding_source_details.display_string`: "Saldo disponível (R$0,00 BRL)"
- **Ação:** Todos os insights pulados (retornariam `{"data": []}`). Todas as 5 campanhas estavam PAUSED.
- **Regra:** `amount_spent >= spend_cap` → conta esgotada, pular insights.

---

## ⛔ Erro 3907143 — "Sua mídia é inválida" (Confirmado 2026-08-12)
- **Ad ID afetado:** `120240553069670154` (campanha `120240553067550154`)
- **Tentativa:** `mcp_meta_ads_update_ad` com `status=PAUSED`
- **Retorno:** `HTTP 400, code 1/3907143: "Sua mídia é inválida" (fbtrace_id: AyWlngcxrgR7ffcXBMXiWnP)`
- **Diagnóstico:** Anúncio com creative `826968350219416` tem mídia descontinuada no backend do Meta.
- **Workaround confirmado:** Campanha-pai já estava PAUSED → veiculação interrompida de fato. Não insistir na chamada; documentar erro e verificar nível de campanha primeiro.

---

## ⚠️ Erro 1870250 — Público Descontinuado (WITH_ISSUES)
- **AdSet afetado:** `120240553068690154`
- **Mensagem:** "Este conjunto de anúncios não está sendo veiculado porque usa opções de direcionamento detalhado que foram combinadas."
- **Estado:** Campanha PAUSED + AdSet PAUSED — sem risco de spend.
- **Ação necessária:** Editar o targeting do AdSet removendo combinações depreciadas antes de reativar.

---

## ✅ Landing Pages Verificadas (2026-08-12)
| URL | HTTP | Destino Final |
|-----|------|---------------|
| `https://www.anrdoezrs.net/click-101209511-17083170` | 200 | `https://contabo.com/en/vps/?...` (Afiliado legítimo) |
| `https://youtu.be/zwXm0MwGHpY` | 200 | `https://www.youtube.com/watch?v=zwXm0MwGHpY` |
| `https://api.whatsapp.com/send` | 200 | `https://api.whatsapp.com/send` |

---

## 📌 Criativos Ativos e Seus Destinos (Mapeamento Rápido)
| Creative ID | Destino Principal | Tipo |
|---|---|---|
| `931715969406929` | Post IG orgânico (ODOO WEEK #5 VoIP) | WATCH_MORE |
| `826968350219416` | `https://www.anrdoezrs.net/click-101209511-17083170` | Link de afiliado Contabo |
| `840594038926422` | `https://youtu.be/zwXm0MwGHpY` (embutido em body) | YouTube Live |
| `978292430913465` | `https://api.whatsapp.com/send` | WhatsApp DeliveryFlow |
| `1335408661104848` | `https://api.whatsapp.com/send` | WhatsApp DeliveryFlow |

---

## 📱 GHL Leads Sem Resposta — Padrões de Triagem Observados (2026-08-12)
8 conversas identificadas via `ghl_client.py --action unanswered`. Nota: o `id` retornado = **Conversation ID**, não Contact ID. Para ações como `send_msg`, buscar `contactId` via `/conversations/search`.

| Conversa ID | Lead | Classificação |
|---|---|---|
| `DrD0JLtBVCMyvJpho9tO` | Lenine Junior | Aguardando análise (imagem recebida) |
| `C56MEX4rJeqJuX3TQSpY` | Sinivaldo Filho | Inbound humano ativo |
| `nWR1wnvuE6igwUnEiEtE` | Rafa Martins | Notificação de sistema / admin |
| `HTqNd6BpKSuPT1ksQoG9` | Joel | Conversa comercial em andamento |
| `Y7RI5dgqvhOluOTTDV31` | Line | Urgência interna / equipe |
| `DgSC4DkDTZRzR8QANoDp` | Financeiro BV / Rock Telecom | Faturamento / promessa de pagamento |
| `tOIh63TgESqnXzYPaOAI` | Thais | Suporte operacional (RAT do dia) |
| `ipIEzDl6LDawLB912RPT` | fm9070519@gmail.com | Informal / encerramento |
