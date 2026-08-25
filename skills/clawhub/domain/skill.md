---
name: domainkits
description: Check domain availability. Search domains by keyword across the full lifecycle, from newly registered to expired and deleted. Analyze keyword value and trends. Turn AI into your domain agent. domainkits.com
homepage: https://domainkits.com/mcp
metadata: {"openclaw":{"emoji":"🌐","primaryEnv":"DOMAINKITS_API_KEY"}}

---

## Why DomainKits?

With DomainKits MCP your AI can:
- **Data-driven actions** -- See what's registering now, what's expiring tomorrow, what just dropped
- **Make informed decisions** -- Analyze keyword value, brand risk, and safety in seconds
- **Execute instantly** -- From idea to available domain with pricing in seconds

## Setup

### Claude Code
```bash
claude mcp add domainkits https://api.domainkits.com/v1/mcp
```

With API key (for higher limits):
```bash
claude mcp add domainkits https://api.domainkits.com/v1/mcp --header "X-API-Key: YOUR_KEY"
```

### Claude.ai
Connect DomainKits via **Settings > Connectors**. No manual configuration needed.

### Cursor / Other MCP Clients
Add to your MCP config:
```json
{
  "mcpServers": {
    "domainkits": {
      "url": "https://api.domainkits.com/v1/mcp"
    }
  }
}
```

With API key:
```json
{
  "mcpServers": {
    "domainkits": {
      "url": "https://api.domainkits.com/v1/mcp",
      "headers": {
        "X-API-Key": "YOUR_KEY"
      }
    }
  }
}
```

## Tools

### Search
- `nrds` -- Newly registered domains, by keyword or browse a gTLD
- `nrds_live` -- Live feed of domains registered in the last three days
- `aged` -- Domains with 5-20+ years history
- `expired` -- Domains entering deletion cycle, by keyword or browse a gTLD
- `deleted` -- Just-dropped domains, available now
- `active` -- Live registered domains (~240M gTLD database)
- `market` -- Domains with marketplace listing data, by keyword or browse a gTLD
- `ns_reverse` -- Domains on a specific nameserver
- `unregistered_ai` -- Unregistered short .ai domains (3-letter, pattern-based)
- `domain_changes` -- Domain change detection across 4M+ monitored domains
- `typosquat` -- Generate typosquat permutations and check which variants are registered

### Lookup
- `available` -- Single-domain availability with pricing
- `dns` -- DNS records (A, AAAA, MX, NS, TXT, SOA)
- `whois` -- WHOIS/RDAP registration data
- `safety` -- Google Safe Browsing status (requires account)
- `tld_check` -- Keyword availability across TLDs
- `keyword_data` -- Google Ads keyword data (requires account)
- `price` -- Registration and renewal prices by TLD
- `market_price` -- Secondary market listing prices
- `backlink_summary` -- SEO backlink profile (requires account)

### Trends
- `keywords_trends` -- Hot, emerging, and prefix keywords in domain registrations
- `tld_trends` -- Historical registration trends by TLD
- `tld_rank` -- TLD rankings by registration volume

### Bulk
- `bulk_tld` -- Keyword popularity across TLDs
- `bulk_available` -- Batch availability check (up to 50 domains)

### Stateful (require memory)
- `preferences` -- Manage memory and saved preferences (action: get/set/delete)
- `monitor` -- Domain monitoring with WHOIS/DNS/page change checks (action: get/set/update/delete)
- `strategy` -- Store user-authored strategy text, run timestamps and the most recent result (action: get/set/update/delete)
- `usage` -- Current tier, per-group usage, and remaining quota

## Skills

DomainKits MCP serves raw data. For domain industry workflows (naming consultation, competitive analysis, keyword intelligence, expired domain due diligence, and more), see [DomainKits Skills](https://github.com/ABTdomain/domainkits-skills), an open-source collection of workflow prompts that any AI assistant can use on top of this data.

## Instructions

When user wants domain suggestions:
1. Brainstorm names based on keywords
2. Call `bulk_available` to validate
3. Show available options with prices

When user wants to analyze a domain:
1. Call `whois`, `dns`, `safety`
2. Give a clear verdict

Output rules:
- Default to `no_hyphen=true` and `no_number=true`
- Use `usage` to check remaining quota before heavy operations

## Access

Works without an API key on a guest quota. A free account raises it; paid tiers raise it further and unlock the full filter set, deeper paging, and the account-bound tools (`safety`, `keyword_data`, `backlink_summary`, monitors, strategies). Current per-tier limits are listed at [domainkits.com/pricing](https://domainkits.com/pricing); the `usage` tool reports the live quota for the current account. Register free at [domainkits.com](https://domainkits.com/register).

## Privacy

- Works without API key (guest access)
- Memory OFF by default, requires explicit consent
- All stored data encrypted at rest (AES-256-GCM)
- GDPR compliant, delete data anytime via `preferences` with action: delete

## Links

- Website: https://domainkits.com/mcp
- Skills: https://github.com/ABTdomain/domainkits-skills
- GitHub: https://github.com/ABTdomain/domainkits-mcp
- Contact: info@domainkits.com
