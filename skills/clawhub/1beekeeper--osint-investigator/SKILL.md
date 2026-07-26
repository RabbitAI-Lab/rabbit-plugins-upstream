---
name: osint-investigator
description: Open-source intelligence gathering with theHarvester, recon-ng, Maltego, and SpiderFoot. Domain recon, email harvesting, DNS mapping, and threat actor profiling from BlackArch tools on ARGUS.
homepage: https://github.com/nousresearch/argus
metadata:
  openclaw:
    requires:
      bins: ["curl", "jq", "theHarvester", "recon-ng", "maltego"]
      mcps: ["aynops", "cve-mcp"]
      optional_bins: ["spiderfoot", "amass", "subfinder", "whois"]
    os: ["linux"]
---

# OSINT Investigator

Open-source intelligence (OSINT) gathering and analysis pipeline using ARGUS BlackArch tools. Combines theHarvester for email/subdomain harvesting, recon-ng for web reconnaissance, Maltego for graphical link analysis, and SpiderFoot for automated data aggregation. Enriched with aynops for domain recon and CVE-MCP for threat intelligence context.

Runs on ARGUS infrastructure with 11 installed BlackArch recon/OSINT tools.

## Prerequisites

- **ARGUS host** with BlackArch tools installed
- **theHarvester** 4.11.1+ — email and subdomain harvesting
- **recon-ng** 5.1.2+ — web reconnaissance framework
- **Maltego** 4.11.3+ — graphical link analysis
- **aynops** MCP available on localhost — domain recon + scanning
- `curl`, `jq` on PATH

## Infrastructure

| Component | Location | Purpose |
|-----------|----------|---------|
| theHarvester | `/usr/bin/theHarvester` | Email, subdomain, and name harvesting |
| recon-ng | `/usr/bin/recon-ng` | Web reconnaissance framework |
| Maltego | `/usr/bin/maltego` | Graphical link analysis |
| SpiderFoot | `/usr/bin/spiderfoot` | Automated OSINT platform |
| aynops | localhost MCP | Domain recon: whois, DNS, ports, SSL |
| CVE-MCP | localhost MCP | CVE intelligence enrichment |

## Core Commands

### Quick Domain Recon (theHarvester)

Harvest emails, subdomains, IPs, and URLs for a target domain:

```bash
TARGET="example.com"
OUTDIR="/tmp/osint/$TARGET-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$OUTDIR"

echo "=== theHarvester: Full Harvest ==="
theHarvester -d "$TARGET" -b all -f "$OUTDIR/harvest.html" 2>&1 | \
  tee "$OUTDIR/harvest-output.txt"

# Extract emails
echo ""
echo "=== Extracted Emails ==="
grep -E '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' "$OUTDIR/harvest-output.txt" | \
  sort -u > "$OUTDIR/emails.txt"
cat "$OUTDIR/emails.txt"

# Extract subdomains
echo ""
echo "=== Extracted Subdomains ==="
grep -E '^[*]?[a-zA-Z0-9.-]+\.'"$TARGET" "$OUTDIR/harvest-output.txt" | \
  sort -u > "$OUTDIR/subdomains.txt"
cat "$OUTDIR/subdomains.txt"

# Extract IPs
echo ""
echo "=== Extracted IPs ==="
grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' "$OUTDIR/harvest-output.txt" | \
  sort -u > "$OUTDIR/ips.txt"
cat "$OUTDIR/ips.txt"
```

### theHarvester — Targeted Source Selection

Use specific data sources for focused harvesting:

```bash
TARGET="example.com"

# LinkedIn-focused (people, roles)
echo "=== LinkedIn Harvest ==="
theHarvester -d "$TARGET" -b linkedin 2>&1

# DNS brute-force
echo "=== DNS Brute-Force ==="
theHarvester -d "$TARGET" -b dnsdumpster,crtsh,certspotter 2>&1

# Search engines
echo "=== Search Engine Discovery ==="
theHarvester -d "$TARGET" -b google,bing,yahoo,duckduckgo 2>&1

# GitHub/code discovery
echo "=== Code Repository Discovery ==="
theHarvester -d "$TARGET" -b github-code 2>&1
```

