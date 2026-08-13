## Description:

Generates automotive configuration planning reports that combine QFD, Matrix Analysis, benchmarking, Patsnap patent and literature signals, and supply-chain evidence to support next-generation vehicle feature decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Product planners, competitive intelligence teams, R&D pre-research teams, supply-chain teams, and presales stakeholders use this skill to turn vehicle segment, model, or feature questions into evidence-backed HTML decision reports for configuration planning. It is scoped away from FTO legal opinions, precise BOM cost analysis, broad financial analysis, and company strategy profiles unrelated to vehicle configuration decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Patsnap MCP services and user-authorized account access.

Mitigation: Confirm the Patsnap MCP connection and account authorization before use, and use only data sources the user is licensed or configured to access.

Risk: Generated automotive recommendations can be misleading if source data is stale, incomplete, or missing supplier and patent support.

Mitigation: Review generated reports for data cutoffs, stale-data caveats, data gaps, and unsupported supplier or patent conclusions before relying on recommendations.

Risk: The skill explicitly excludes FTO legal opinions, precise BOM cost analysis, broad financial analysis, and unrelated company strategy profiling.

Mitigation: Keep use scoped to vehicle configuration planning and route legal, cost, financial, or broad strategy questions to qualified workflows or experts.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/yuanzhian-patsnap/skills/prism-auto-config-map)
- [PatSnap Open Platform MCP Marketplace](https://open.zhihuiya.com/marketplace/mcp-servers)
- [PatSnap developer documentation](https://open.patsnap.com/devportal)
- [Methodology reference](references/methodology.md)
- [Data sources and reliability reference](references/data_sources.md)
- [Patsnap data lens reference](references/patsnap_data_lens.md)
- [Supply chain lens reference](references/supply_chain_lens.md)
- [Output templates reference](references/output_templates.md)
- [Configuration taxonomy reference](references/config_taxonomy.md)
- [Demo prompts and QA reference](references/demo_prompts.md)

## Skill Output:

**Output Type(s):** [analysis, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance and static HTML report files with local assets when report generation is requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce index.html, patent_pools/*.html, local assets, and zip packages; generated reports must disclose data cutoffs, source limits, and evidence gaps.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
