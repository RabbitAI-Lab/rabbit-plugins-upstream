## Description:

This skill helps agents manage Geckoboard data through OOMOL-connected actions for reading, creating, updating, and deleting datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Geckoboard datasets through an OOMOL-connected account, including creating datasets, appending or replacing records, and deleting datasets when explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write to, replace, or delete Geckoboard dataset data.

Mitigation: Confirm the exact payload, target dataset, and expected effect with the user before running write or destructive actions.

Risk: The one-time setup path may require installing the oo CLI.

Mitigation: Confirm trust in OOMOL as the connector provider and verify installer commands through official OOMOL documentation before installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-geckoboard)
- [Geckoboard Homepage](https://www.geckoboard.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
