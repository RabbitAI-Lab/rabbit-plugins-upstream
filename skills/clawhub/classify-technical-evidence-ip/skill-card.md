## Description:

Builds and applies auditable technical taxonomies for patents, scientific literature, product records, technical intelligence, customer requirements, and other structured text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and technical-intelligence teams use this skill to design governed taxonomies, label CSV/XLSX or text records, and produce reviewable evidence, QA, and provenance outputs for patents, literature, product records, and related technical evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow reads user-supplied CSV/XLSX/text records that may contain confidential, personal, licensed, privileged, or export-controlled material.

Mitigation: Classify data sensitivity, preserve source records locally, and obtain data-owner authorization before any external enrichment.

Risk: Optional PatSnap MCP enrichment may transmit source identifiers, excerpts, or derived queries outside the local workspace.

Mitigation: Use the skill's external-data authorization gate, minimize each query to the evidence needed, prefer public publication numbers or normalized concepts, and record authorization status.

Risk: Credentials or credential-bearing URLs could be exposed if copied into workbooks, provenance tables, chat, or skill files.

Mitigation: Use the MCP client's credential storage and do not store API keys, bearer tokens, authorization headers, or raw credential-bearing URLs in outputs.

Risk: Weak evidence or ambiguous taxonomy boundaries can produce misleading labels.

Mitigation: Keep candidate and formal labels separate, route low-confidence or conflicting cases to review, maintain a taxonomy backlog for coverage gaps, and validate outputs with the bundled helper scripts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/classify-technical-evidence-ip)
- [Input and Output Contract](artifact/references/input-output-contract.md)
- [Workflow Modes](artifact/references/workflow-modes.md)
- [Quality and Review](artifact/references/quality-and-review.md)
- [PatSnap MCP Orchestration](artifact/references/zhihuiya-mcp-orchestration.md)
- [PatSnap Open Platform](https://open.patsnap.com/)
- [PatSnap MCP marketplace](https://open.patsnap.com/marketplace/mcp-servers)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance, JSON or YAML task configuration, CSV/XLSX labeling outputs, validation reports, and shell commands for local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source records and separates formal labels, candidate labels, review queues, taxonomy backlog, evidence, QA summary, and MCP provenance.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
