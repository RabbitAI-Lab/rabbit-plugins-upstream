## Description:

Agenty lets agents read, create, update, delete, and operate Agenty resources through the OOMOL-connected oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to inspect Agenty action schemas, manage agents, lists, rows, jobs, and configurations, and retrieve generated outputs through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may execute remote installer scripts directly without verification.

Mitigation: Review installer source and prefer a verified, version-pinned installation path before use.

Risk: Write and destructive Agenty actions can change or remove agents, lists, rows, jobs, or configurations.

Mitigation: Require user confirmation of the exact target, payload, and effect before running write or destructive actions.

Risk: Incorrect payloads may cause unintended Agenty operations.

Mitigation: Inspect the live action schema before building request payloads.

## Reference(s):

- [Agenty homepage](https://agenty.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-agenty)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions may return JSON responses, raw text content, logs, screenshots, PDFs, or downloadable files depending on the selected Agenty operation.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
