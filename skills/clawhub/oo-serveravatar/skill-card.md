## Description:

ServerAvatar (serveravatar.com). Use this skill for ANY ServerAvatar request - searching and reading data. Whenever a task involves ServerAvatar, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect ServerAvatar organizations, servers, applications, and databases through an OOMOL-connected account. It guides agents to inspect the live connector schema before running read-oriented ServerAvatar actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The oo CLI can access ServerAvatar data through the user's connected OOMOL account.

Mitigation: Install and use the skill only when that account-level access is acceptable for the intended environment.

Risk: The first-time setup path uses a remote CLI installer.

Mitigation: Review the installer before running it and use the setup path only when the CLI is missing.

Risk: Future write or destructive connector actions could change or remove ServerAvatar resources.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running any write or destructive action.

## Reference(s):

- [ServerAvatar homepage](https://serveravatar.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-serveravatar)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect connector schemas and run ServerAvatar actions with JSON responses.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
