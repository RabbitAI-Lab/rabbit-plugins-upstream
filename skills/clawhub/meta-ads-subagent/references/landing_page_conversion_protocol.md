# Protocolo de Conversão de Landing Pages e Alinhamento Criativo (Meta Ads)

Este guia define a governança, as regras de validação prévia com o usuário e as diretrizes de otimização de conversão para Landing Pages integradas a campanhas de tráfego pago (Meta Ads).

---

## 1. Regra de Governança: Validação e Aprovação Prévia Obrigatória

**REGRA INVIOLÁVEL:** O agente NUNCA deve aplicar alterações de código, layout ou copy diretamente em uma Landing Page ativa sem antes:
1. **Apresentar o Diagnóstico Completo:** Explicar claramente onde está o vazamento de conversão (gargalo de cliques, carregamento, copy ou oferta).
2. **Apresentar a Proposta Estruturada:** Detalhar seção por seção (Hero, Players/Demos, Benefícios, Oferta/Planos, FAQ e CTAs) com os textos exatos e componentes visuais.
3. **Aguardar Validação Explícita do Usuário:** Somente após a aprovação do usuário, os arquivos da página devem ser editados ou deployados.

---

## 2. Protocolo "Message Match" (Alinhamento Anúncio ➔ LP)

O principal motivo de alta taxa de rejeição em tráfego pago é a **quebra de expectativa** entre o criativo do anúncio e a primeira dobra da Landing Page.

### Checklist de Alinhamento na 1ª Dobra (Above the Fold):
- **Headline Espelho:** O título da LP deve responder imediatamente à promessa do anúncio (ex: se o anúncio fala de *Chamadas de Voz com IA a R$ 49,90*, a headline da LP deve falar de *Agentes de Voz com IA*, não de chatbots genéricos ou serviços mistos).
- **Prova Sensorial Imediata (Demonstração de Áudio/Voz):**
  - Para produtos de IA de Voz: **É mandatório ter players de áudio reais** nos primeiros 5 segundos de rolagem. O visitante precisa clicar e ouvir a naturalidade da voz humana instantaneamente.
  - Substituir exemplos estáticos ou desconexos (ex: card de restaurante/hambúrguer quando o produto anunciado é automação de voz corporativa).
- **Preço e Oferta Transparentes:**
  - O valor anunciado (ex: R$ 49,90/mês ou R$ 14,90/mês) e incentivos (ex: Teste Grátis, 50% OFF no primeiro mês) devem estar explícitos em cards destacados com botões diretos de checkout/cadastro.

---

## 3. Diagnóstico de Funil: Métricas de Queda e Soluções

| Sintoma Identificado | Causa Raiz | Ação Recomendada |
| :--- | :--- | :--- |
| **Cliques altos e baratos (CPC baixo), mas LPV < 30%** | Meta entregando para quem clica por engano e fecha antes do site carregar. | Alterar a meta de otimização do conjunto de anúncios de `LINK_CLICKS` para `LANDING_PAGE_VIEWS`. |
| **LPVs normais, mas zero conversões/contatos** | Falta de CTA direto, formulário longo ou fricção no cadastro. | Adicionar botão flutuante de WhatsApp Click-to-Chat com mensagem pré-preenchida de cupom/teste. |
| **Pixel sem dados de conversão** | Pixel disparando apenas `PageView` genérico. | Adicionar disparos manuais `fbq('track', 'Lead')` ou `fbq('track', 'Contact')` nos cliques de botões principais. |
| **Anúncio de alto CTR recebendo pouca verba** | Algoritmo concentrou entrega no anúncio mais antigo. | Pausar o criativo perdedor ou isolar o criativo vencedor em conjunto próprio. |
| **Pausa iminente por limite de conta** | Limite de gastos (`spend_cap`) da conta de anúncios atingindo o teto. | Monitorar `amount_spent` vs `spend_cap` e alertar o usuário para aumentar o teto no Gerenciador. |

---

## 4. Estrutura de Alta Conversão para Landing Page de IA Conversacional / Voz

1. **Hero Section:** Headline de benefício tangível + badge de lançamento + CTAs duplos (Ouvir Demonstração / Começar Agora) + chips de diferenciais (latência < 500ms, integrações).
2. **Voice Showcase (Players Interativos):** 3 cards com áudios curtos (15-30s) demonstrando: Vendas Ativas, Confirmação de Agendamento e Suporte Financeiro.
3. **Como Funciona (3 Passos):** Prompt ➔ Conexão/MCPs ➔ Atendimento 24/7.
4. **Tabela / Cards de Planos:** Preço destacado (ex: R$ 49,90), lista de recursos, bônus de ativação e botão de compra.
5. **FAQ Técnico & Comercial:** Respostas diretas sobre latência, compatibilidade (CRMs/n8n/Webhooks) e número próprio de WhatsApp.
6. **Sticky CTA / WhatsApp Direct:** Banner final com link direto para falar com especialista técnico.
