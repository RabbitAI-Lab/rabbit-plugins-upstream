## Description:

This skill manages Coolify requests for reading, creating, updating, and deleting data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Coolify projects, applications, and deployments from an OOMOL-connected account. It supports read operations and controlled deployment actions such as deploy, restart, start, stop, and cancel deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unpinned remote install scripts that could execute arbitrary code.

Mitigation: Review the oo CLI installation path before installing; prefer a pinned, verified installer or trusted package manager.

Risk: Write and destructive Coolify actions can change deployment state or stop applications.

Mitigation: Confirm the exact target, payload, and effect with the user before running write or destructive actions.

## Reference(s):

- [Coolify homepage](https://coolify.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-coolify)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
