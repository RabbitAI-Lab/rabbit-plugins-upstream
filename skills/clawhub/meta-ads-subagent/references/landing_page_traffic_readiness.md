# Checklist de Validação Pré-Tráfego da Landing Page (Meta Ads)

Antes de ativar ou direcionar orçamento de campanhas no Meta Ads para uma landing page de destino, realize a auditoria pré-voo em 4 pilares:

---

## 1. Congruência Anúncio-Página (Ad-to-Page Message Match)
- **Headline & Hero:** A promessa central do criativo (texto, preço e proposta de valor) deve estar imediatamente visível no primeiro scroll (above the fold) da página.
- **Transparência de Preço / Oferta:** Se o anúncio cita "R$ 49,90" ou "A partir de R$ 14,90", o mesmo plano com os mesmos valores deve estar destacado na página para evitar rejeição e abandono de carrinho.
- **Identidade Visual e Tom:** Cores, logos e posicionamento de marca devem manter coerência com o criativo anunciado.

---

## 2. Prova de Conceito Interativa (Live Demo / Prova Social)
- **Demonstração Funcional:** Para produtos SaaS, IA ou automação, players interativos (áudio de voz, demonstração de chat ou vídeo curto) convertem até 3x mais que textos estáticos.
- **Cenários Segmentados:** Oferecer 2 a 3 casos de uso reais (ex: Vendas Ativas, Anti-No-Show, Suporte Omnichannel) para o visitante se auto-identificar rapidamente.

---

## 3. Rastreamento e Pixel Meta (Pre-Flight Check)
- **Instalação do Pixel:** Verificar se o script `fbevents.js` e o identificador do Pixel do anunciante (ex: `1079270794502909`) estão carregados e disparando o evento `PageView`.
- **Eventos de Funil:**
  - Clique em CTA de Compra/Assinatura ➔ disparar `InitiateCheckout` ou redirecionar com tracking do plano (`/auth?plan=...`).
  - Clique em WhatsApp ➔ disparar evento customizado ou `Contact` / `Lead`.
- **OpenGraph & Meta Tags:** Validar `og:image`, `og:title` e `og:description` para compartilhamentos sociais e consistência da marca.

---

## 4. Rotas de Conversão Claras (Dois Caminhos)
- **Caminho 1 (Self-Service / Baixo Atrito):** Botão direto para criação de conta / checkout com plano pré-selecionado (`/auth?plan=voice_starter`).
- **Caminho 2 (Conversacional / Alto Ticket):** Botão de WhatsApp direto com mensagem inicial contextualizada para tirar dúvidas comerciais com o time de vendas.
