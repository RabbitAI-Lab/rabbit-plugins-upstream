---
name: ClawSearch Ultra
slug: clawsearch-ultra
version: 1.0.0
description: "Federeret websøgning over 10+ søgemaskiner (DuckDuckGo, Brave, Tavily, Exa, Serper, SearXNG, Perplexity m.fl.) med forklarlig routing, udtræk, crawl og research-pakker. PLUS unik feature: dansk/flersproget søgning + nyheds-overvågning med ændrings-advarsler."
metadata: {"clawdbot":{"emoji":"🔎","requires":{"bins":["node","curl"]}}}
---

# ClawSearch Ultra

Federeret søge-skill og lokal hentnings-runtime for agenter — bygget på Web Search Pro's
kerne, **forbedret med unikke features**:

## 🆕 Unikke features (findes ikke i originalen)

### Feature 1: Dansk + flersproget søgning
Søg med automatisk sprog-detektion og resultater på dansk, arabisk, somali, engelsk m.fl.
Brug `--lang da` for dansk-filtrerede resultater:

```bash
node scripts/search.mjs "renten 2026 danmark" --lang da --json
node scripts/search.mjs "aqoonsi" --lang so --json   # somali
```

### Feature 2: Nyheds-overvågning med advarsler
Overvåg et emne og få besked når der kommer NYT indhold (diff mod sidste søgning):

```bash
node scripts/watch.mjs "BTC pris" --interval 1h --notify telegram
node scripts/watch.mjs "Vantage spreads" --notify slack
```

### Feature 3: Svar-med-kilder (answer-first)
Få et kort svar + verificerede kilder i ét kald (samme som Perplexity, men gratis baseline):

```bash
node scripts/answer.mjs "Hvad er DRT-strategien?" --json
```

---

## Basis-søgning (arvet)

Ingen API-nøgle krævet for baseline:

```bash
node scripts/search.mjs "OpenClaw docs" --json
node scripts/search.mjs "seneste nyheder" --type news --json
```

## Premium-udbydere (valgfrit)

```bash
export TAVILY_API_KEY=tvly-xxxxx      # bedste baseline-opgradering
export EXA_API_KEY=exa-xxxxx
export BRAVE_API_KEY=xxxxx
export SERPER_API_KEY=xxxxx
export PERPLEXITY_API_KEY=xxxxx
export SEARXNG_INSTANCE_URL=https://searx.example.com
```

## Runtime-kontrakt

- `selectedProvider` — primær rute
- `routingSummary` — kompakt rute-forklaring med konfidens
- `federated.providersUsed` — udbydere der faktisk svarede
- `federated.value` — gevinst ved fanout (ekstra resultater, duplikat-besparelser)
- `cached` / `cache` — cache-hit og TTL

## Fuld dokumentation
- Kilde: https://github.com/Zjianru/web-search-pro (baseret på v2.1, forbedret)
- Nyheds-overvågning: `node scripts/watch.mjs --help`

## Feedback
- Hjælpsom? → `clawhub star clawsearch-ultra`
