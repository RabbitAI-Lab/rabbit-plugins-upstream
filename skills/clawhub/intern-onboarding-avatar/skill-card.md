## Description:

Turns authorized stills and already-written intern onboarding notes into short Beatra talking clips, one clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters and hiring managers use this skill to turn approved intern onboarding facts, still images, and authorized likeness or voice assets into short first-day talking clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra Device Token grants broad media, task, voice, artifact, wallet, and cancellation capabilities.

Mitigation: Install only on trusted devices, review Beatra account permissions and billing controls before use, and avoid exposing the token in chat, logs, command arguments, or environment variables.

Risk: The bundled client can silently update package-owned files by default.

Mitigation: Use the documented update command to disable automatic checks when change control is required, and review updates before approving paid generation.

Risk: Voice clone, speech, and video generation are paid stages that can create charges if repeated incorrectly.

Mitigation: Require explicit approval for each stage, use one opaque request identity per paid task, and retry uncertain submissions only with byte-identical arguments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/intern-onboarding-avatar)
- [Beatra skill homepage](https://beatra.ai/skills/intern-onboarding-avatar)
- [Intern onboarding talking-clip workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown with inline JSON and shell command blocks; generated media files from Beatra tasks when paid generation is approved.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a labeled clip list and, after explicit paid-stage approval, separate 2 to 15 second talking-clip files.]

## Skill Version(s):

0.1.1 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
