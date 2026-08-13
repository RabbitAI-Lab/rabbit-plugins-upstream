## Description:

pps-tag helps patent panorama teams design a tagging taxonomy, key technical questions, representative patent packages, demo tagging samples, and SaaS export files without performing full-pool tagging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts and customer-facing project teams use this skill after candidate collection, SaaS tagging, and panorama statistics are ready to produce a structured patent taxonomy proposal, representative patent packages, and handoff files for customer SaaS tagging workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may connect an agent to PatSnap MCP services and process patent project files.

Mitigation: Confirm the required MCP services and project inputs before use, and keep API keys managed through the client or MCP configuration.

Risk: Generated taxonomy proposals and export files can influence downstream customer SaaS tagging workflows.

Mitigation: Review generated files, especially taxonomy_proposal.md and to_be_tagged.csv, before sharing them or using them in a customer workflow.

Risk: The workflow depends on prior candidate, tagged, statistics, and value-signal inputs and does not perform full-pool tagging itself.

Mitigation: Verify required inputs are present before running the skill and hand full-sample tagging off to the customer SaaS process as documented.

## Reference(s):

- [Query and Taxonomy Methodology](references/query-and-taxonomy-methodology.md)
- [pps-tag ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/pps-tag)
- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [PatSnap MCP Server Marketplace](https://open.zhihuiya.com/marketplace/mcp-servers)
- [PatSnap Authentication Guide](https://open.zhihuiya.com/devportal/guides/authentication)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [JSON, CSV, Markdown, and optional HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces tech_breakdown.json, key_questions.json, patent_packages.csv, tagging_demo_sample.csv, to_be_tagged.csv, taxonomy_proposal.md, and optionally panorama_stats_report.html.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
