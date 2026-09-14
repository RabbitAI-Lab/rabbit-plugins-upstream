## Description:

Animate one product image, portrait, photo, illustration, or AI artwork into a directed short video with purposeful motion and camera movement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative teams use this skill to turn a supplied still image into a short image-to-video clip for product animation, social hooks, cinematic motion, animated portraits, storyboard shots, and moving artwork. The skill guides live model checks, paid-task confirmation, single-submit execution, polling, delivery reporting, and visual drift review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared local bearer credential with broad media, account, wallet, task, artifact, and cancellation authority.

Mitigation: Install only if the user trusts Beatra with that local credential; keep the credential out of chat, logs, command arguments, and environment variables, and revoke the Beatra device authorization when the skill is no longer used.

Risk: Silent package updates are enabled by default before ordinary Beatra commands.

Mitigation: Use the packaged update controls to disable silent checks when required, and rely on the package's checksum and manifest verification before accepting updates.

Risk: Image-to-video generation is paid work and can consume Beatra credits.

Mitigation: Check live model and pricing facts, show an admission card, require explicit confirmation of sufficient credits or top-up, submit each frozen paid request once, and report the returned net charged credits.

Risk: Generated motion can drift from the source image, including changes to faces, product shape, logos, typography, or composition.

Mitigation: Treat user-named details as must-keep priorities, review inspectable output against the source image, report visible drift honestly, and wait for fresh approval before any paid revision.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/image-to-motion)
- [Beatra skill homepage](https://beatra.ai/skills/image-to-motion)
- [Motion brief, request, and recovery](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report returned Beatra task IDs, statuses, usage, billing facts, and generated video artifact links when execution succeeds.]

## Skill Version(s):

0.1.7 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
