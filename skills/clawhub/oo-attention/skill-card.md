## Description:

Attention connector skill for searching, reading, and analyzing Attention conversations, deals, teams, and users through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to let an agent retrieve and analyze Attention conversations, deals, teams, and users after Attention is connected through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup commands execute mutable remote installer scripts directly in the user's shell.

Mitigation: Review setup commands before installation and prefer downloading, inspecting, and verifying the OOMOL CLI installer before execution.

Risk: The connected OOMOL account can read Attention conversations, users, teams, and related deal data.

Mitigation: Use the skill only with an account and workspace where this level of Attention data access is acceptable.

## Reference(s):

- [Attention homepage](https://attention.com)
- [OOMOL CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
