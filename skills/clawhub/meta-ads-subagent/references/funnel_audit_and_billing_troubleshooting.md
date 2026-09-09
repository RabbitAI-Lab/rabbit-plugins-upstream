# Auditoria de Funil de Conversão & Resolução de Problemas de Cobrança Meta Ads

Guia prático para diagnóstico de tráfego, resolução de falsos bloqueios de saldo e otimização de conversão pós-clique no ecossistema Meta Ads.

---

## 1. Falso Alarme: "Restrição da Conta de Anúncio" no App Mobile da Meta

### O Problema
Em contas com modalidade **pré-paga** (`is_prepay_account: true`), quando o saldo chega a **R$ 0,00** e o valor gasto atinge o teto pré-pago (`amount_spent == spend_cap`):
1. A Meta pausa temporariamente a veiculação de anúncios.
2. O aplicativo mobile exibe uma tela travada com o aviso:
   > *"Restrição da conta de anúncio - Você pode ver o status das suas contas e solicitar análises acessando a Página Inicial do Suporte para Empresas em um computador."*
3. O app mobile frequentemente bloqueia recargas in-app devido a políticas de lojas de aplicativos (Apple/Google).

### Diagnóstico via Graph API
Sempre consulte os dados brutos da conta antes de abrir chamados ou se preocupar com banimento:
```python
# GET https://graph.facebook.com/v21.0/act_<AD_ACCOUNT_ID>?fields=account_status,disable_reason,spend_cap,amount_spent,is_prepay_account
```
* Se `account_status: 1` (Ativo) e `disable_reason: 0` (Nenhum), a conta está **100% saudável** e apenas sem saldo.

### Solução
- Recarregar via navegador web (PIX, Boleto ou Cartão) no link direto de cobrança:
  `https://adsmanager.facebook.com/billing_hub/payment_settings?act=<AD_ACCOUNT_ID>`
- Assim que o PIX compensa, o saldo é creditado, o limite de gastos expande automaticamente e a entrega dos anúncios é destravada sem intervenção manual.

---

## 2. Diagnóstico de Funil Pós-Clique (Alto CTR / Baixo CPC, mas 0 Conversões)

Quando campanhas de tráfego/conversão atingem métricas de anúncio excelentes (ex: CTR 3% a 5%+, CPC < R$ 0,20), mas não geram clientes pagantes ou cadastros, o gargalo reside **exclusivamente na jornada pós-clique**:

### Principais Fricções a Auditar:

1. **Aba de Autenticação Padrão (`/auth`):**
   - Se o botão da Landing Page ("Começar agora", "Criar minha Z-AI") direciona para `/auth` com a aba "Entrar / Sign In" selecionada por padrão, o tráfego frio desiste acreditando que já precisa ter login.
   - **Ação:** Passar parâmetro (ex: `/auth?tab=signup` ou `/auth?plan=...`) e forçar a aba **"Criar Conta"** como default quando houver parâmetro de plano/cadastro.

2. **Exigência Prematura de Dados Sensíveis (CPF/CNPJ):**
   - Exigir CPF/CNPJ no primeiro formulário de cadastro cria uma barreira de atrito que derruba a taxa de conversão em 70% a 85%.
   - **Ação:** Coletar apenas **Nome, E-mail, WhatsApp e Senha** no primeiro acesso. Reservar CPF/CNPJ estritamente para o momento do checkout/pagamento no painel.

3. **Falta de Demonstração Interativa Imediata:**
   - Tráfego frio de desenvolvedores e tomadores de decisão converte muito mais quando há um teste de baixo atrito (ex: receber ligação de demonstração de 1 min no próprio celular ou testar prompt da IA sem colocar cartão).

---

## 3. Avaliação de Expansão Internacional (LATAM / Países Vizinhos)

Antes de expandir anúncios do Brasil para a América Latina (Argentina, Chile, Colômbia, México, etc.), certifique-se de que os 3 pré-requisitos essenciais estão prontos:

| Pré-Requisito | Descrição | Risco de Iniciar Sem |
| :--- | :--- | :--- |
| **1. Idioma / Localização** | Criativos, áudios da IA e landing page em Espanhol nativo/neutro. | Rejeição imediata do público hispanofalante ao ouvir áudio ou ler copy em PT-BR. |
| **2. Checkout Internacional** | Gateway com suporte a cartões internacionais / moeda USD / Stripe / dLocal (estrangeiros não têm PIX). | Abandono total no checkout devido à incompatibilidade do método de pagamento. |
| **3. Cadastro sem Exigência de CPF** | Formulário de registro adaptado para ID internacional ou sem validação rígida de 11 dígitos do CPF. | Bloqueio total no envio do formulário de registro. |

**Regra de Ouro:** Otimize a taxa de conversão doméstica no Brasil antes de alocar orçamento em novos territórios.
