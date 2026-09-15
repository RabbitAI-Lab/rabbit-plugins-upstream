## Description:

Railway (railway.com). Use this skill for ANY Railway request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Railway projects, services, deployments, and logs through an OOMOL-connected Railway account. With explicit confirmation, it can also trigger deployments, update variables, or roll back rollback-capable deployments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes unverified remote script execution for installing the oo CLI.

Mitigation: Prefer a pinned oo CLI version and verify the installer checksum or signature before installation.

Risk: The skill can modify live Railway resources through deployments, variable updates, and rollbacks.

Mitigation: Confirm the target project, service, environment, payload, and expected effect before any write or destructive action.

## Reference(s):

- [ClawHub Railway Skill](https://clawhub.ai/oomol/skills/oo-railway)
- [Railway Homepage](https://railway.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Railway connector responses as JSON and confirmation prompts for write or destructive actions.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
