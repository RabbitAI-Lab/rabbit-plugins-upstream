## Description:

pretix (pretix.eu) helps agents read, create, and update pretix data through OOMOL's oo CLI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and developers use this skill to inspect pretix connector schemas, list and fetch organizers, events, items, and orders, and prepare confirmed connector actions for pretix workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Install the oo CLI through a verified package manager or an inspected downloaded installer before using the skill.

Risk: pretix requests and order data are sent through OOMOL's connector.

Mitigation: Use the skill only when that connector path is acceptable for the relevant pretix account and data.

Risk: The get_order action is labeled as write even though its description is read-like.

Mitigation: Inspect the live connector schema and confirm the intended payload and effect before running get_order.

## Reference(s):

- [ClawHub pretix skill](https://clawhub.ai/oomol/skills/oo-pretix)
- [pretix homepage](https://pretix.eu)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
