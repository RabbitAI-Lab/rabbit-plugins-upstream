## Description:

Build dated store PA announcement reads for one campaign window: open, promo, flash, and close.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Retail marketers, store operators, and agents acting for them use this skill to draft and generate dated in-store PA reads for a single campaign window. It supports open, promo, flash-sale, and closing announcements using one selected or consented cloned store voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence says the skill needs review because a narrow store-announcement workflow ships broad Beatra account authority and billing-related scopes.

Mitigation: Install only when the publisher is trusted with those Beatra scopes, and review the Beatra approval page before authorizing access.

Risk: The release evidence says the skill uses a shared Beatra Device Token.

Mitigation: Keep the token only in the documented local credential file and do not expose it in chat, logs, command arguments, environment variables, or package directories.

Risk: The release evidence says package self-updates are enabled by default.

Mitigation: Disable automatic updates with the documented update command when a fixed package version is required before use.

Risk: The release evidence warns that uploaded voice samples or files are sent to Beatra.

Mitigation: Upload only files intended for Beatra processing and require explicit speaker consent before any voice clone request.

## Reference(s):

- [Store PA broadcast workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/store-pa-broadcast-pack)
- [Beatra skill homepage](https://beatra.ai/skills/store-pa-broadcast-pack)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance with JSON payload examples, shell commands, task metadata, and links or artifacts for generated audio files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dated slot IDs, campaign ledger details, task IDs, MIME type, duration, resolved model, and billing.net_charged_credits.]

## Skill Version(s):

0.1.1 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