Available sources: `anubis, baidu, bing, binaryedge, bingapi, bufferoverun, censys, certspotter, crtsh, dnsdumpster, duckduckgo, github-code, google, hackertarget, hunter, intelx, linkedin, linkedin_links, netcraft, omnisint, otx, pentesttools, projectdiscovery, rapiddns, rocketreach, securitytrails, shodan, sslcert, subdomaincenter, threatcrowd, threatminer, urlscan, virustotal, yahoo, zoomeye`

### recon-ng — Automated Reconnaissance

Initialize and run a recon-ng workspace:

```bash
TARGET="example.com"
WORKSPACE="osint-$(date +%Y%m%d)"

# Create workspace and run modules
recon-ng << RECONEOF
workspaces create $WORKSPACE
add domains $TARGET

# Discover contacts
modules load recon/contacts-contacts/mailtester
run

# Certificate transparency
modules load recon/domains-certificates/certspotter
run

# DNS enumeration
modules load recon/domains-hosts/bing_domain_web
run

modules load recon/domains-hosts/google_site_web
run

# Whois information
modules load recon/domains-contacts/whois_pocs
run

# Shodan integration
modules load recon/hosts-ports/shodan_ip
run

# Generate report
modules load reporting/list
set FILENAME /tmp/osint/${WORKSPACE}-contacts.txt
set TABLE contacts
run

modules load reporting/list
set FILENAME /tmp/osint/${WORKSPACE}-hosts.txt
set TABLE hosts
run

exit
RECONEOF

echo "Workspace: $WORKSPACE"
echo "Report: /tmp/osint/${WORKSPACE}-*.txt"
```

### DNS Reconnaissance via aynops

Use aynops MCP for comprehensive DNS mapping:

```bash
TARGET="example.com"

echo "=== AynOps DNS Recon: $TARGET ==="

# Whois
echo "--- Whois ---"
curl -s -X POST "http://localhost:8765/aynops/whois" \
  -H "Content-Type: application/json" \
  -d "{\"domain\": \"$TARGET\"}" | jq '{
    registrar: .registrar,
    created: .creation_date,
    expires: .expiration_date,
    nameservers: .name_servers[:5],
    org: .registrant_organization
  }'

# DNS Records
echo ""
echo "--- DNS Records ---"
curl -s -X POST "http://localhost:8765/aynops/dns" \
  -H "Content-Type: application/json" \
  -d "{\"domain\": \"$TARGET\", \"type\": \"all\"}" | jq '{
    a: .A[:5],
    mx: .MX[:3],
    ns: .NS[:5],
    txt: .TXT[:3],
    cname: .CNAME[:5],
    soa: .SOA
  }'

# SSL Certificate Info
echo ""
echo "--- SSL Certificate ---"
curl -s -X POST "http://localhost:8765/aynops/ssl" \
  -H "Content-Type: application/json" \
  -d "{\"domain\": \"$TARGET\"}" | jq '{
    issuer: .issuer,
    valid_from: .valid_from,
    valid_until: .valid_until,
    sans: .subject_alt_names[:10],
    fingerprint: .sha256_fingerprint[:16]
  }'
```

### SpiderFoot — Automated OSINT Scan

Run a comprehensive SpiderFoot scan (passive only by default):

```bash
TARGET="example.com"
SCAN_NAME="osint-$(date +%Y%m%d)"

echo "=== SpiderFoot: Passive Scan ==="
spiderfoot -s "$TARGET" -t "$SCAN_NAME" -m all 2>&1 | \
  tee "/tmp/osint/spiderfoot-$SCAN_NAME.txt"

echo ""
echo "=== SpiderFoot: High-Risk Findings ==="
grep -E "HIGH|CRITICAL|RISK" "/tmp/osint/spiderfoot-$SCAN_NAME.txt"
```

### Maltego — Graph Export

Export Maltego graph data for programmatic analysis:

