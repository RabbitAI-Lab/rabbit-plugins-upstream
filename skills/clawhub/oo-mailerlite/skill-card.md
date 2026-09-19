## Description:

MailerLite (mailerlite.com). Use this skill for MailerLite requests that read, create, update, or delete data through the OOMOL MailerLite connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage MailerLite subscribers, groups, group membership, and account fields through an OOMOL-connected MailerLite account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the OOMOL CLI.

Mitigation: Review the OOMOL CLI installation path and do not run remote installer commands automatically.

Risk: MailerLite subscriber and account operation data may be routed through OOMOL-connected services.

Mitigation: Connect MailerLite only when the user accepts that routing model and the account has appropriate access for the requested task.

Risk: Write and destructive actions can change or delete MailerLite groups, subscribers, or group memberships.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running any write or destructive action.

## Reference(s):

- [ClawHub MailerLite skill page](https://clawhub.ai/oomol/skills/oo-mailerlite)
- [MailerLite homepage](https://www.mailerlite.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL MailerLite connection page](https://console.oomol.com/app-connections?provider=mailerlite)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and JSON command payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before payload construction and requires confirmation before write or destructive actions.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
