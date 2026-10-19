## Description:

Helps agents provision and warm up Cargo sending mailboxes, send email, and review replies, delivery events, and suppressions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cargo-owned outbound mailboxes, check sending allowances, deliver approved messages, and review conversations and suppression status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live email sends may contact unintended or opted-out recipients.

Mitigation: Check contact basis, relevance, and workspace suppressions before sending; obtain approval before batch sends.

Risk: Mailbox or domain provisioning can incur recurring or one-time charges.

Mitigation: Check live pricing and require explicit human approval before provisioning or purchasing.

Risk: An unpinned CLI installation and exposed Cargo credentials could compromise the workspace.

Mitigation: Install only from a trusted Cargo package, prefer a pinned CLI version, and keep the access token private.

## Reference(s):

- [ClawHub release](https://clawhub.ai/cargo-ai/skills/cargo-mailbox-management)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Sending guidance](artifact/references/sending.md)
- [Warm-up and sending allowance](artifact/references/warmup-and-allowance.md)
- [Sending domains](artifact/references/sending-domains.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown]

**Output Format:** [Markdown with shell command examples and concise status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cargo account and CLI; sending and provisioning affect real recipients and billing.]

## Skill Version(s):

1.3.1 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
