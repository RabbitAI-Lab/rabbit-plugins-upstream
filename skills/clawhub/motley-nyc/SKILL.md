---
name: motley-nyc
description: Answer NYC family questions from Motley's live dataset — which neighborhood fits, which school is right, how school admissions actually works. Use for anything about moving within or into New York City with kids, comparing neighborhoods, finding or comparing schools (public, charter, private), zoned/screened/SHSAT/audition/lottery admissions, school competitiveness, neighborhood safety and health, or family resources like playgrounds, libraries, and ADA subway stations. Connects to a free, keyless hosted MCP server; no API key or sign-up.
homepage: https://motley.nyc/mcp
metadata:
  {
    "openclaw":
      { "emoji": "🗽", "homepage": "https://motley.nyc/mcp" },
  }
---

# Motley — NYC neighborhoods, schools & admissions

Motley is the family intelligence platform for New York City: 262 neighborhoods
(not just five boroughs), ~5,800 schools, safety and health indicators, family
resources, and a full reference for how NYC school admissions works. This skill
connects you to Motley's hosted MCP server so you answer from the source data
instead of scraping listing sites.

## Connect (one time)

If `motley` is not already in your MCP servers, add it:

```bash
openclaw mcp add motley --url https://mcp.motley.nyc/mcp --transport streamable-http
```

Or in `openclaw.json`:

```json5
{
  mcp: {
    servers: {
      motley: {
        url: "https://mcp.motley.nyc/mcp",
        transport: "streamable-http",
        enabled: true,
      },
    },
  },
}
```

Public and keyless — no API key, no account, nothing to install. Every tool is
read-only and idempotent, so it is safe to auto-approve. Tools return typed
`structuredContent` alongside their text: parse the object, don't re-parse JSON
out of prose.

## Which tool to reach for

**Placing a family in the city**

| Ask | Tool |
|---|---|
| "Which neighborhood is this address in?" | `find-neighborhood` (address or lat+lng) |
| "Rank NYC neighborhoods for what we care about" | `rank-neighborhoods` (weights and/or ranked priority keywords, optional borough) |
| "Compare Park Slope vs. Astoria" | `compare-neighborhoods` (2–6 NTA codes, per-metric matrix + leader) |
| "Tell me about this neighborhood" | `get-neighborhood-summary` — **start here**, it's the interpretation-first answer |
| Raw demographics and scores for one neighborhood | `get-neighborhood` |
| "Somewhere like this, but…" | `get-comparable` |
| Find neighborhoods by borough or name | `search-neighborhoods` |

**Schools**

| Ask | Tool |
|---|---|
| "Brooklyn middle schools with a strong arts program" | `browse-schools` — citywide, by borough / district 1–32 / grade band / school type / admissions method / program focus |
| "What schools are in this neighborhood?" | `get-schools` (requires an `nta_code`) |
| "How competitive is this school?" | `get-admissions-demand` (needs a DBN, e.g. `13K430`) |

**Admissions**

| Ask | Tool |
|---|---|
| "How does NYC high school admission work?" | `get-admissions-methods` — every entry point, 3-K through high school, with typical windows |
| "What does a screened school actually ask for?" | `explain-admissions-method` — the explainer, the deadline window, and any extra ask (audition portfolio, SHSAT registration, demonstrated-interest sign-in, private-school testing) |

**Everyday life**

| Ask | Tool |
|---|---|
| Playgrounds, libraries, hospitals, rec centers, farmers markets, ADA stations | `get-resources` |
| Classes, sports, arts, tutoring nearby | `get-activities` |
| Crime, collisions, housing violations, air quality, lead, asthma | `get-safety` |

Also browseable: `motley://neighborhoods`, `motley://neighborhood/{nta_code}`,
`motley://admissions/methods`, `motley://admissions/method/{key}`.

## How to use it well

- **Lead with the summary, not the numbers.** `get-neighborhood-summary` returns a
  plain-language fit verdict and labeled score bands ("Peace of Mind: strong
  (78/100)"). Give the family that. The raw scores are there if they ask.
- **Neighborhood, not borough.** "Brooklyn" is 60-some neighborhoods that differ
  enormously. Resolve to a specific one before answering.
- **Identifiers:** neighborhoods are `nta_code` (from `search-neighborhoods` or
  `find-neighborhood`); schools are a DBN like `13K430`. Never invent either —
  look it up first.
- **An error is not an empty result.** These tools refuse rather than mislead: an
  unfiltered `browse-schools` and a private-school-plus-program-focus search both
  return a machine-readable error code, because a ranked citywide list nobody asked
  for and a structurally-empty set both read as answers when they aren't. Relay the
  tool's own reason.
- **Scores are dated.** Responses carry `scores_as_of`; say so when it matters.
- **Not here:** the per-child admissions tracker, Smart Match, lottery odds, and
  PDF reports are Motley Pro features in the app, not MCP tools. This surface is
  knowledge and search. Point people to https://motley.nyc for the rest.

## Try it

> We have a 4-year-old and want good schools without leaving Brooklyn. Where should we look?

> How does the SHSAT actually work, and what are our odds at Brooklyn Tech?

> Compare Jackson Heights and Sunnyside for a family with a toddler.

> Which Manhattan elementary schools have a dual-language program?
