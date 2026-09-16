## Description:

Figma (figma.com). Use this skill for Figma requests that read, create, update, delete, inspect, or render Figma data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and design-automation agents use this skill to operate on Figma files, nodes, metadata, components, styles, comments, dev resources, and rendered node images without handling raw Figma credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute unverified local code.

Mitigation: Review setup before installation, prefer a verified or package-manager installation of the oo CLI, and avoid piping remote scripts directly into a shell.

Risk: Write and destructive Figma actions can change or remove comments, reactions, or dev resources.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Figma skill](https://clawhub.ai/oomol/skills/oo-figma)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Figma](https://www.figma.com)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId fields when actions are run with --json.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
