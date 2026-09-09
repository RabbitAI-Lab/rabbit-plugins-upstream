# 📋 Playbook de Auditoria, Stop-Loss e Integridade Meta Ads

Este guia detalha o fluxo de auditoria automatizada para contas de anúncios Meta Ads via MCP/API.

---

## 1. 💰 Verificação de Saldo Pré-pago e Spend Cap
Ao auditar uma conta (`act_XXX`):
- Consultar campos `amount_spent`, `spend_cap`, `balance`, `is_prepay_account`.
- **Heurística de Risco de Saldo:**
  - Se `is_prepay_account == true` e `balance < (gasto_diário_total * 1.5)` ou `balance < R$ 20,00`, emitir alerta prioritário no topo do relatório executivo recomendando emissão imediata de PIX/boleto para evitar interrupção no leilão.
  - Se `amount_spent >= spend_cap` e `spend_cap > 0`, a conta pausará silenciosamente. Notificar para reajuste do limite de gastos.

---

## 2. 🔗 Validação de Integridade de Landing Pages (LPs)
Antes de escalar ou manter anúncios ativos:
- **Extração Recursiva de URLs de Destino:**
  1. `creative.object_story_spec.link_data.link` ou `call_to_action.value.link`
  2. `creative.object_story_spec.video_data.call_to_action.value.link`
  3. `creative.asset_feed_spec.link_urls[].website_url`
- **Validação HTTP:**
  - Executar probe HTTP (`curl -sIL -o /dev/null -w "%{http_code}" "<url>"`).
  - **Ação em Caso de Falha:** Se retornar código diferente de `200` ou `301/302` válido (ex: 404, 500, 502, timeout), pausar o anúncio imediatamente via `update_ad(status='PAUSED')` e alertar a equipe.

---

## 3. 🎯 Matriz de Decisão Stop-Loss & Desempenho (+30% CPA/CPC)
- **Janela de Análise:** `last_7d` (ou últimos 3 a 7 dias para contas de alto volume).
- **Classificação de Criativos:**
  - **Estrela / Top Performer:** CTR acima da média da conta, CPC/CPA abaixo do target, volume constante de impressões e cliques.
  - **Em Ramp-up (Novo):** 0 a 100 impressões, 0 spend ou < R$ 5,00 investidos. **NÃO pausar prematuramente**, manter em observação para saída da fase de aprendizado.
  - **Perdedor / Stop-loss Ativado:** CPA ou CPC > 30% acima da meta estabelecida após gastar pelo menos 1x a 2x o CPA target sem conversões. Ação: Pausar via `update_ad`.
  - **Com Falha Técnica (`WITH_ISSUES`):** Mídia corrompida, post de origem deletado ou violação de política. Pausar ou arquivar.

---

## 4. 📱 Formato de Entrega Executiva para Chat / Telegram (< 3.000 caracteres)
Estruturar o relatório com alta densidade de informação:
1. **Cabeçalho:** ID da Conta, Status, Moeda, Saldo disponível e período analisado.
2. **Desempenho de Campanhas & AdSets:** Tabela resumida com Nome do Ad/Criativo, Público, Gasto, Impressões, Cliques, CTR e CPC médio.
3. **Segurança & Stop-Loss:** Status das LPs testadas, verificação de anomalias de leilão.
4. **Integração CRM / GHL (se aplicável):** Leads sem resposta e prioridades de triagem.
5. **Copies Alternativas & Próximas Ações:** Recomendações táticas e novos ganchos (AIDA/PAS).
