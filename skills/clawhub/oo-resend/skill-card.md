## Description:

Resend helps an agent operate a connected Resend account through the OOMOL oo CLI for email reading, sending, scheduling, updating, and cancellation tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Resend email workflows through a connected OOMOL account, including reading sent or received email, sending individual or batch messages, and managing scheduled sends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path can execute a remote oo CLI installer script directly.

Mitigation: Review the installer before running it, prefer a verified package-manager installation path when available, and use the fallback only after an oo command fails because the CLI is missing.

Risk: Write and destructive actions can send emails, update scheduled delivery times, or cancel scheduled sends in the connected Resend account.

Mitigation: Require explicit user confirmation of the exact payload, target, and expected effect before running send, update, or cancellation actions.

Risk: Attachment retrieval can expose temporary download URLs for email attachments.

Mitigation: Treat returned attachment URLs as sensitive account data and share or store them only when the user explicitly requests it.

## Reference(s):

- [ClawHub Resend skill page](https://clawhub.ai/oomol/skills/oo-resend)
- [Resend homepage](https://resend.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas; state-changing and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.5 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
