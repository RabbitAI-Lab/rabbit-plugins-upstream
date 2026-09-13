## Description:

Generates a one-page model card for an AI system, covering identity, purpose, data, limits, risks, and contact details with Markdown and JSON output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, AI governance teams, and system owners use this skill to create a compact model card for an AI system or agent, including purpose, data, known limits, risks, and responsible contact information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Published install commands may fetch mutable remote content.

Mitigation: Verify the repository and pin installation to a reviewed commit or release before use.

Risk: The generator can write Markdown to a user-supplied output path.

Mitigation: Run it from a normal project or output folder and avoid sensitive paths for --out.

Risk: Generated model cards may be mistaken for final governance or compliance approval.

Mitigation: Review generated cards with the relevant owner or governance process before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/model-card-generator)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [README](README.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown model card and optional JSON object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes Markdown to a user-supplied output path when --out is provided; prints JSON when --json is set.]

## Skill Version(s):

1.0.0 (source: server release metadata and manifest.json; artifact frontmatter and changelog state 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
