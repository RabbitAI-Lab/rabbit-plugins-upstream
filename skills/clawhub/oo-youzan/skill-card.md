## Description:

Youzan (youzan.com). Use this skill for ANY Youzan request, including reading, creating, and updating data through the Youzan connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected Youzan shop through OOMOL, including inspecting live connector schemas and running supported shop, item, order, logistics, refund, and after-sale actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Youzan business data through a connected OOMOL account.

Mitigation: Install and authenticate the oo CLI only when needed, keep the Youzan connection scoped to the intended account, and review returned business data before sharing it.

Risk: Some connector actions may affect store or order data if the live connector contract exposes write behavior.

Mitigation: Inspect the live schema before each action and confirm the exact payload and intended effect with the user before running any write or destructive operation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-youzan)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [Youzan homepage](https://www.youzan.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should inspect the live connector schema before running actions.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
