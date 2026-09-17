## Description:

Operate SuperSaaS through an OOMOL-connected account to search and read scheduling data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect SuperSaaS connector schemas and run read/list actions for appointments, slots, schedules, resources, groups, forms, field names, and recent booking changes through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Use an official, versioned, integrity-checked installer source and independently verify it before running remote installation commands.

Risk: The skill accesses SuperSaaS data through OOMOL-mediated credentials.

Mitigation: Install only when OOMOL-mediated access is acceptable, and use the skill for explicit read/list tasks requested by the user.

Risk: Future connector actions could change SuperSaaS state if write or destructive actions are added.

Mitigation: Require user confirmation of the exact payload and expected effect before running any state-changing action.

## Reference(s):

- [SuperSaaS homepage](https://www.supersaas.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-super-saas)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill tells the agent to inspect live connector schemas before constructing JSON payloads and to run read-oriented SuperSaaS actions through the oo CLI.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