```bash
TARGET="example.com"
GRAPH_DIR="/tmp/osint/maltego-$TARGET-$(date +%Y%m%d)"
mkdir -p "$GRAPH_DIR"

echo "=== Maltego Export Instructions ==="
echo ""
echo "1. Launch Maltego:  maltego"
echo "2. New Graph → select 'Company Stalker' or 'Domain Investigation' machine"
echo "3. Input: $TARGET"
echo "4. Run machine → wait for transforms to complete"
echo "5. Export: File → Export as CSV → $GRAPH_DIR/entities.csv"
echo "6. Export: File → Export as CSV (connections) → $GRAPH_DIR/links.csv"
echo ""
echo "After export, analyze:"

# Analysis after manual export
if [ -f "$GRAPH_DIR/entities.csv" ]; then
  echo ""
  echo "=== Entity Summary ==="
  echo "Total entities: $(wc -l < "$GRAPH_DIR/entities.csv")"
  
  echo ""
  echo "=== Top Entity Types ==="
  cut -d',' -f2 "$GRAPH_DIR/entities.csv" | sort | uniq -c | sort -rn | head -10
  
  echo ""
  echo "=== IP Addresses Discovered ==="
  grep -E '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' "$GRAPH_DIR/entities.csv" | sort -u
  
  echo ""
  echo "=== Email Addresses ==="
  grep -E '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+' "$GRAPH_DIR/entities.csv" | sort -u
  
  echo ""
  echo "=== Domains ==="
  grep -E '\.[a-z]{2,}$' "$GRAPH_DIR/entities.csv" | cut -d',' -f1 | sort -u | head -20
fi
```

### Combined OSINT Report

Generate a comprehensive OSINT report from all tools:

```bash
TARGET="example.com"
REPORT_DIR="$HOME/App/domains/argus/reports/osint"
REPORT="$REPORT_DIR/osint-report-$TARGET-$(date +%Y%m%d-%H%M%S).md"
TMPDIR="/tmp/osint/$TARGET-$(date +%Y%m%d)"
mkdir -p "$REPORT_DIR" "$TMPDIR"

echo "# OSINT Report: $TARGET" > "$REPORT"
echo "**Date:** $(date)" >> "$REPORT"
echo "" >> "$REPORT"

# 1. Domain Info (aynops)
echo "## 1. Domain Registration" >> "$REPORT"
curl -s -X POST "http://localhost:8765/aynops/whois" \
  -H "Content-Type: application/json" \
  -d "{\"domain\": \"$TARGET\"}" | jq -r '
    "| Field | Value |\n|---|---|\n" +
    "| Registrar | \(.registrar // "N/A") |\n" +
    "| Created | \(.creation_date // "N/A") |\n" +
    "| Expires | \(.expiration_date // "N/A") |\n" +
    "| Nameservers | \(.name_servers[:3] | join(", ") // "N/A") |"
  ' >> "$REPORT" 2>/dev/null

# 2. DNS Records (aynops)
echo "" >> "$REPORT"
echo "## 2. DNS Records" >> "$REPORT"
curl -s -X POST "http://localhost:8765/aynops/dns" \
  -H "Content-Type: application/json" \
  -d "{\"domain\": \"$TARGET\", \"type\": \"all\"}" | jq -r '
    "### A Records\n" + (.A[:10] | map("  - " + .) | join("\n") // "  None") +
    "\n\n### MX Records\n" + (.MX[:5] | map("  - " + .) | join("\n") // "  None") +
    "\n\n### NS Records\n" + (.NS[:5] | map("  - " + .) | join("\n") // "  None") +
    "\n\n### TXT Records\n" + (.TXT[:5] | map("  - " + (. | tostring)[:100]) | join("\n") // "  None")
  ' >> "$REPORT" 2>/dev/null

# 3. Subdomain Discovery (theHarvester)
echo "" >> "$REPORT"
echo "## 3. Subdomain Discovery" >> "$REPORT"
theHarvester -d "$TARGET" -b crtsh,certspotter,dnsdumpster -f "$TMPDIR/harvest.html" 2>&1 | \
  grep -E '^[*]?[a-zA-Z0-9.-]+\.'"$TARGET" | sort -u | while IFS= read -r sub; do
  echo "  - $sub" >> "$REPORT"
done

# 4. Email Exposure
echo "" >> "$REPORT"
echo "## 4. Email Discovery" >> "$REPORT"
theHarvester -d "$TARGET" -b hunter,intelx 2>&1 | \
  grep -E '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' | sort -u | while IFS= read -r email; do
  echo "  - \`$email\`" >> "$REPORT"
done

# 5. SSL Certificate (aynops)
echo "" >> "$REPORT"
echo "## 5. SSL Certificate" >> "$REPORT"
curl -s -X POST "http://localhost:8765/aynops/ssl" \
  -H "Content-Type: application/json" \
  -d "{\"domain\": \"$TARGET\"}" | jq -r '
    "| Field | Value |\n|---|---|\n" +
    "| Issuer | \(.issuer // "N/A") |\n" +
    "| Valid From | \(.valid_from // "N/A") |\n" +
    "| Valid Until | \(.valid_until // "N/A") |\n" +
    "| SANs | \(.subject_alt_names[:10] | join(", ") // "N/A") |"
  ' >> "$REPORT" 2>/dev/null

# 6. Threat Intel (CVE-MCP)
echo "" >> "$REPORT"
echo "## 6. Threat Intelligence" >> "$REPORT"
echo "Cross-reference discovered IPs with known threat indicators:" >> "$REPORT"

echo ""
echo "Report written: $REPORT"
```

