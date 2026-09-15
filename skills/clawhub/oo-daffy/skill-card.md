## Description:

Daffy (daffy.org). Use this skill for Daffy requests involving searching and reading data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect Daffy action schemas and retrieve Daffy account, user, nonprofit, donation, contribution, and cause data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run mutable remote installer scripts without verification.

Mitigation: Install the oo CLI only after independently verifying the installer source, or use a safer package installation method where available.

Risk: Daffy connector actions can return account, donation, contribution, user, and nonprofit data.

Mitigation: Run actions only for the connected account the user authorizes and avoid exposing returned personal or financial data beyond the current task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-daffy)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Daffy homepage](https://www.daffy.org/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect live action schemas before running Daffy connector actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
