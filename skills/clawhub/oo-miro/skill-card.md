## Description:

Miro lets an agent inspect live Miro connector schemas and run OOMOL `oo` CLI actions to read, create, update, and delete Miro boards and board items through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users can use this skill to operate Miro from an agent workflow, including listing boards, inspecting items, creating board content, updating sticky notes, and deleting selected items after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running a remote installer script directly.

Mitigation: Review the installer path and use this setup flow only when the `oo` CLI is missing and the user trusts the source.

Risk: Using the connector requires trusting OOMOL with access to the connected Miro account.

Mitigation: Use the skill only with an OOMOL account and Miro connection the user approves for the requested workspace access.

Risk: Create, update, and delete actions can change or remove Miro content.

Mitigation: Confirm the exact target, payload, and expected effect before running any write or destructive action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-miro)
- [Miro Homepage](https://miro.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