### IP/Email Reputation Check

Check discovered IPs and emails against threat intel:

```bash
IP="8.8.8.8"

echo "=== Threat Intel: $IP ==="
curl -s -X POST "http://localhost:8765/aynops/reputation" \
  -H "Content-Type: application/json" \
  -d "{\"ip\": \"$IP\"}" | jq '{
    ip: .ip,
    abuse_score: .abuseipdb_score,
    reports: .total_reports,
    last_reported: .last_reported_at,
    country: .country,
    isp: .isp,
    usage_type: .usage_type
  }'
```

## Usage Patterns

### Domain Due Diligence

Before engaging with a new domain/company:

1. **Registration check** — whois, creation date, registrar (aynops)
2. **DNS mapping** — full DNS record enumeration (aynops + theHarvester)
3. **Subdomain discovery** — certificate transparency + brute force
4. **Email footprint** — discover exposed emails on target domain
5. **SSL analysis** — certificate validity, SANs, issuer trust
6. **Threat intel** — cross-reference IPs against abuse databases
7. **Report** — compile findings with risk assessment

### Threat Actor Profiling

When investigating a potential threat actor:

1. Start with known indicators (email, domain, IP)
2. theHarvester: pivot from email to domains, from domains to IPs
3. Maltego: build relationship graph — who connects to whom
4. SpiderFoot: deep web scan for additional indicators
5. recon-ng: search for the indicators across 50+ modules
6. CVE-MCP: check if actor targets known vulnerabilities
7. Document TTPs (Tactics, Techniques, Procedures)

### Attack Surface Discovery

For red team / security assessment:

1. Full subdomain enumeration (theHarvester + cert transparency)
2. Port scanning via aynops
3. Technology stack detection from headers/DNS
4. CVE-MCP cross-reference for discovered tech
5. Email pattern analysis for social engineering vectors
6. Code repository discovery (GitHub, GitLab, Bitbucket)

### Continuous Monitoring

Ongoing OSINT watch:

1. Weekly domain recon for new subdomains
2. Daily certificate transparency log monitoring
3. New email exposure alerts
4. IP reputation changes
5. New DNS records (especially MX/NS changes — could indicate compromise)

## Pricing Tiers

### Free (Basic)
- Single domain recon (theHarvester — 5 sources max)
- Basic whois lookup (aynops)
- Subdomain discovery (certificate transparency only)
- Email discovery (10 results)
- Text-only report
- 1 scan/day

### Pro ($5/credits, 1 credit = 1 full scan)
- Full domain recon (theHarvester — all sources)
- Complete DNS mapping (aynops)
- SpiderFoot automated scan (passive)
- recon-ng multi-module pipeline
- Email discovery (unlimited)
- IP reputation check (10 IPs/scan)
- Maltego graph export (CSV)
- PDF report with risk scoring
- 30-day data retention

