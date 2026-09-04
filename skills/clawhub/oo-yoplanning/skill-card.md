## Description:

YoPlanning helps agents search and read YoPlanning teams, online products, product availability, and availability details through OOMOL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect YoPlanning teams, online products, availability slots, and related availability details through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read YoPlanning data available to the connected OOMOL account.

Mitigation: Install it only for users who intend to allow agent access to that YoPlanning data.

Risk: Write-like YoPlanning requests could affect account data if future connector actions support changes.

Mitigation: Confirm the exact action and payload with the user before running any write-like or destructive request.

## Reference(s):

- [ClawHub YoPlanning skill page](https://clawhub.ai/oomol/skills/oo-yoplanning)
- [YoPlanning homepage](https://www.yoplanning.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running YoPlanning read actions.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
