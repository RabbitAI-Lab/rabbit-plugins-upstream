## Description:

Design and calibrate the Stage 3/4 tagging system for a patent-landscape program after search-patents-ip and analyze-patent-search-results-ip by creating a versioned four-column technology taxonomy, decision-relevant technical questions, evidence-backed patent groups, a reviewed tagging demonstration, and a complete empty-tag CSV for genuine human tagging at Stage 3.5, then validating the returned tagged_pool.csv before routing to create-patent-search-report-ip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent landscape analysts and IP teams use this skill after search and analysis stages to design a versioned technology taxonomy, calibrate patent tagging rules, prepare reviewed examples, and hand off a complete candidate pool for authorized human tagging. It also validates the returned tagged pool before downstream patent landscape reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may need access to patent-landscape input artifacts and may write derived JSON and CSV files.

Mitigation: Confirm the workspace, file scope, privacy boundary, and approved patent connectors before installation or execution.

Risk: Automated full-pool tagging could be mistaken for authorized expert review.

Mitigation: Keep full-pool human tag fields empty, use reviewed examples only for calibration, and require an authorized human-tagged tagged_pool.csv before downstream reporting.

Risk: Mismatched scope, privacy constraints, or failed validation could make outputs unreliable.

Mitigation: Stop when scope, privacy, row-count, checksum, taxonomy-version, or validation checks fail instead of silently repairing labels or records.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yuanzhian-patsnap/skills/tag-patent-search-results-ip)
- [PatSnap Skill Hub marketplace](https://open.patsnap.com/marketplace/skill-hub)
- [PatSnap MCP marketplace](https://open.patsnap.com/marketplace/mcp-servers)
- [Deep Patent Mining MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-mining)
- [Patent Briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [Advanced Patent Search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [Global Core Patent Database MCP](https://open.patsnap.com/marketplace/mcp-servers/core-patents)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, CSV, guidance]

**Output Format:** [JSON and CSV artifacts with concise Markdown or text handoff and validation summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces tech_breakdown.json, key_questions.json, patent_packages.csv, tagging_demo_sample.csv, to_be_tagged.csv, and validation guidance for tagged_pool.csv.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
