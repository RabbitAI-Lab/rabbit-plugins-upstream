# Identidade do Anunciante (Facebook Page) em Campanhas Meta Ads

Todo `adcreative` no ecossistema Meta exige uma **Página do Facebook** em `object_story_spec.page_id`.
Essa Página é a assinatura visível no topo do anúncio (nome + foto). Errar isso queima a
percep\u00e7\u00e3o de marca mesmo com criativo perfeito.

---

## 1. Regra de ouro: escolher a Page ANTES de criar criativos

Nunca deixe o `page_id` ser escolhido "por default" (primeira página retornada pela API).
Antes de gerar qualquer criativo, pergunte/confirme com o usu\u00e1rio qual identidade deve assinar
o an\u00fancio. Para produtos com marca pr\u00f3pria (SaaS/API), o usu\u00e1rio quase sempre quer uma
P\u00e1gina dedicada, n\u00e3o uma p\u00e1gina institucional legada.

### Descoberta de Pages dispon\u00edveis

```python
# Pages que o token pode usar para anunciar (com Page Access Token de cada uma)
requests.get('https://graph.facebook.com/v21.0/me/accounts',
    params={'access_token': TOKEN, 'fields': 'id,name,category,tasks,access_token'})

# Pages pertencentes ao Business Manager (mais completo — inclui as sem role direto)
requests.get(f'https://graph.facebook.com/v21.0/{BM_ID}/owned_pages',
    params={'access_token': TOKEN, 'fields': 'id,name'})

# Contas Instagram do BM (para placements IG)
requests.get(f'https://graph.facebook.com/v21.0/{BM_ID}/instagram_accounts',
    params={'access_token': TOKEN, 'fields': 'id,username'})
```

Nota: `GET act_<id>/promote_pages` frequentemente retorna `[]` mesmo com Pages v\u00e1lidas —
n\u00e3o use isso como fonte de verdade. Use `me/accounts` + `BM/owned_pages`.

### Validação de elegível para anúncio
A checagem confiável é tentar criar um `adcreative` descartável com aquela `page_id` e
apagar em seguida. Se voltar `id`, a Page anuncia. Se voltar erro (ex: `page not found` ou
`permissions error`), aquela Page não está autorizada na conta de anúncios.

---

## 4. Instagram Placements e PBIA (Page-Backed Instagram Account)

Quando a Página do Facebook não possui uma conta de Instagram vinculada (`instagram_business_account` vazio):
1. **Comportamento Padrão do Meta Ads (Advantage+ Placements):**
   - O Meta cria/utiliza automaticamente uma identidade virtual no Instagram espelhada na Página do Facebook (PBIA).
   - O anúncio é entregue normalmente em **Instagram Feed, Stories, Reels e Explorar**.
   - O usuário no Instagram vê o nome e a foto de perfil da Página do Facebook.
2. **Validação de Previews Cross-Platform via API:**
   Para garantir que todos os formatos do Instagram estão 100% elegíveis e renderizando:
   ```python
   formats = ['MOBILE_FEED_STANDARD', 'INSTAGRAM_STANDARD', 'INSTAGRAM_STORY', 'INSTAGRAM_REELS']
   for fmt in formats:
       res = requests.get(f'https://graph.facebook.com/v21.0/{ad_id}/previews',
                          params={'access_token': TOKEN, 'ad_format': fmt}).json()
       # Se 'data' existir com o iframe preview, o placement está aprovado
   ```
3. **Erro 283 (`pages_manage_metadata`):**
   Atualizações cadastrais da Página via API (`POST /{page_id}` alterando `about`, `website`, etc.) exigem o escopo `pages_manage_metadata`. Tokens emitidos apenas com `ads_management` e `pages_show_list` receberão erro 283. Se o escopo não estiver presente, oriente o usuário a editar pela UI web do Facebook ou gerar token com a permissão necessária.

---

## 5. Workflow de Troca de Identidade/Página em Anúncios Existentes

Quando o usuário cria ou altera a Página após os anúncios já terem sido criados:
1. Faça upload da imagem para a conta de anúncios para obter o `image_hash` atualizado.
2. Crie um novo `adcreative` com o novo `page_id`.
3. Atualize os anúncios existentes sem deletá-los:
   ```python
   requests.post(f'https://graph.facebook.com/v21.0/{ad_id}',
                 params={'access_token': TOKEN},
                 json={'creative': {'creative_id': new_creative_id}})
   ```
Isso atualiza a identidade instantaneamente, mantendo o histórico e os IDs dos anúncios.
```python
r = requests.post(f'https://graph.facebook.com/v21.0/{ACT}/adcreatives',
        params={'access_token': TOKEN},
        json={'name':'probe','object_story_spec':{'page_id':PAGE,'link_data':{
              'link':'https://example.com','message':'probe','name':'probe','image_hash':HASH}}}).json()
if 'id' in r: requests.delete(f'https://graph.facebook.com/v21.0/{r["id"]}', params={'access_token': TOKEN})
```

