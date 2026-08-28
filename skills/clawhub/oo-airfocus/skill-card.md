## Description:

Use airfocus through a connected OOMOL account to read, search, create, update, and delete airfocus data without calling the airfocus API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and workspace operators use this skill to let an agent manage airfocus workspaces and items through a connected OOMOL account. It supports read workflows as well as confirmed create, update, and delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create or update airfocus items.

Mitigation: Confirm the exact action, payload, and expected effect with the user before running write actions.

Risk: Destructive actions can permanently delete airfocus items.

Mitigation: Require explicit approval for the target and deletion request before running destructive actions.

## Reference(s):

- [airfocus homepage](https://airfocus.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-airfocus)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
