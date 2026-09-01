## Description:

Captures clause risks, compliance gaps, precedent shifts, contract deviations, regulatory changes, and litigation exposure to enable continuous legal operations improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

Legal operations teams and agents use this skill to capture process-level legal learnings, compliance issues, contract deviations, regulatory changes, and litigation exposure in workspace markdown logs. It is intended to preserve reusable lessons while excluding privileged communications, case strategy, and confidential settlement terms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Legal learning logs can contain privileged, confidential, or matter-specific details if users capture raw legal context.

Mitigation: Keep .learnings local or gitignored unless reviewed, and abstract entries to process-level lessons that omit privileged communications, case strategy, and settlement terms.

Risk: Automatic reminders and Bash output detection can surface legal capture prompts in inappropriate workspaces or from sensitive command output.

Mitigation: Enable only project-scoped reminders by default, and use the Bash output detector only after explicit review.

Risk: Promoting learnings or extracting new skills can turn matter-specific observations into reusable guidance before review.

Mitigation: Require a reviewed diff and explicit user approval before promoting entries to playbooks, rules, hooks, generated skills, or shared standards.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jose-compu/skills/self-improving-legal)
- [OpenClaw Legal Integration](references/openclaw-integration.md)
- [Legal Hook Setup Guide](references/hooks-setup.md)
- [Legal Entry Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates local legal learning logs and may provide opt-in hook reminders when configured.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
