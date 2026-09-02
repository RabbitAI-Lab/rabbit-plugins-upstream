## Description:

Build a labeled IVR voice pack for a phone tree: welcome, menu, hold, transfer, after-hours, and error prompts in one consistent brand voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan, synthesize, review, and recover a labeled phone-tree prompt pack for IVR, call center, auto attendant, and hotline workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist a reusable local Beatra Device Token with broad account access.

Mitigation: Review installation and authentication behavior before use, keep the token only in the documented local credential file, and never expose credentials in chat, logs, command arguments, or environment variables.

Risk: The skill can spend Beatra credits for text-to-speech generation and optional voice cloning.

Mitigation: Confirm voice choice, prompt count, live estimate, and one stable client request ID per paid task before submitting generation work.

Risk: Voice cloning can upload speaker samples and create cloned voices.

Mitigation: Use cloning only after explicit speaker authorization and follow the documented consent, sample-quality, and billing confirmation checks.

Risk: Silent automatic updates are enabled by default and can replace package code.

Mitigation: Review the update behavior before installing and disable automatic checks with the documented update command when silent package replacement is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/ivr-voice-pack)
- [Beatra skill homepage](https://beatra.ai/skills/ivr-voice-pack)
- [IVR voice-pack workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON payload examples and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a prompt ledger and delivery guidance for labeled MP3 IVR clips generated through Beatra tasks.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
