# Auditoria de Procedência de Ativos ("de onde saiu esse anúncio?")

Quando o usuário pergunta **"de onde saiu esse X? isso é campanha?"** sobre um nome/URL que ele
viu num relatório, a resposta só vale se for baseada em varredura da Graph API. Nunca deduza
procedência ("provavelmente é um post legado do Instagram", "deve ser criativo antigo") — isso
já foi feito uma vez, foi aceito como fato, e estava **errado**.

---

## 1. Regra de ouro: procedência exige evidência de duas frentes

| Frente | O que responde | Como |
|---|---|---|
| **Graph API** | O ativo existe na conta de anúncios? | Varredura de todas as edges em **todas** as contas do token |
| **Origem do relatório** | Como o nome apareceu no relatório? | Grep nos outputs/prompts do cron que gerou o relatório |

Só depois das duas é que se afirma "não é campanha". Uma frente sozinha produz conclusão
inventada.

---

## 2. Varredura Graph API — todas as contas, todas as edges

Nunca audite apenas a conta principal. O token costuma ter acesso a mais de uma conta e o
ativo pode estar em qualquer uma.

```python
# 1) Descobrir TODAS as contas do token (não presuma act_<principal>)
requests.get('https://graph.facebook.com/v21.0/me/adaccounts',
    params={'fields': 'id,name', 'limit': 50, 'access_token': TOKEN})
```

Edges obrigatórias por conta (o ativo pode existir só como criativo órfão ou só como imagem):

| Edge | Fields úteis |
|---|---|
| `campaigns` | `id,name,status,effective_status,created_time` |
| `adsets` | `id,name,status,effective_status,created_time` |
| `ads` | `id,name,status,effective_status,created_time` |
| `adcreatives` | `id,name,object_story_spec,asset_feed_spec,object_type,effective_object_story_id,link_url` |
| `adimages` | `hash,name,created_time` |
| `advideos` | `id,title,description` |

Método de busca: serializar cada objeto com `json.dumps(x, ensure_ascii=False)` e aplicar
`re.search(termo, s, re.I)`. Buscar dentro do JSON serializado (e não campo por campo) pega
menções escondidas em `object_story_spec`, `asset_feed_spec` e captions.

Complemento decisivo: extrair **todas as URLs dos criativos** e agrupar por host. Se a URL
suspeita não aparece nesse conjunto, ela não é destino de nenhum anúncio — prova negativa forte.

```python
urls = {}
for x in creatives:
    for u in re.findall(r'https?://[^"\\ ]+', json.dumps(x, ensure_ascii=False)):
        urls[u.split('?')[0]] = urls.get(u.split('?')[0], 0) + 1
# filtrar ruído de CDN: descartar hosts scontent.* / fbcdn
```

Script pronto: `scripts/meta_asset_provenance_sweep.py`.

---

## 3. Falso positivo clássico: URL de conversa do CRM virando "Landing Page"

Causa raiz encontrada em 2026-08: o cron de auditoria (Meta Ads **&** GHL) lê conversas sem
resposta no GoHighLevel. Mensagens de **broadcast de terceiros** (comunidades, grupos, listas
de transmissão que o usuário assina) contêm links promocionais. O relatório extraiu essas URLs
e as listou na tabela *"Auditoria de Disponibilidade das Landing Pages"* junto com as URLs reais
dos criativos — criando um ativo fantasma que parecia campanha ativa.

**Diagnóstico:** procure o nome/URL nos outputs do cron antes de olhar a conta de anúncios.

```bash
grep -i -n -E "<termo>" /root/.hermes/cron/output/*.txt
grep -rhoi -E ".{0,300}<dominio-suspeito>" /root/.hermes/sessions/*.json | sort -u | head
```

Nos dumps de sessão o conteúdo vem com escape múltiplo (`\\\\u00e7`). Para ler, desserialize
em loop:

```python
s = open(path).read()
for _ in range(6):
    try:
        s2 = json.loads(s) if s.strip().startswith(('{', '[', '"')) else s
        s = s2 if isinstance(s2, str) else json.dumps(s2, ensure_ascii=False)
    except Exception:
        break
```

**Prevenção:** relatórios de auditoria de Landing Page devem varrer **apenas** URLs extraídas
de `adcreatives` da conta de anúncios. URLs vindas de conversas do CRM, quando relevantes,
ficam em seção separada e rotulada como *"links recebidos de terceiros (não são destinos de
anúncio)"*.

---

## 4. Formato da resposta ao usuário

O usuário quer o veredito primeiro e a prova depois:

1. **Uma linha de veredito** — "Não é campanha." / "É campanha ativa, ID X."
2. **De onde veio** — o caminho real de entrada do nome (CRM, relatório, criativo legado), com
   citação literal da mensagem/linha que provou isso.
3. **Tabela de verificação** — entidades varridas × ocorrências encontradas (inclusive os zeros).
4. **Inventário real** — lista das campanhas de fato existentes com status.
5. **Conclusão de risco financeiro** — "zero risco de gasto" só com adset/orçamento verificados.
6. **Uma pergunta de ação** no fim, se houver correção óbvia a aplicar.

Se uma conclusão anterior (sua ou do resumo de contexto) estava errada, **diga isso de forma
explícita e direta** logo no começo ("a explicação anterior está errada") e siga. Sem rodeios,
sem desculpas longas.
