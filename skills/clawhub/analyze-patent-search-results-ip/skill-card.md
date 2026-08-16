## Description:

Converts validated Stage 1 patent-search artifacts into reproducible statistics, organization and technology views, branch-organized core patent indexes, transparent value proxies, chart-ready data, and a self-contained statistical snapshot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts, IP teams, and agent operators use this skill after a validated patent-search stage to produce Stage 2 statistical artifacts, reviewed core-record indexes, value-signal proxies, chart data, and a snapshot for downstream tagging and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect or mismatched Stage 1 artifacts could produce misleading Stage 2 statistics and indexes.

Mitigation: Confirm search_config.json, candidate_pool.csv, and core_recall.csv are from the intended scope and query version before execution, and stop if they cannot be reconciled.

Risk: Patent counts, rankings, status signals, and composite proxies may be mistaken for legal opinions, official statistics, or patent valuation.

Mitigation: Preserve population, unit, family method, cutoff, completeness, sample state, proxy definitions, and limitations in every output, and keep legal, valuation, and transaction conclusions out of scope.

Risk: Patent-search inputs and local output files may contain confidential project material.

Mitigation: Confirm the authorized data-handling boundary and acceptability of PatSnap connector use and local artifact writes before running the workflow.

## Reference(s):

- [PatSnap Skill Hub](https://open.patsnap.com/marketplace/skill-hub)
- [PatSnap MCP Servers](https://open.patsnap.com/marketplace/mcp-servers)
- [Advanced Patent Search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [Patent Briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [Deep Patent Mining MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-mining)
- [Global Core Patent Database MCP](https://open.patsnap.com/marketplace/mcp-servers/core-patents)

## Skill Output:

**Output Type(s):** [text, markdown, json, csv, html, guidance]

**Output Format:** [JSON, CSV, HTML, and concise Markdown/text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local Stage 2 artifacts including panorama_stats.json, patent_index.core.json/csv, value_signals.json, chart_data.json, and panorama_stats_report.html with source, operation, request, query version, cutoff, limitations, and proxy states preserved.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
