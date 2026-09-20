## Description:

Xodo Sign (eversign.com) skill for reading, creating, updating, and deleting Xodo Sign data through the OOMOL eversign connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Xodo Sign documents, templates, businesses, audit logs, signer reminders, and signer reassignment through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can ask users to run remote oo CLI installer scripts.

Mitigation: Review the installer source first and prefer a verified, pinned, or package-manager installation path before installing the oo CLI.

Risk: Write and destructive actions can create documents, send reminders, or reassign signers in the connected Xodo Sign account.

Mitigation: Use the skill only with the intended OOMOL-connected account and require explicit confirmation of the target, payload, and effect before running state-changing actions.

## Reference(s):

- [Xodo Sign homepage](https://eversign.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands execute through the oo CLI against the connected Xodo Sign account; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
