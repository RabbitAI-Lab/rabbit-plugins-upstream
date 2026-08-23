## Description:

Generate one cinematic vertical micro-drama shot from a frozen dramatic beat, actor and scene references, and camera direction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and agent users use this skill to plan, submit, monitor, and review one vertical cinematic micro-drama video shot from text, approved opening or ending images, or actor and location references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared full-scope persistent Beatra device token.

Mitigation: Review the Beatra authorization page before approval, keep the credential file private, and revoke the device from the Beatra Console or uninstall flow when access is no longer needed.

Risk: The bundled client performs silent package updates by default.

Mitigation: Use the documented update controls to disable automatic updates or check the available release before updating.

Risk: Video generation can spend paid Beatra credits after user approval.

Mitigation: Require an admission card and explicit balance or top-up confirmation before each paid shot, then report only returned billing details after the task completes.

## Reference(s):

- [Short-drama shot workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces shot cards, admission summaries, Beatra task status, returned video artifact links, billing details, and review notes.]

## Skill Version(s):

0.1.3 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
