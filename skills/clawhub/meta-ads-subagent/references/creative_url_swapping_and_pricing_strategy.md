# Atualização de URLs de Destino e Estratégia de Precificação / Cupons em SaaS de IA

Este documento registra os procedimentos técnicos para troca de URLs de destino na Meta Graph API e as diretrizes estratégicas de precificação e cupons para campanhas de produtos de entrada (low-ticket B2B / APIs de IA).

---

## 1. Atualização Segura de URL de Destino (Imutabilidade de Ad Creatives)

Na Graph API da Meta, objetos `adcreative` são **imutáveis** quanto à URL de destino (`link` e `call_to_action.value.link`). Não é possível alterar a URL de um criativo existente via PATCH/POST direto.

### Procedimento Correto para Redirecionamento de Tráfego:
1. **Criar Novo `adcreative`:**
   - Obter os dados do criativo atual (imagem `image_hash` ou vídeo `video_id`, mensagem, headline).
   - Fazer `POST /act_{account_id}/adcreatives` com a nova URL em `object_story_spec.link_data.link` e `object_story_spec.link_data.call_to_action.value.link`.
   - Manter os parâmetros UTM de rastreamento sincronizados (ex: `utm_source=meta_ads&utm_medium=feed&utm_campaign=...`).
   - Sincronizar o `instagram_user_id` / `page_backed_instagram_account_id` para manter a veiculação no Instagram ativa.
2. **Atualizar o Anúncio Ativo (`ad`):**
   - Fazer `POST /{ad_id}` passando `creative: {"creative_id": "<novo_creative_id>"}`.
   - O status do anúncio transiciona para `IN_PROCESS` e em seguida `ACTIVE` sem perder o histórico do conjunto (`adset`).

---

## 2. Estratégia de Precificação & Cupons em Fase Inicial de Tráfego

Ao rodar campanhas para produtos de IA/API com preços agressivos de entrada (ex: R$ 14,90/mês WhatsApp ou R$ 49,90/mês Voz com IA):

### 🚫 O que NÃO fazer nas primeiras 48h-72h de tráfego:
- **Não baixar o preço público na Landing Page de forma precipitada:** Reduzir preços públicos de R$ 49,90 para R$ 25,00 atrai curiosos desqualificados e desvaloriza a percepção tecnológica da solução.
- **Não expor cupons abertos na Home:** Cupons públicos generalizados corroem a margem antes de validar se o gargalo é preço ou objeção de confiança/teste.

### ✅ Melhores Práticas de Conversão:
1. **Manter Preço Âncora com Gatilho de Lançamento:**
   - Exibir na LP o preço cheio com contexto de oportunidade (ex: *"Preço promocional de lançamento — Primeiras 100 instâncias"*).
2. **Cupons Conversacionais como Arma de Fechamento (1-on-1):**
   - Direcionar dúvidas e leads hesitantes para o WhatsApp / GHL.
   - Aplicar cupom de desconto (ex: `PAPI50` - 50% OFF no 1º mês) ou bônus de créditos/minutos (ex: 100 minutos grátis para homologação) estritamente na conversa direta para quebrar a última hesitação do desenvolvedor/gestor.
3. **Foco na Demonstração Interativa:**
   - Em soluções de Voz com IA, a demonstração de áudio interativa na LP converte mais do que cortes agressivos de preço.
