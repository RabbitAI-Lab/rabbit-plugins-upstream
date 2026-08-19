## Description:

Build and validate expert patent-search branches for Stage 1/4 of a patent-landscape program. Use when starting create-patent-landscape-overview-ip or when a user needs a reusable, field-scoped, anchored, classification-assisted, de-noised patent search configuration with precision/recall validation, a traceable family-aware candidate pool, a lightweight core-recall set, and a preliminary taxonomy export for later human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, patent analysts, and intellectual-property teams use this skill to turn a confirmed patent-landscape scope into validated, reproducible search branches and traceable downstream handoff artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent-search scope, terms, identifiers, and related project details may be sent to the configured PatSnap MCP services.

Mitigation: Confirm the confidentiality boundary and approval to use the configured PatSnap MCP services before running searches.

## Reference(s):

- [Query and Preliminary Taxonomy Methodology](references/query-and-taxonomy-methodology.md)
- [Advanced Patent Search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [Patent Briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [Deep Patent Mining MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-mining)
- [Global Core Patent Database MCP](https://open.patsnap.com/marketplace/mcp-servers/core-patents)
- [PatSnap MCP Marketplace](https://open.patsnap.com/marketplace/mcp-servers)

## Skill Output:

**Output Type(s):** [Files, Text, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON, CSV, and plain-text artifact specifications]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces search_config.json, candidate_pool.csv, core_recall.csv, run_config.json, and preliminary tech_taxonomy.txt when the workflow completes.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
