## Description:

Turn one shop portrait and short welcome, product, FAQ, and close scripts into talking-avatar clips a store can loop overnight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External store operators and live-commerce teams use this skill to create loopable talking-head avatar clips for unattended or overnight shop livestreams. It guides rights confirmation, voice selection or cloning, speech synthesis, image-to-video generation, task polling, billing review, and delivery of welcome, product, FAQ, and close clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device authorization with broad media, task, and paid-operation capability.

Mitigation: Install only when that access is acceptable, keep the device token private, and revoke the connected agent from Beatra Console if access must be cut off.

Risk: Silent automatic update checks and replacement are enabled by default before ordinary bundled-client commands.

Mitigation: Review the automatic update behavior before use and disable silent checks with the documented update control when fixed package contents are required.

Risk: Voice cloning, speech synthesis, and avatar video generation can create paid Beatra tasks.

Mitigation: Require explicit admission and balance confirmation before billable calls, preserve request identities during recovery, and report returned net charged credits.

Risk: First-use package registration may send package and environment metadata in the background.

Mitigation: Expect non-billable registration metadata to be sent and evaluate that behavior before installing in restricted environments.

## Reference(s):

- [Unattended Live Avatar homepage](https://beatra.ai/skills/unattended-live-avatar)
- [Unattended live avatar workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON payload examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces labeled avatar clip delivery notes with task, usage, and billing facts when generation succeeds.]

## Skill Version(s):

0.1.1 (source: release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