### Enterprise (Custom pricing)
- Unlimited scans across unlimited domains
- Active SpiderFoot scans (with authorization)
- Maltego Transform Hub access
- Custom data source integrations
- Team dashboard + shared workspaces
- API access for CI/CD integration
- SLA: results within 2 hours
- Data retention: 1 year

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `AYNOPS_MCP_URL` | `http://localhost:8765/aynops` | AynOps MCP endpoint |
| `CVE_MCP_URL` | `http://localhost:8765/cve-mcp` | CVE-MCP endpoint |
| `THEHARVESTER_SOURCES` | `all` | Default sources for theHarvester |
| `OSINT_OUTPUT_DIR` | `/tmp/osint` | Temporary scan output |
| `REPORT_DIR` | `~/App/domains/argus/reports/osint` | Report storage |
| `SPIDERFOOT_PORT` | `5001` | SpiderFoot web UI port |
| `RECON_NG_DB` | `~/.recon-ng/workspaces` | recon-ng workspace database |
| `MAX_SUBDOMAINS` | `500` | Limit subdomain results to avoid noise |
| `SCAN_TIMEOUT` | `600` | Max seconds per scan phase |

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| theHarvester returns empty | Source API rate-limited | Spread scans over time, use fewer sources |
| recon-ng module fails | API key not configured | `keys add <module>_api <key>` in recon-ng |
| SpiderFoot hangs | Too many modules selected | Use `-m sfp_dns,sfp_crt,sfp_email` to limit |
| Maltego not found | Not in PATH | `/usr/bin/maltego` or install via BlackArch |
| aynops timeout | Target DNS slow | Increase timeout, try alternative resolver |
| Emails not extracted | Domain uses email obfuscation | Try `hunter` source specifically, check LinkedIn |
| jq parse error | API returned null/error | Check service health first, handle null in jq |

## Security

- **Authorization required** — only run OSINT on domains you own or have explicit permission
- **Passive by default** — no active scanning without authorization
- **Rate limiting** — respect source API rate limits to avoid blocks
- **Data handling** — discovered emails/PII should be treated as sensitive
- **Attribution caution** — OSINT data can be outdated or planted; cross-reference 3+ sources
- **ARGUS isolation** — all scans run on dedicated ARGUS host

## BlackArch OSINT Tools

Installed and available on ARGUS:

| Tool | Version | Use |
|------|---------|-----|
| theHarvester | 4.11.1 | Email, subdomain, and employee harvesting |
| recon-ng | 5.1.2 | Full-featured web reconnaissance framework |
| maltego | 4.11.3 | Graphical link analysis and data visualization |
| spiderfoot | 4.0 | Automated OSINT aggregation (100+ modules) |
| brainstorm | 1.0 | AI-driven discovery engine |
| ffuf | 2.1.0 | Fast web fuzzer for endpoint discovery |

Additional BlackArch tools that can be installed:

```bash
cd ~/App/domains/argus/tools
./manage-blackarch.sh install amass      # OWASP subdomain enumeration
./manage-blackarch.sh install subfinder  # Fast passive subdomain discovery
./manage-blackarch.sh install nuclei     # Template-based vulnerability scanning
```

## AynOps Integration

AynOps MCP provides domain reconnaissance:

- **Whois** — full domain registration data
- **DNS** — all record types (A, AAAA, MX, NS, TXT, CNAME, SOA, SRV)
- **SSL** — certificate chain, validity, SAN enumeration
- **Port Scan** — TCP/UDP service discovery
- **HTTP Headers** — technology stack fingerprinting
- **Reputation** — IP/domain abuse database lookup

## Related Skills

- **vulnerability-scanner** — active vulnerability scanning of discovered assets
- **cve-tracker** — CVE monitoring for discovered technology stacks
- **incident-responder** — actionable response when OSINT reveals threats
- **gdpr-security-auditor** — GDPR impact of exposed data discovered via OSINT
