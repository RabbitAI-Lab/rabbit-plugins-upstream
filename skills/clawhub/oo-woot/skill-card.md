## Description:

Woot helps agents list live Woot offers and retrieve detailed offer information through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up live Woot category feeds and retrieve offer details from a connected Woot account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can ask an agent to run a remote installer script for the oo CLI.

Mitigation: Review the installer source and prefer installing the oo CLI from verified official documentation before using the skill.

Risk: Woot access is mediated through OOMOL server-side credentials.

Mitigation: Install only when the user is comfortable using OOMOL as an intermediary for Woot data and limit use to explicit Woot offer or feed lookup tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-woot)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Woot homepage](https://www.woot.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Woot offer and feed lookups; setup guidance is used only after missing CLI, authentication, or connection errors.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
