# Landing Page Audit - Conta Ramel & Papi

Última auditoria completa em 02 de Setembro de 2026. Abaixo encontra-se o histórico e mapeamento dos links de destino válidos e testados para as campanhas da conta `act_327126129438619` e ecossistema de tráfego.

## Destinos Válidos e Testados (HTTP Check / Baseline)

| Criativo ID / Origem | URL Original do Link / Criativo | Destino Final (Seguindo Redirecionamentos) | Tipo | Último Status | Latência |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Papi Web / Landing` | `https://papi.api.br` | `https://papi.api.br/` | Landing Page Oficial Papi API WhatsApp | **200 OK** (02/09/2026) | ~0.30s |
| `Evolution Foundation`| `https://evolutionfoundation.com.br/imersao` | `https://evolutionfoundation.com.br/imersao` | Landing Page Oficial Imersão Evolution | **200 OK** (02/09/2026) | ~0.23s |
| `826968350219416` | `https://www.anrdoezrs.net/click-101209511-17083170` | `https://contabo.com/en/vps/...` | Redirecionador Afiliado / VPS Contabo | **200 OK** (02/09/2026) | ~2.28s |
| `840594038926422` | `https://youtu.be/zwXm0MwGHpY` | `https://www.youtube.com/watch?v=zwXm0MwGHpY` | Vídeo do YouTube (Live explosiva Builders Dyad) | **200 OK** (02/09/2026) | ~0.47s |
| `GHL MacDos Booking` | `https://ghl.macdos.online/widget/booking/cAaoX3igXghJqP5TBIMf` | `https://ghl.macdos.online/widget/booking/cAaoX3igXghJqP5TBIMf` | Agendamento de Reuniões MacDos | **200 OK** (02/09/2026) | ~0.67s |
| `978292430913465` | `https://api.whatsapp.com/send` | `https://api.whatsapp.com/send` | Link API de WhatsApp para o DeliveryFlow | **200 OK** (02/09/2026) | ~0.50s |
| `1335408661104848` | `https://api.whatsapp.com/send` | `https://api.whatsapp.com/send` | Link API de WhatsApp para o DeliveryFlow | **200 OK** (02/09/2026) | ~0.50s |
| `Portal ST Hub` | `https://portal.sthub.com.br` | `https://portal.sthub.com.br/` | Portal Oficial ST Hub (SPA Client Login Shell) | **401 (Auth)** (02/09/2026) | ~0.49s |

---

### Observações Técnicas:
1. **Portal ST Hub (401 Response):** O `portal.sthub.com.br` é a casca SPA do GHL Client Portal (`clientclub.net`). Quando chamado sem sessão/token HTTP direto, retorna 401 por padrão do middleware Express/Cloudflare, porém carrega o frontend de login normalmente no browser.
2. **Execução em Lote via Terminal:**
```bash
for url in \
  "https://papi.api.br" \
  "https://evolutionfoundation.com.br/imersao" \
  "https://www.anrdoezrs.net/click-101209511-17083170" \
  "https://youtu.be/zwXm0MwGHpY" \
  "https://api.whatsapp.com/send" \
  "https://ghl.macdos.online/widget/booking/cAaoX3igXghJqP5TBIMf" \
  "https://portal.sthub.com.br"; do
  status=$(curl -sIL -o /dev/null -w "%{http_code} %{time_total}s %{url_effective}\n" "$url")
  echo "$url -> $status"
done
```
