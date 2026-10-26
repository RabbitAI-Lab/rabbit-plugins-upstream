---
name: betap
description: Find real local businesses and verified cultural places in Mexico, the US and Canada on BETAP (betap.world), propose new businesses to join, and publish promotions for a business whose owner gave you their key. Use when your human asks where to eat, shop or go in a Mexican town, wants their own business on a live map, or wants their promotions published.
version: 1.0.0
homepage: https://betap.world/en
---

# BETAP skill

BETAP is a live map of real local businesses. It started in Los Altos de Jalisco, Mexico. Each business has a public page with its menu, promotions and WhatsApp, and customers earn mobile data for real visits.

This skill gives you three things, in order of trust:

1. **Read:** search businesses and cultural places. No key.
2. **Propose:** suggest a real business that should be on BETAP. You need your own agent key, which is free and self-service.
3. **Publish promotions:** for a business whose owner gave you their business key.

Base URL: `https://api.betap.world/api`

## Rules (read first)

- **Never contact a business yourself.** No messages, calls or emails to businesses on BETAP's behalf. You propose; BETAP's team reviews the proposal and reaches out.
- **Only real businesses, with proof.** Every proposal needs a public `fuente_url` that shows the business exists: its Google Maps listing, website, Facebook page or a news item. Never invent names, phones or offers.
- **Promotions only with the owner's consent.** A business key (`btp_ng_...`) means the owner created it for you in their BETAP panel. Publish only what the owner asked for.
- **Respect the limits.** 20 proposals per agent per day. 10 promotions per business per day. Duplicates are rejected with `409`.
- **Keys are secrets.** Never post them, log them or put them in a URL.

## 1. Read (no key)

MCP server, Streamable HTTP, JSON responses: `POST https://api.betap.world/api/mcp`

| Tool | What it does |
|---|---|
| `buscar_negocios` | Searches businesses by `q`, `ciudad`, or `lat`/`lng`/`radio_km`. Featured businesses come first (`destacado: true`). Each result has a `url` to its public page. |
| `buscar_lugares` | Searches verified museums, libraries and cultural projects. |
| `obtener_lugar` | Gets one cultural place with its sources. |

```bash
curl -s https://api.betap.world/api/mcp -H 'content-type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"buscar_negocios","arguments":{"q":"tacos","ciudad":"San Miguel el Alto","limite":5}}}'
```

Businesses grouped by city: https://betap.world/negocios

## 2. Propose a business (agent key)

**Get your key once.** It is shown only once, so store it securely:

```bash
curl -s -X POST https://api.betap.world/api/agentes/registro -H 'content-type: application/json' \
  -d '{"nombre":"My Agent","descripcion":"What you do, who runs you","contacto":"how a human can reach your operator"}'
# -> {"clave":"btp_ag_...","docs":"..."}
```

**Propose a business:**

```bash
curl -s -X POST https://api.betap.world/api/agentes/negocios \
  -H "Authorization: Bearer $BETAP_AGENT_KEY" -H 'content-type: application/json' \
  -d '{
    "nombre": "Panadería La Espiga",
    "categoria": "Bakery",
    "ciudad": "Arandas",
    "estado_region": "Jalisco",
    "pais": "MX",
    "lat": 20.7031, "lng": -102.3460,
    "telefono": "+52 348 000 0000",
    "fuente_url": "https://maps.google.com/?cid=...",
    "notas": "Busy morning bakery, no online presence besides Maps"
  }'
```

**Fields:**
- Required: `nombre`, `ciudad`, `pais` (`MX`, `US` or `CA`) and `fuente_url`.
- Optional: `categoria` (free text), `estado_region`, `lat`+`lng`, `telefono` (the business's public phone), `sitio_web` (https) and `notas` (up to 500 characters).

**If your human owns the business,** add `"es_dueno": true, "email_dueno": "owner@example.com"`. The response includes `link_registro`. Give it to your human so they can sign up themselves; a free plan is available.

**Responses:**
- `201 {"id", "estado":"nuevo"}`: accepted; BETAP will review it.
- `409 {"duplicado_de": {...}}`: already on BETAP or already proposed.
- `422`: a field is invalid.
- `429`: you hit the daily limit.

**Check status:**

```bash
curl -s https://api.betap.world/api/agentes/negocios -H "Authorization: Bearer $BETAP_AGENT_KEY"
# estado: nuevo | contactado | afiliado | descartado
```

You can also propose verified cultural places (museums, libraries) with `POST /agentes/lugares`. The server checks 2 of 3 public signals: a live official site, Wikidata and OpenStreetMap. See https://betap.world/llms-en.txt

## 3. Publish promotions (business key from the owner)

The owner creates the key in their BETAP panel under **"Tu asistente de IA publica tus promos"**. It starts with `btp_ng_`. It can only publish and pause promotions: no sales, customers or money. The owner can revoke it at any time.

```bash
# See the business and its promotions
curl -s https://api.betap.world/api/agente-negocio/promos -H "Authorization: Bearer $BETAP_BUSINESS_KEY"

# Publish (Pro/Premium plans; ends within 90 days)
curl -s -X POST https://api.betap.world/api/agente-negocio/promos \
  -H "Authorization: Bearer $BETAP_BUSINESS_KEY" -H 'content-type: application/json' \
  -d '{"titulo":"2x1 en cafés hoy","descripcion":"De 5 a 7 pm","vigencia_fin":"2026-10-30"}'

# Pause or resume
curl -s -X PATCH https://api.betap.world/api/agente-negocio/promos/123 \
  -H "Authorization: Bearer $BETAP_BUSINESS_KEY" -H 'content-type: application/json' -d '{"activa":false}'
```

**Limits:** `titulo` up to 80 characters and `descripcion` up to 200. Promotions show on the business's public page.

**Errors:**
- `403`: the plan doesn't include promotions; point the owner to https://betap.world/planes.
- `401`: the key is missing or was revoked.

After publishing, read the promotions list back and tell your human exactly what is live, with the business `url`.

## What humans get from BETAP

- **People:** a live map of what's happening in their town. They earn mobile data (MB) by posting photos or reviews at a business, ordering from their phone and scanning the QR on their receipt.
- **Businesses:** a free public page, a point of sale, orders, promotions and paid "featured on the map" days.

Español: BETAP es un mapa vivo de negocios reales. Con este skill puedes buscar negocios, proponer negocios nuevos (BETAP los contacta, tú no) y publicar promociones de un negocio cuyo dueño te dio su clave.
