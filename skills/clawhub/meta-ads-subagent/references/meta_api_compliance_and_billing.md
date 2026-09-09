# Meta Ads API: Compliance, Faturamento e Otimização de Funil

Este documento detalha resoluções técnicas para erros de API recentes (Graph API v21.0+), particularidades de contas pré-pagas e diretrizes de auditoria de conversão para tráfego pago B2B/SaaS.

---

## 1. Compliance e Anunciante Ausente (Meta Error 100 / Subcode 3858634)

### Sintoma do Erro
Ao tentar atualizar orçamento (`daily_budget`), status ou segmentação de um conjunto de anúncios (`adset`) no Brasil ou regiões com regras de transparência, a API retorna:
```json
# Meta Ads API: Compliance, Faturamento e Otimização de Funil

Este documento detalha resoluções técnicas para erros de API recentes (Graph API v20.0+ / v21.0+), criação e duplicação de campanhas de conversão, particularidades de contas pré-pagas e diretrizes de auditoria de conversão para tráfego pago B2B/SaaS.

---

## 0. Regra de Ouro: Vendas = Sempre Conversão com Pixel

- **Diretriz:** Toda campanha focada em vendas ou faturamento deve obrigatoriamente ser configurada com objetivo `OUTCOME_SALES` e conjunto com `optimization_goal=OFFSITE_CONVERSIONS`, associado ao Meta Pixel e evento `PURCHASE`. Tráfego (`OUTCOME_TRAFFIC` / `LINK_CLICKS`) deve ser evitado para metas de venda, pois o algoritmo otimiza apenas para cliques baratos sem qualificação de compra.
- **Rascunho de Segurança:** Em operações de reestruturação e duplicação, criar todos os níveis (Campanha, AdSets, Ads) com `status="PAUSED"`.

---

## 1. Compliance e Anunciante Ausente (Meta Error 100 / Subcode 3858634)

### Sintoma do Erro
Ao tentar criar ou atualizar orçamento (`daily_budget`), status ou segmentação de um conjunto de anúncios (`adset`) no Brasil ou regiões com regras de transparência, a API retorna:
```json
{
  "error": {
    "message": "Invalid parameter",
    "type": "OAuthException",
    "code": 100,
    "error_data": "{\"blame_field_specs\":[[\"compliance_section\"]]}",
    "error_subcode": 3858634,
    "error_user_title": "O anunciante está ausente",
    "error_user_msg": "Forneça um anunciante verificado para que os anúncios neste conjunto de anúncios sejam veiculados a públicos nas localizações selecionadas."
  }
}
```

### Causa
A Graph API exige a declaração explícita das identidades do beneficiário e do pagador (`regional_regulation_identities` / `compliance_section`) associadas a um Business Manager verificado ou Página oficial.

### Solução via API
Ao criar ou atualizar o adset, passe `regional_regulated_categories` e `regional_regulation_identities` com o ID numérico do Business Manager (`bm_id`):

```python
import json
import requests

bm_id = "100754338860752"  # ID numérico do Business Manager / Pagador

url = f"https://graph.facebook.com/v20.0/act_{ad_account_id}/adsets"
data = {
    "access_token": token,
    "campaign_id": campaign_id,
    "name": "AdSet Name",
    "daily_budget": 1000,
    "billing_event": "IMPRESSIONS",
    "optimization_goal": "OFFSITE_CONVERSIONS",
    "bid_strategy": "LOWEST_COST_WITHOUT_CAP",
    "promoted_object": json.dumps({"pixel_id": pixel_id, "custom_event_type": "PURCHASE"}),
    "regional_regulated_categories": json.dumps(["BRAZIL_REGULATION", "VOLUNTARY_VERIFICATION"]),
    "regional_regulation_identities": json.dumps({
        "universal_beneficiary": bm_id,
        "universal_payer": bm_id
    }),
    "status": "PAUSED"
}
r = requests.post(url, data=data)
```

---

## 1.1. Erros Recorrentes na Criação de Campanhas e AdSets (Graph API v20.0+)

### A. Budget Sharing em Campanhas ABO (Meta Error 100 / Subcode 4834011)
- **Mensagem:** `É necessário especificar True ou False no campo is_adset_budget_sharing_enabled se você não estiver usando o orçamento da campanha.`
- **Solução:** Em campanhas `OUTCOME_SALES` com orçamento a nível de conjunto (ABO), envie `is_adset_budget_sharing_enabled=false` no `POST /campaigns`.

### B. Exigência de Lance em AdSet de Conversão (Meta Error 100 / Subcode 2490487)
- **Mensagem:** `O valor ou as restrições de lance são obrigatórios para a estratégia de lance`
- **Solução:** Quando o conjunto for de conversão (`OFFSITE_CONVERSIONS`), defina explicitamente `bid_strategy=LOWEST_COST_WITHOUT_CAP` para não ser obrigado a passar `bid_amount`.

---
```

**⚠️ Regras Críticas:**
1. A chave correta é `universal_payer` (com `er`, **NÃO** `universal_payor`).
2. Os valores devem ser **IDs numéricos** válidos (Business ID ou Page ID), nunca strings de texto/razão social.

---

## 2. Falso Positivo de "Restrição de Conta" em Contas Pré-Pagas

### Comportamento no App Mobile
Quando o saldo pré-pago de uma conta Meta Ads zera (`balance: 0` e `amount_spent` atinge o `spend_cap` acumulado), o aplicativo mobile da Meta (iOS/Android) exibe um aviso genérico e alarmista:
> *"Restrição da conta de anúncio: Você pode ver o status das suas contas e solicitar análises acessando a Página Inicial do Suporte para Empresas em um computador."*

O app mobile costuma travar o botão de recarga/pagamento devido a restrições de compras in-app (taxas de 30% da Apple/Google).

### Verificação e Resolução
1. **Validar via API:** Consultar `account_status` (1 = Ativa) e `disable_reason` (0 = Nenhum). A conta não está punida nem violou políticas.
2. **Link Direto de Pagamento:** Orientar o usuário a recarregar diretamente pelo navegador:
   `https://adsmanager.facebook.com/billing_hub/payment_settings?act=<AD_ACCOUNT_ID>`
3. Assim que o PIX/boleto/cartão é compensado, a Meta expande o teto de gastos automaticamente e retoma os anúncios sem necessidade de intervenção manual ou apelação de suporte.

---

## 3. Diretrizes de Auditoria de Funil e Expansão Internacional

### Regras para Expansão Internacional (LATAM / Países Vizinhos)
Nunca expanda campanhas de tráfego para países vizinhos sem validar previamente os 3 pilares:
1. **Idioma:** Criativos, landing page e materiais de áudio devem estar no idioma nativo (Espanhol neutro para LATAM).
2. **Meio de Pagamento:** O público externo não utiliza PIX. É obrigatório ter gateway internacional (Stripe, PayPal, Cartão Internacional em USD/EUR).
3. **Formulário de Cadastro:** Eliminar bloqueios regionais (como exigência de CPF/CNPJ brasileiro).

### Otimização de Conversão no Cadastro (SaaS / B2B)
- **Fricção Mínima no 1º Passo:** Em tráfego frio, exigir apenas *Nome, Email, WhatsApp e Senha*. Exigir CPF/CNPJ antes do teste do produto gera perda de 70% a 85% dos leads.
- **Roteamento de Landing Page (`/auth`):** Links vindos de botões de conversão (ex: `/auth?plan=...`) devem carregar a aba de **Cadastro (Sign Up)** por padrão, evitando que novos visitantes caiam na tela de Login (Sign In).
