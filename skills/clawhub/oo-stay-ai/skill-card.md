## Description:

Stay AI lets agents search and read Stay AI account settings, orders, and subscriptions through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Stay AI account settings, subscriptions, and orders through an OOMOL-connected Stay AI account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes an internet installer command for the oo CLI, which the security evidence flags as unverified.

Mitigation: Install the oo CLI through a verified manual process when possible, and avoid letting an agent run the installer command directly.

Risk: The skill can expose Stay AI account, order, and subscription data through OOMOL-connected actions.

Mitigation: Use only with a Stay AI account whose data may be exposed through OOMOL, and confirm any future write-capable action before execution.

## Reference(s):

- [ClawHub Stay AI Skill](https://clawhub.ai/oomol/skills/oo-stay-ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Stay AI homepage](https://stay.ai)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill runs read-oriented Stay AI connector actions and returns JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
