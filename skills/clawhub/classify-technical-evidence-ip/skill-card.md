## Description:

Build, refine, govern, and apply evidence-based taxonomies to patents, scientific literature, product records, technical intelligence, customer requirements, and other structured text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and technical teams use this skill to create governed taxonomies, label structured technical records, manage review queues and taxonomy backlogs, and validate auditable labeling outputs with optional authorized PatSnap enrichment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source records, excerpts, identifiers, or derived queries may contain confidential, personal, export-controlled, licensed, or otherwise restricted information before optional external enrichment.

Mitigation: Confirm authorization before any external transmission, minimize each request to the needed evidence, prefer public publication numbers or normalized concepts when sufficient, and record the authorization status.

Risk: Taxonomy labels for sensitive domains could be misused as medical, marketing, legal, regulatory, or compliance determinations.

Mitigation: Treat labels as technical evidence review outputs and require qualified subject-matter, legal, or regulatory reviewers to approve downstream use.

Risk: Retrieved evidence or candidate labels could be mistaken for final classification decisions.

Mitigation: Keep business decisions, model judgments, external evidence, and deterministic validation separate; do not promote candidate labels or retrieval results to formal outputs without the configured confirmation gates.

Risk: Credentials or credential-bearing connection URLs could leak through workbooks, provenance tables, chat messages, or skill files.

Mitigation: Store API keys only in the MCP client's credential mechanism and exclude API keys, authorization headers, bearer tokens, and credential-bearing URLs from deliverables and provenance.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/classify-technical-evidence-ip)
- [Input and Output Contract](references/input-output-contract.md)
- [Workflow Modes](references/workflow-modes.md)
- [Default Decision Rules](references/default-decision-rules.md)
- [Taxonomy Design](references/taxonomy-design.md)
- [Quality and Review](references/quality-and-review.md)
- [PatSnap MCP Orchestration](references/zhihuiya-mcp-orchestration.md)
- [PatSnap Open Platform](https://open.patsnap.com/)
- [PatSnap MCP Marketplace](https://open.patsnap.com/marketplace/mcp-servers)
- [Advanced Patent Search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [Deep Patent Mining MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-mining)
- [Patent Briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [Scientific and Translational Evidence MCP](https://open.patsnap.com/marketplace/mcp-servers/scientific-translational-evidence)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured CSV/XLSX workbook outputs, YAML/CSV configuration, and validation command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include labeling results, evidence tables, review queues, taxonomy backlogs, QA summaries, and MCP provenance when authorized.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