---

## 2. Limites do System User Token (o que N\u00c3O d\u00e1 para automatizar)

Tokens de System User / Business (mesmo com `access_token` de Page vindo de `me/accounts`)
**n\u00e3o** conseguem editar metadados de P\u00e1gina. Erros esperados:

| Opera\u00e7\u00e3o | Erro | Motivo |
|---|---|---|
| `POST /{page_id}` com `about`/`website`/`description` | `#283 Requires pages_manage_metadata` | Escopo ausente no token |
| `POST /{page_id}` com `name` | `#3 Application does not have the capability` | Rename de Page \u00e9 bloqueado por app comum (anti-fraude) |
| `POST /{page_id}/picture` | `#283 Requires pages_manage_metadata` | Escopo ausente |
| `GET /{page_id}/page_backed_instagram_accounts` | `#200 pages_read_engagement` | Escopo ausente |

**Conclus\u00e3o operacional:** renomear/rebrandar uma P\u00e1gina ou criar uma nova \u00e9 sempre
trabalho manual do usu\u00e1rio no navegador. N\u00e3o insista em tentativas de API — falhe r\u00e1pido,
explique o motivo em uma linha e entregue o passo a passo + os assets prontos.

---

## 3. O que entregar quando o usu\u00e1rio vai criar/ajustar a P\u00e1gina

O usu\u00e1rio n\u00e3o quer "instru\u00e7\u00f5es"; quer um kit pronto para copiar e colar. Entregue **sempre**:

1. **Foto de perfil 800\u00d71080** (quadrado) — logo em SVG centralizado sobre fundo escuro
   com glow radial na cor da marca. Renderize via Playwright, n\u00e3o gere \u00e0 m\u00e3o.
2. **Capa 1640\u00d7924** (propor\u00e7\u00e3o oficial FB desktop) — logo no topo-esquerda, headline com
   gradiente na palavra-chave, 3 feature-cards em glassmorphism, footer com dom\u00ednio + pre\u00e7o.
   Respeite `padding: 90px 100px` como safe-zone (a capa \u00e9 recortada em mobile).
3. **Tabela Markdown** com: Nome da P\u00e1gina, 3 Categorias sugeridas, Site, E-mail, Telefone, @username.
4. **Bio curta** (\u2264255 chars) e **Sobre longo** em blocos de c\u00f3digo (para copiar sem perder emoji/quebras).
5. **Aviso de vincula\u00e7\u00e3o ao BM** (ver se\u00e7\u00e3o 4).

Templates HTML de refer\u00eancia: `templates/fb_page_avatar.html` e `templates/fb_page_cover.html`.

### Verifica\u00e7\u00e3o dos renders sem depender de vis\u00e3o
Se `vision_analyze` estiver indispon\u00edvel, confirme que a logo/texto renderizou contando
pixels claros por amostragem — assets corretos ficam bem acima de ~800 px claros amostrados:

```python
from PIL import Image
im = Image.open(path).convert('RGB'); px = im.load(); bright = 0
for x in range(0, im.size[0], 4):
    for y in range(0, im.size[1], 4):
        r,g,b = px[x,y]
        if r>180 and g>180 and b>180: bright += 1
print(im.size, bright)
```
Se `bright` vier perto de 0, o SVG/fonte n\u00e3o carregou (caminho relativo errado no `file://`,
ou falta de `wait_for_timeout` antes do screenshot).

---

## 4. Vincula\u00e7\u00e3o obrigat\u00f3ria ao Business Manager

Uma Page nova s\u00f3 serve para a conta de an\u00fancios se estiver dentro do mesmo Portfolio/BM.
Oriente o usu\u00e1rio a criar direto em **Meta Business Suite \u2192 Configura\u00e7\u00f5es do Neg\u00f3cio \u2192
P\u00e1ginas \u2192 Adicionar \u2192 Criar nova P\u00e1gina** (nasce vinculada). Se criar pelo Facebook comum,
depois \u00e9 preciso **Adicionar P\u00e1gina existente** no BM.

---

## 5. Trocar a identidade de an\u00fancios j\u00e1 criados

N\u00c3O \u00e9 preciso recriar campanha/adset. Basta criar o novo `adcreative` com a `page_id`
correta e apontar os ads existentes para ele:

```python
# novo creative com a Page certa -> creative_id
requests.post(f'https://graph.facebook.com/v21.0/{AD_ID}',
    params={'access_token': TOKEN}, json={'creative': {'creative_id': NEW_CREATIVE_ID}})
```

Se o usu\u00e1rio apenas **renomear/trocar a foto** da mesma Page, nome e imagem nos an\u00fancios
atualizam automaticamente — nenhuma a\u00e7\u00e3o de API \u00e9 necess\u00e1ria.

Ads recém-criados/editados aparecem como `effective_status: IN_PROCESS` por alguns minutos;
isso é normal e não indica erro.
