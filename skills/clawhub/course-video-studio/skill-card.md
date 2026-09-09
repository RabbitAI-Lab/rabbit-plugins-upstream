## Description:

Turn lesson materials into presenter-led course videos with lecture narration. This course video studio prepares the spoken narration for each lesson, then records a digital-teacher delivery, so enablement teams get ready-to-publish lecture videos and training presenter clips.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Training, enablement, and course-production teams use this skill to turn finalized lecture scripts and an authorized teacher portrait into ordered presenter-led lesson videos with narration, review, billing, and recovery guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants broad Beatra account authority through a shared device credential.

Mitigation: Install only if Beatra is trusted with the account and media involved, and use it only where broad generation, upload, task, wallet, and voice permissions are acceptable.

Risk: The bundled client silently self-updates local executable skill files by default.

Mitigation: Disable automatic updates after install with `python3 scripts/mcp_client.py update --auto off` when review-before-update is required.

## Reference(s):

- [Course video workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/course-video-studio)
- [Beatra skill homepage](https://beatra.ai/skills/course-video-studio)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline JSON payloads and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports staged narration, video generation, task polling, billing review, recovery, authorization, update, and uninstall workflows.]

## Skill Version(s):

0.1.3 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
