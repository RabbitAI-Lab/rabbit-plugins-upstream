## Description:

Textmagic (textmagic.com). Use this skill for ANY Textmagic request: reading, creating, and updating data through an OOMOL-connected Textmagic account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to read Textmagic account, contact, list, and template data, create contact lists, and send plain-text SMS messages through a connected Textmagic account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send SMS messages to many recipients through the connected Textmagic account.

Mitigation: Require explicit user confirmation for every send_message payload, including message text and recipient list, before execution.

Risk: State-changing actions can create Textmagic contact lists or send messages under the connected account.

Mitigation: Inspect the live connector schema first and review the exact write payload and intended effect with the user before running any write action.

## Reference(s):

- [Textmagic homepage](https://www.textmagic.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-textmagic)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Textmagic connector actions that read account data, create contact lists, or send SMS messages after user confirmation for writes.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
