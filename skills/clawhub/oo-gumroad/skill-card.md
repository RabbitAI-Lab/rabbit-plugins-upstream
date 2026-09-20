## Description:

Gumroad enables agents to read, create, and update Gumroad account data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect Gumroad users, products, sales, and subscribers, and to perform confirmed account-changing sales actions such as refunds, shipment updates, and receipt resends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform account-changing Gumroad actions, including refunds, shipment updates, and receipt resends.

Mitigation: Confirm the exact action payload and expected effect with the user before running any write action.

Risk: The first-time setup section includes remote installer one-liners.

Mitigation: Prefer a verified installer or inspect the installer script before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gumroad)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Gumroad homepage](https://gumroad.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action payload construction; write actions require user confirmation.]

## Skill Version(s):

1.0.5 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
