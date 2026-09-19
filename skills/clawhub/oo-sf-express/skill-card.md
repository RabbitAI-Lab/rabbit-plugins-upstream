## Description:

Use this skill for SF Express requests through the OOMOL SF Express connector, including reading, creating, updating, and deleting logistics data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate SF Express logistics workflows from an agent, including pickup checks, shipment creation, cancellation, waybill allocation, tracking, pricing, print generation, delivery-time queries, and station or freight operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands that execute downloaded scripts directly.

Mitigation: Install the oo CLI only from a verified release or after inspecting the installer, consistent with the server security guidance.

Risk: The skill can perform real account-changing SF Express logistics actions such as creating, cancelling, updating, printing, notifying, and modifying shipment data.

Mitigation: Confirm the exact payload and business effect with the user before write or destructive actions, and review connector responses for the expected execution result.

## Reference(s):

- [SF Express Open Platform](https://open.sf-express.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-sf-express)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before actions and returns SF Express connector responses as JSON when commands are run.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
