## Description:

Prism Auto Config Map helps automotive product, strategy, R&D, supply-chain, and sales teams create patent- and literature-supported HTML decision reports for next-generation vehicle configuration planning and competitor benchmarking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Automotive product planners, competitive intelligence teams, R&D researchers, procurement and supply-chain teams, and sales/demo teams use this skill to scope a vehicle segment or configuration set, connect market configuration signals to PatSnap patent/literature and supply-chain evidence, and generate an offline HTML planning report. It is not intended for FTO legal opinions, exact BOM costing, broad financing analysis, or company strategy profiles unrelated to vehicle configuration decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on PatSnap MCP services and user account authorization, so database-backed conclusions may be incomplete if those services are unavailable or unauthenticated.

Mitigation: Configure the required PatSnap MCP services before use and disclose unavailable sources or data gaps in generated reports.

Risk: Automotive forecasts can be misleading when source data is stale or when recent patent activity is hidden by publication lag.

Mitigation: Review generated reports for data cutoff dates, source limitations, patent-publication lag, confidence labels, and forward-looking caveats before relying on recommendations.

Risk: The workflow is not intended to produce FTO legal opinions or exact BOM cost estimates.

Mitigation: Keep use scoped to configuration planning and patent-supported research, and route FTO, legal, and exact costing questions to qualified specialists and authoritative tools.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/prism-auto-config-map)
- [Publisher profile](https://clawhub.ai/user/yuanzhian-patsnap)
- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [PatSnap MCP server marketplace](https://open.zhihuiya.com/marketplace/mcp-servers)
- [Data Sources](references/data_sources.md)
- [Methodology](references/methodology.md)
- [PatSnap Data Lens](references/patsnap_data_lens.md)
- [Supply Chain Lens](references/supply_chain_lens.md)
- [Output Templates](references/output_templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance and local static HTML report files with bundled assets when the host agent executes the workflow]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should disclose data cutoffs, source limitations, patent-publication lag, confidence, and data gaps.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
