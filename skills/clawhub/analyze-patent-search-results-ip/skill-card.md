## Description:

Analyze validated patent-search artifacts at Stage 2/4 of a patent-landscape program. Use after search-patents-ip to produce population-bounded trends, organization and technology distributions, competitor profiles, a branch-organized reviewed core patent index, transparent candidate-level value proxies, chart-ready data, and a self-contained statistical snapshot for tag-patent-search-results-ip and create-patent-search-report-ip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, patent analysts, and IP teams use this skill after a validated patent search to produce reproducible Stage 2 patent-landscape statistics, core-record review indexes, value-proxy artifacts, chart data, and a statistical HTML snapshot for downstream tagging and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses PatSnap patent-data connectors and may access project patent-search artifacts.

Mitigation: Install it only in intended patent-landscape projects and review connector permissions before use.

Risk: Patent search inputs and generated analysis artifacts may contain confidential project information.

Mitigation: Confirm the project confidentiality boundary and store generated artifacts only in authorized locations.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yuanzhian-patsnap/skills/analyze-patent-search-results-ip)
- [PatSnap MCP marketplace](https://open.patsnap.com/marketplace/mcp-servers)
- [Advanced Patent Search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [Patent Briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [Deep Patent Mining MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-mining)
- [Global Core Patent Database MCP](https://open.patsnap.com/marketplace/mcp-servers/core-patents)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance, JSON, CSV, HTML]

**Output Format:** [Structured analysis artifacts plus concise Markdown handoff text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes bounded Stage 2 patent-landscape artifacts such as panorama_stats.json, patent_index.core.json, patent_index.core.csv, value_signals.json, chart_data.json, and panorama_stats_report.html.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
