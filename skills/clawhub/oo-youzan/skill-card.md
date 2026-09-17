## Description:

Youzan (youzan.com). Use this skill for Youzan requests that read, create, or update shop, item, order, logistics, refund, and after-sale data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect live Youzan connector schemas and run account-scoped Youzan actions for shop, product, order, logistics, refund, and after-sale workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute shell or PowerShell content directly.

Mitigation: Install the oo CLI only from an official, versioned, verifiable source and review installer behavior before execution.

Risk: The connector uses OOMOL-managed credentials and may access Youzan account data or account-scoped actions.

Mitigation: Confirm the OOMOL and Youzan connection scopes, account permissions, and intended action payload before running write-tagged actions.

Risk: Action inputs can change because payloads are based on the live connector schema.

Mitigation: Inspect the live action schema with the oo CLI before constructing each request payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-youzan)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Youzan Homepage](https://www.youzan.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should inspect the live action schema before constructing connector payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
