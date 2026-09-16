## Description:

Megaventory (megaventory.com). Use this skill for ANY Megaventory request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business operations teams use this skill to inspect Megaventory schemas, list inventory and order records, and create or update products, purchase orders, and sales orders through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include direct internet installer commands.

Mitigation: Use an official, verifiable installation method where possible, review installer contents before execution, and install only if OOMOL and Megaventory access through this connector is acceptable.

Risk: The skill can create or update Megaventory products, purchase orders, and sales orders.

Mitigation: Confirm the exact payload and expected effect with the user before allowing write actions.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Megaventory homepage](https://www.megaventory.com/)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-megaventory)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI connector actions; write actions require confirmation of the exact payload and effect before execution.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
