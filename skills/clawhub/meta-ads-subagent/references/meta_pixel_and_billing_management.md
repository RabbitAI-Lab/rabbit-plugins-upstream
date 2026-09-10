# Guia de Gestão de Meta Pixel, Auditoria Financeira e Resolução de Erros de API

Este documento técnico reúne os procedimentos operacionais para criação, injeção e validação do Meta Pixel em SPAs/Landing Pages, diagnóstico de saldo/limites de gastos (*Spend Cap*) e tratamento de erros comuns da Meta Graph API.

---

## 1. Ciclo de Vida e Instalação do Meta Pixel

### 1.1 Criação ou Consulta via Graph API
Ao configurar o rastreamento de um novo domínio ou produto:
- **Consulta de Metadados:** `GET /{pixel_id}?fields=id,name,is_unavailable,last_fired_time,first_party_cookie_status`
- **Criação de Pixel na Conta:** `POST /act_{ad_account_id}/adspixels` com `name="[Nome] Meta Pixel Oficial"`

### 1.2 Código Padrão para SPAs (React / Vite / Next.js / HTML)
Insira no `<head>` do arquivo principal (`index.html` ou `_document.tsx`):

```html
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'SEU_PIXEL_ID');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=SEU_PIXEL_ID&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->
```

### 1.3 Eventos de Conversão Customizados em Botões (Lead / Checkout)
```javascript
// Disparo no clique de botões de conversão / WhatsApp / Cadastro:
window.fbq && window.fbq('track', 'Lead', { content_name: 'Cadastro Plataforma', value: 0.00, currency: 'BRL' });
```

### 1.4 Validação Remota Automatizada
Para auditar se o site em produção (ex: Vercel/GitHub Pages) publicou o pixel com sucesso, faça a inspeção do HTML retornado:
```python
import urllib.request, re

req = urllib.request.Request('https://papi.api.br', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
pixel_found = re.findall(r'fbevents\.js|fbq\(|1079270794502909', html)
# Confirme a presença dos 3 elementos: fbevents.js, fbq('init', ID) e fbq('track', 'PageView')
```

---

## 2. Auditoria Financeira da Conta e Armadilha do Spend Cap

### 2.1 Campos Críticos de Inspeção Financeira
Ao auditar uma conta de anúncios (`act_{ad_account_id}`), sempre consulte:
- `funding_source_details`: Exibe `type: 20` (Saldo pré-pago) e `display_string` com o valor disponível (ex: `Saldo disponível (R$0,00 BRL)`).
- `spend_cap` (Limite de gastos da conta em centavos).
- `amount_spent` (Total gasto histórico em centavos).
- `balance` (Saldo remanescente em centavos).
- `account_status`: `1` (Ativo), `2` (Desativado/Restrito).
- `disable_reason`: `0` (Sem erros).

### 2.2 Diagnóstico de Contas Pré-Pagas e Pausa Silenciosa de Entrega
- **Comportamento de Entrega Zero:** Em contas com cobrança pré-paga (`funding_source_details.type: 20` via PIX/Boleto/Recarga), quando o saldo disponível atinge `R$ 0,00`, a campanha e seus adsets continuam exibindo status `ACTIVE` e `effective_status: ACTIVE`, mas as impressões e gastos caem para zero sem notificação explícita de erro.
- **Investigação de Causa-Raiz:**
  1. Verifique se `int(spend_cap) <= int(amount_spent)` ou se `funding_source_details.display_string` exibe `R$0,00`.
  2. Inspecione os insights diários (`GET /{campaign_id}/insights?date_preset=maximum&time_increment=1&fields=spend,impressions,clicks,cpc,ctr`) para localizar a data exata em que os últimos centavos foram consumidos.
  3. **Resolução de Erro de Permissão (`#100 Requires business_management permission`):** Se a chamada MCP `get_ad_account` falhar com erro 400 em subcontas, solicite diretamente via Graph API apenas os campos financeiros essenciais: `fields=name,account_status,disable_reason,amount_spent,balance,spend_cap,currency,funding_source_details,min_daily_budget`.

### 2.3 Armadilha do Limite de Gastos Manual (*Spend Cap*) & Contas Pré-Pagas
- **Diagnóstico:** Verifique se `int(spend_cap) <= int(amount_spent)`.
- **Contas Pré-Pagas (Funding Type 20):** Contas pré-pagas recarregadas com PIX/Boleto não aceitam alteração direta de `spend_cap` via API (`error_subcode: 1487840: "Essa alteração é inválida para uma conta pré-paga."`). Nelas, os anúncios e posts impulsionados no Instagram consomem diretamente do saldo disponível sem travas manuais.
- **Link do Billing Hub:** Caso precise redefinir limites em contas pós-pagas:
  - `https://adsmanager.facebook.com/ads/manager/billing_hub/summary/?act={account_id_sem_act}`

### 2.3 Orçamento Mínimo Diário por Conjunto em BRL (Subcode 1885272)
- A Meta exige um piso mínimo diário de ~US$ 1,00 por conjunto de anúncios (atualmente **R$ 5,21 a R$ 5,22 / dia**).
- Tentar definir `daily_budget` abaixo disso (ex: R$ 5,00 = 500 cents) dispara o erro `1885272: "O orçamento é muito baixo. Seu orçamento do conjunto de anúncios deve ser superior a R$5,21"`.
- **Estratégia para Validações Low-Cost (ex: R$ 10/dia total com 2 públicos):** Alocar **R$ 5,50/dia** (550 cents) em cada Ad Set (total R$ 11,00/dia), permitindo teste A/B de públicos por 4 a 5 dias com R$ 50 de saldo.

### 2.4 Entrega no Instagram via PBIA (Page-Backed Instagram Account)
- Quando a Página do Facebook não possui conta do Instagram vinculada diretamente, utilize o recurso de **PBIA** (`page_backed_instagram_account_id`).
- Isso libera todos os posicionamentos do Instagram (`INSTAGRAM_STANDARD`, `INSTAGRAM_STORY`, `INSTAGRAM_REELS`, `INSTAGRAM_EXPLORE`).
- O anúncio é exibido no Instagram com o nome e foto de perfil da Página do Facebook anunciante, direcionando os cliques para a URL de destino da campanha.

---

## 3. Resolução de Erros da Meta Graph API (Criativos e Anúncios)

### 3.1 Erro Subcode 1815520 (*"O criativo do anúncio não está usando um link válido"*)
- **Causa:** Ocorre quando `link_data.link` e `link_data.call_to_action.value.link` não coincidem perfeitamente ou contêm parâmetros de URL que ainda não foram sincronizados entre conjuntos de anúncios com otimização `LINK_CLICKS`.
- **Solução:**
  1. Garanta que a URL de destino seja idêntica no `link` principal e no `call_to_action.value.link`.
  2. Em campanhas multi-adset com UTMs distintas, crie `adcreative`s específicos para cada AdSet em vez de compartilhar o mesmo criativo com links divergentes.

### 3.2 Indexação Imediata de Imagens na API
- Para evitar erros de *Imagem não encontrada* (`error_code: 2446386`), faça o upload do arquivo binário diretamente via `multipart/form-data` para `/{ad_account_id}/adimages`:
  ```python
  with open('criativo.png', 'rb') as f:
      files = {'filename': ('criativo.png', f, 'image/png')}
      res = requests.post(f'https://graph.facebook.com/v21.0/{ad_account_id}/adimages', params={'access_token': token}, files=files).json()
      image_hash = res['images']['criativo.png']['hash']
  ```
  Isso garante retorno instantâneo do `hash` já propagado na CDN da Meta.
