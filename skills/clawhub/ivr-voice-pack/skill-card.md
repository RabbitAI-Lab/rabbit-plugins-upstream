## Description:

Build a labeled IVR voice pack for a phone tree: welcome, menu, hold, transfer, after-hours, and error prompts in one consistent brand voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan, synthesize, and deliver labeled IVR phone-tree prompts in a consistent brand voice through Beatra speech tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests a shared Beatra device credential with broad media, wallet spending, task, and artifact permissions.

Mitigation: Install only when that access is acceptable, consider using a separate or low-balance account, and keep the device credential private.

Risk: The bundled client silently checks for and installs package updates by default before ordinary Beatra commands.

Mitigation: Disable silent updates with `python3 scripts/mcp_client.py update --auto off` when review-controlled local code changes are required.

Risk: Voice cloning and speech synthesis can spend credits, and voice samples can be sensitive.

Mitigation: Confirm live estimates before paid requests, use unchanged request identities for recovery, and upload voice samples only with explicit speaker consent.

## Reference(s):

- [IVR voice-pack workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/ivr-voice-pack)
- [Beatra skill homepage](https://beatra.ai/skills/ivr-voice-pack)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON payload examples and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include labeled prompt ledgers, Beatra task IDs, artifact URLs or IDs, duration, MIME type, resolved model, and net charged credits when generation succeeds.]

## Skill Version(s):

0.1.2 (source: server evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
