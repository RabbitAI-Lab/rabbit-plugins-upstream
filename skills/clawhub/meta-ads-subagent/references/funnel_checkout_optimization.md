# Otimização de Funil e Telas de Conversão para Tráfego Pago

Ao rodar campanhas no Meta Ads (ou outras redes de tráfego pago), a experiência pós-clique na Landing Page e na tela de Autenticação/Checkout determina diretamente a taxa de conversão (CVR) e o Custo por Aquisição (CPA).

---

## 1. Redução de Fricção no Primeiro Cadastro (Sign Up)
- **Campos Mínimos no Topo do Funil:** Para leads oriundos de anúncios, solicite inicialmente apenas os dados essenciais para identificação e ativação (Nome, Telefone/WhatsApp, E-mail, Senha).
- **Postergamento de Dados Fiscais:** Evite exigir CPF/CNPJ logo no primeiro formulário se o pagamento só ocorrer no painel interno. Quando for necessário solicitar documentos fiscais no cadastro, implemente fallback inteligente.

---

## 2. Internacionalização e Adaptação Dinâmica por DDI
Se a campanha ou o produto aceitar tráfego de outros países (LATAM, EUA, Europa):
- **Seletor de DDI:** Permitir escolha rápida de país (`+55`, `+1`, `+351`, `+54`, `+52`, `+34`, `Outro`).
- **Validação Condicional de CPF/CNPJ:**
  - `DDI == +55`: Exigir e validar 11 ou 14 dígitos (CPF/CNPJ) com máscara brasileira.
  - `DDI != +55`: Tornar o campo opcional (`Document / Tax ID (Optional)`), sem aplicar máscara de CPF/CNPJ que travaria o preenchimento de estrangeiros.
- **Formatação de Telefone:** Desativar a máscara de DDD brasileiro para números internacionais, preservando os dígitos limpos.

---

## 3. Deep Linking Direto para a Aba de Cadastro
- **Abertura Inteligente de Abas:** Páginas de autenticação frequentemente compartilham a mesma rota para Login e Cadastro (ex: `/auth`).
- **Padrão de Roteamento:** Links de CTA em anúncios ou landing pages devem conter parâmetros que ativem imediatamente a aba de criação de conta (`/auth?tab=signup` ou `?plan=...`), evitando que o usuário caia em "Entrar / Login" e desista por confusão.

---

## 4. Preservação de UTMs e Disparo de Eventos do Pixel
- **Captura e Persistência de Atribuição:** Armazenar `utm_source`, `utm_campaign`, `utm_content`, `fbclid` e `gclid` em `sessionStorage` no primeiro hit do visitante.
- **Eventos Padrão do Meta Pixel:**
  - Clique no CTA da Landing Page: Disparar `Lead` ou `InitiateCheckout`.
  - Conclusão do formulário de cadastro: Disparar `CompleteRegistration`.
