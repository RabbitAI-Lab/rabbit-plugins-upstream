## Description:

Railway lets agents read, create, update, and delete Railway data through the OOMOL-connected railway connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Railway projects, services, deployments, and logs, and to run confirmed deployment, variable update, or rollback actions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path may execute remote installer scripts directly.

Mitigation: Review the installer path before use, or install the oo CLI from a pinned and verifiable package after inspecting the downloaded installer.

Risk: The connected Railway account can grant broad project and deployment management authority.

Mitigation: Use a least-privilege Railway account or workspace connection and confirm the exact target and payload before deployments, variable changes, or rollbacks.

## Reference(s):

- [ClawHub Railway Skill](https://clawhub.ai/oomol/skills/oo-railway)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Railway](https://railway.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions and requires explicit approval for write or destructive Railway operations.]

## Skill Version(s):

1.0.2 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
