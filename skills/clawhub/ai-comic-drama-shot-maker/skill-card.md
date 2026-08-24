## Description:

Turns an approved comic panel, character sheet, webtoon frame, or frozen story beat into one dynamic comic-drama shot for motion comics, manga panel animation, character entrances, emotional close-ups, action panels, and serialized creator workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to plan, preflight, submit, recover, and review Beatra comic-drama generation jobs. It supports animating one approved panel, interpolating first and last comic panels, combining loose references, or creating an original first comic frame before animation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a broad shared Beatra device token and wallet-spend-capable account access.

Mitigation: Review the package before installing, keep the credential local, and revoke the Beatra device authorization from the console when access is no longer needed.

Risk: The package can silently self-update local package files.

Mitigation: Use the documented auto-update controls and disable silent checks with the --auto off command when automatic replacement is not acceptable.

Risk: Comic-shot generation can consume Beatra credits and duplicate submissions can create unwanted paid work.

Mitigation: Require a live admission card, explicit top-up or balance confirmation, one stable client_request_id, and exact-request recovery before submitting or retrying paid generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/ai-comic-drama-shot-maker)
- [Beatra skill homepage](https://beatra.ai/skills/ai-comic-drama-shot-maker)
- [Comic-drama shot workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON payload examples, admission cards, task status summaries, and returned artifact links when generation completes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Beatra task IDs, resolved model facts, dimensions, duration, usage, billing fields, and review notes for generated shots.]

## Skill Version(s):

0.1.5 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
