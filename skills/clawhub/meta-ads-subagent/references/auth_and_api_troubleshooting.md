# Meta Ads API & MCP Auth Troubleshooting

Guia de diagnóstico e resolução de problemas de autenticação e execução do Meta Ads no Hermes.

---

## 1. Diagnóstico de Token Expirado (OAuthException 190)

Quando o token de acesso da Meta expira ou é revogado:
- **Erro na API:** `{"error": {"message": "Error validating access token: Session has expired...", "type": "OAuthException", "code": 190, "error_subcode": 463}}`
- **Erro no MCP:** `Meta token expired or invalid — HTTP 400, code 190.`

### Verificação Rápida via Terminal:
```bash
python3 -c "
import requests, yaml
with open('/root/.hermes/config.yaml') as f:
    cfg = yaml.safe_load(f)
token = cfg.get('mcp_servers', {}).get('meta-ads', {}).get('env', {}).get('META_ACCESS_TOKEN')
r = requests.get('https://graph.facebook.com/v21.0/me', headers={'Authorization': f'Bearer {token}'})
print('Status:', r.status_code, r.json())
"
```

---

## 2. Procedimento de Atualização do Token

1. **Atualizar Variável de Ambiente:**
   ```bash
   hermes config set META_ACCESS_TOKEN "<novo_token>"
   ```

2. **Atualizar `config.yaml` (bloco `meta-ads.env`):**
   Garantir que `mcp_servers.meta-ads.env.META_ACCESS_TOKEN` receba o novo valor.

3. **Reiniciar Processos Node do MCP:**
   Processos MCP já em execução mantêm as variáveis de ambiente anteriores na memória. Para forçar o reload:
   ```bash
   pkill -f mcp-meta-ads
   ```

4. **Lidar com Backoff do Circuit Breaker:**
   Se o Hermes MCP bloquear chamadas com erro de circuito aberto (*unreachable after N consecutive failures. Auto-retry available in ~Xs*), utilize chamadas REST diretas via Python (`requests.post/get` na `https://graph.facebook.com/v21.0/`) para não interromper a operação.

---

## 3. Falso Bloqueio no App Mobile vs. Saldo Pré-Pago Esgotado

### Sintoma no App Mobile (iOS / Android):
- O anunciante abre o app Meta Ads ou tenta adicionar saldo e se depara com uma tela travada exibindo:
  > *"< Restrição da conta de anúncio: Você pode ver o status das suas contas e solicitar análises acessando a Página Inicial do Suporte para Empresas em um computador."*

### Causa Raiz Técnica:
1. Em contas **pré-pagas** (`is_prepay_account: true`), o limite de gastos (`spend_cap`) é amarrado dinamicamente ao total de recargas acumuladas.
2. Quando o saldo zera (`balance: 0`, `amount_spent == spend_cap`), a veiculação pausa por teto atingido.
3. O app mobile da Meta restringe recargas in-app (políticas de cobrança mobile) e classifica o estado internamente como restrição de veiculação, gerando um falso aviso de banimento/análise.

### Script de Diagnóstico Rápido via API:
```python
import requests, yaml, json

with open('/root/.hermes/config.yaml') as f:
    token = yaml.safe_load(f)['mcp_servers']['meta-ads']['env']['META_ACCESS_TOKEN']

url = 'https://graph.facebook.com/v21.0/act_<AD_ACCOUNT_ID>'
params = {'access_token': token, 'fields': 'account_status,disable_reason,is_prepay_account,balance,spend_cap,amount_spent'}
res = requests.get(url, params=params).json()

# Status 1 e disable_reason 0 = Conta 100% LIMPA (apenas sem saldo)
print(json.dumps(res, indent=2))
```

### Solução e Destravamento:
- **NÃO** é necessário abrir chamado ou solicitar análise de conformidade.
- Envie diretamente o link web de cobrança para o anunciante fazer o PIX/Boleto/Cartão no navegador:
  `https://adsmanager.facebook.com/billing_hub/payment_settings?act=<AD_ACCOUNT_ID>`
- Assim que o PIX compensa, a Meta credita o saldo, expande o `spend_cap` automaticamente e o aviso no app mobile desaparece sem qualquer ação manual.
