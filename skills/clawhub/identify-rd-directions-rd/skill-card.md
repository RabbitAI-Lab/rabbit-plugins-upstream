## Description:

Convert a concrete engineering, scientific, manufacturing, or technical project requirement into evidence-backed R&D directions, including requirement analysis, bounded technical issues, research questions, tasks, targets, deliverables, patent and literature evidence, standards and engineering cases, relevant organizations, search logs, and synchronized Markdown and HTML reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and technical teams use this skill to turn a concrete project requirement into structured R&D directions with traceable requirement analysis, evidence-backed tasks, validation targets, and synchronized report artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can create report files and may overwrite named outputs when replacement is explicitly authorized.

Mitigation: Use an explicit output directory, review target paths before rendering, and rely on the artifact's overwrite gate for existing files.

Risk: Evidence searches may expose sensitive project details if queries include confidential requirement text.

Mitigation: Use confidentiality-minimized wording for external searches and confirm authorization before querying patent, literature, standards, or web sources.

Risk: R&D directions and evidence summaries may be mistaken for legal, safety, regulatory, funding, or investment conclusions.

Mitigation: Treat outputs as technical research planning support and route legal, safety, regulatory, commercial, or specialist conclusions to qualified reviewers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/identify-rd-directions-rd)
- [PatSnap Advanced Patent Search](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Patent Briefing](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Validated JSON payload plus synchronized Markdown and self-contained HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces deterministic Markdown and HTML from one reviewed canonical payload and may create report files in an explicit output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
