## Description:

pps-tag helps patent-landscape teams design a tagging taxonomy, select representative patent packages, create a 20-30 record tagging demo, and export candidates for SaaS-based full tagging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts, innovation teams, and agent users use this skill after earlier patent panorama steps to turn candidate pools, taxonomy files, tagged pools, statistics, and value signals into a structured tagging proposal and handoff package.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent or project data may be sent to configured PatSnap MCP services or shared with a customer SaaS tagging tool.

Mitigation: Install and use the skill only when that data flow is intended and authorized; keep API keys in MCP or client configuration rather than project files.

Risk: Generated taxonomy, package, and export files can affect downstream customer tagging quality.

Mitigation: Review generated exports before sharing them with a customer SaaS tool and confirm that required upstream inputs are complete.

Risk: The skill is a structured patent-taxonomy workflow, not a complete legal review or deep representative-patent reading process.

Mitigation: Use qualified human review for legal conclusions and for high-impact patent package decisions.

## Reference(s):

- [Query and Taxonomy Methodology](references/query-and-taxonomy-methodology.md)
- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [PatSnap MCP Server Marketplace](https://open.zhihuiya.com/marketplace/mcp-servers)
- [PatSnap Developer Authentication Guide](https://open.zhihuiya.com/devportal/guides/authentication)
- [PatSnap Search MCP](https://open.zhihuiya.com/marketplace/mcp-servers/patsnap-search)
- [Patent Mining MCP](https://open.zhihuiya.com/marketplace/mcp-servers/patent-mining)
- [Patent Visual MCP](https://open.zhihuiya.com/marketplace/mcp-servers/patent-visual)
- [Landscape Projects MCP](https://open.zhihuiya.com/marketplace/mcp-servers/landscape-projects)

## Skill Output:

**Output Type(s):** [Files, JSON, CSV, Markdown, HTML, Guidance]

**Output Format:** [Structured files including JSON taxonomy and questions, CSV patent package and tagging exports, Markdown proposal, and optional HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires completed upstream candidate, taxonomy, tagged-pool, statistics, and value-signal inputs; full-sample tagging is handed off to a customer SaaS tool.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
