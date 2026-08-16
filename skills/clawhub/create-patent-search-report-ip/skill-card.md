## Description:

Creates the final evidence-backed patent-landscape insight report from validated search, statistics, taxonomy, human-tagging, value-signal, and patent-package artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External IP, R&D, product, and strategy teams use this skill at Stage 4 of a patent-landscape workflow to turn validated upstream patent-analysis artifacts into a decision-readable report and manifest. It supports bounded monitoring, comparison, technical-reference, data-validation, and specialist-review actions without replacing patent counsel or subject-matter experts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent-analysis inputs can contain confidential invention, product, organization, or strategy information.

Mitigation: Review input files for confidentiality before use and keep generated report_manifest.json and report.html within the authorized workspace.

Risk: Optional live patent connector use can introduce new evidence that changes the report boundary.

Mitigation: Approve connector use only for a real evidence gap and record why upstream artifacts were insufficient and how new evidence was reconciled.

Risk: Incomplete, incompatible, or unreconciled upstream artifacts can produce misleading patent-landscape conclusions.

Mitigation: Use the skill's stop or degraded-mode behavior when required artifacts, schemas, counts, taxonomy, family identifiers, or data cutoffs cannot be reconciled.

Risk: Patent value, legal, transaction, or freedom-to-operate conclusions can be over-inferred from proxy signals.

Mitigation: Keep actions bounded to reading, monitoring, comparison, technical reference, data validation, or specialist review, and require patent counsel or expert review for legal and commercial decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/create-patent-search-report-ip)
- [PatSnap Skill Hub](https://open.patsnap.com/marketplace/skill-hub)
- [PatSnap MCP marketplace](https://open.patsnap.com/marketplace/mcp-servers)
- [PatSnap patent search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap patent briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [PatSnap deep patent mining MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-mining)
- [PatSnap core patents MCP](https://open.patsnap.com/marketplace/mcp-servers/core-patents)

## Skill Output:

**Output Type(s):** [Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance that directs the agent to write JSON and self-contained HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces report_manifest.json and one offline report.html when required validated inputs are available.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
