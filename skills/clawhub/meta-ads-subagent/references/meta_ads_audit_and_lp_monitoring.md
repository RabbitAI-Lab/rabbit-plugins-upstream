# Protocolo de Auditoria Contínua de Meta Ads, Stop-Loss e Monitoramento de LPs

Este documento estabelece o procedimento padrão para rotinas de auditoria periódica (cron jobs ou comandos manuais) de contas de anúncios Meta Ads, integrando monitoramento de métricas, integridade de Landing Pages (LPs) e triagem de leads no CRM (GoHighLevel/GHL).

---

## 1. Coleta de Métricas e Insights na Graph API v21.0

Ao auditar a conta de anúncios, colete dados em dois níveis: **Campanha** e **Anúncio Individual** (`insights` com `date_preset: 'last_7d'`).

### Métricas Críticas para Análise:
* **Status Financeiro da Conta & Spend Cap (`spend_cap`, `amount_spent`, `balance`):**
  * Verificar sempre `amount_spent` vs `spend_cap` da conta (`get_ad_account`).
  * Se o consumo atingir >95% do limite da conta, disparar alerta CRÍTICO no relatório executivo, pois o Meta interrompe a veiculação de todos os anúncios sem marcar erro de status nos conjuntos ou campanhas.
* **Diagnóstico de Vício de Entrega (Delivery Skew):**
  * Em conjuntos com múltiplos anúncios ativos, verificar se criativos mais antigos estão concentrando a maior parte do orçamento (>70%) apesar de novos criativos apresentarem CTR ou métricas de conversão substancialmente superiores.
  * Ação recomendada: Isolar o novo criativo campeão em conjunto dedicado ou pausar anúncios obsoletos para destravar a distribuição do leilão.
* **Gasto (`spend`):** Total consumido no período.
* **Impressões & Alcance (`impressions`, `reach`, `frequency`):** Frequência ideal entre 1.2 e 2.5 para públicos frios.
* **Cliques & Taxa de Cliques (`clicks`, `link_click`, `ctr`):**
  * `CTR (link_click)` > 1.5%: Bom desempenho.
  * `CTR (link_click)` > 3.0%: Top Performer (candidato a aumento de orçamento).
  * `CTR (link_click)` < 0.8%: Alerta de fadiga ou criativo fraco.
* **Custo por Clique (`cpc`) e Custo por Mil (`cpm`):** Monitorar oscilações bruscas de leilão.
* **Taxa de Conexão de Página (Drop-off):**
  $$\text{Taxa de Conexão} = \frac{\text{Landing Page Views}}{\text{Link Clicks}} \times 100$$
  Se a taxa for inferior a 60%, indica lentidão no carregamento da LP ou rejeição por incompatibilidade móvel.

---

## 2. Regras de Stop-Loss e Ações Automáticas

1. **Stop-Loss de CPA (+30%):**
   * Se o CPA real (ou CPC para campanhas de tráfego) superar o teto estabelecido em mais de 30% e o anúncio tiver acumulado pelo menos $2 \times \text{CPA Alvo}$ de gasto sem converter: **Pausar anúncio imediatamente (`status: PAUSED`)**.
2. **Detecção de Anúncios Quebrados / Rejeitados:**
   * Inspecionar o campo `issues_info` e `effective_status` nos anúncios e criativos.
   * Pausar anúncios com status `DISAPPROVED` ou `WITH_ISSUES`.

---

## 3. Verificação de Saúde das Landing Pages (LP Health & Message Match)

Para cada criativo ativo (`adcreatives`):
1. **Extrair URL de Destino:**
   * Inspecione `object_story_spec.link_data.link`, `video_data.call_to_action.value.link` ou `asset_feed_spec.link_urls[0].website_url`.
2. **Teste HTTP de Conectividade:**
   * Fazer requisição GET/HEAD com timeout de 10s.
   * **Status Esperado:** HTTP 200 OK.
   * **Latência:** Ideal < 500ms (alerta se > 2.0s).
   * **Falhas (4xx/5xx):** Se a LP retornar erro, o anúncio correspondente deve ser pausado imediatamente para evitar queima de orçamento.
3. **Message Match:**
   * Garantir que a oferta, preço (ex: R$ 14,90 / R$ 49,90) e proposta de valor do anúncio correspondam exatamente ao conteúdo visível na página.

---

## 4. Integração com Triagem de Leads CRM (GHL)

* Consultar a API do GHL (`/conversations/search` ou `ghl_client.py --action unanswered`) para garantir que o tráfego gerado pelos anúncios está sendo atendido ou processado pelos fluxos de automação sem retenção indevida na caixa de entrada.

---

## 5. Formatação do Relatório Executivo (Telegram Ready)

O relatório consolidado deve ser direto ao ponto e seguir o limite de até **3.000 caracteres**:
* **Cabeçalho:** Data, status geral (🟢/🟡/🔴) e dados consolidados da conta.
* **Tabela/Lista de Anúncios:** Performance de cada criativo (Gasto, CTR, CPC, LP Views, Status).
* **Status das LPs:** URLs testadas, status HTTP e tempo de resposta.
* **Status CRM:** Conversas pendentes / leads órfãos.
* **Recomendações Táticas:** Ações prioritárias (ajuste de orçamento, criação de novos ganchos, etc.).
