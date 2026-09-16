## Description:

Sling (getsling.com). Use this skill for ANY Sling request: searching and reading data through an OOMOL-connected Sling account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and agents use this skill to retrieve Sling sessions, shifts, groups, tasks, users, coworker details, and calendar events through the OOMOL `oo` CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct remote installer execution.

Mitigation: Use official, verifiable installation instructions and do not allow an agent to run curl-to-shell or irm-to-iex installer commands automatically.

Risk: Connecting Sling through OOMOL may expose connected Sling organization data to connector actions.

Mitigation: Confirm the intended OOMOL account, Sling connection, and organization before login or connector use.

Risk: Billing setup or recharge actions may be needed after OOMOL insufficient-credit errors.

Mitigation: Require explicit user confirmation before any billing or recharge step.

## Reference(s):

- [Sling Skill Page](https://clawhub.ai/oomol/skills/oo-sling)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Sling Homepage](https://getsling.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads Sling organization data through OOMOL connector actions after the user has installed the oo CLI, signed in, and connected Sling.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
