## Description:

Build an evidence-backed competitive patent landscape for a defined industry, technology, competitor set, geography, and time window. Use when executives, strategy teams, product leaders, competitive-intelligence analysts, or IP teams need to understand competitor technology bets, patent clusters, geographic filing behavior, cross-market differences, representative patents, potential white-space hypotheses, entry timing, and prioritized actions in an accessible HTML report; do not use this skill as an infringement or FTO opinion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Executives, strategy teams, product leaders, competitive-intelligence analysts, and IP teams use this skill to scope, retrieve, normalize, and report competitive patent-landscape evidence for business strategy decisions. It is designed for patent intelligence and opportunity validation, not infringement clearance or freedom-to-operate opinions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may require business scope, competitor lists, client-sensitive context, and PatSnap MCP connectivity.

Mitigation: Confirm that sharing this context with the connected tools is acceptable, and keep API keys out of prompts, reports, logs, and source control.

Risk: Patent-landscape conclusions can be misleading if live retrieval is unavailable, search results are capped, or entity resolution is incomplete.

Mitigation: Label unavailable retrieval as not executed, disclose result caps and counting units, record queries and filters, and keep uncertain applicants or aliases separate until verified.

Risk: Readers could mistake strategic patent intelligence for legal clearance.

Mitigation: Preserve the skill's boundary that it does not provide infringement clearance, freedom-to-operate opinions, or claims that a technical space is legally clear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/map-competitive-patent-landscape-ip)
- [Competitive patent landscape search strategy](artifact/references/SEARCH_STRATEGY.md)
- [Competitive patent landscape report template](artifact/references/REPORT_TEMPLATE.md)
- [PatSnap Advanced Patent Search MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Patent Briefing MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [HTML report with cited evidence tables, chart-ready data, methodology notes, and strategic interpretation text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a complete competitive patent-landscape report when PatSnap tools are available; produces a clearly labeled report shell and executable search strategy when live retrieval is unavailable.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
