## Description:

Turns finished lecture scripts and an authorized teacher portrait into narrated talking-head lesson videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Course and training teams use this skill to turn finalized lecture scripts, an authorized teacher portrait, and selected or cloned voices into ordered lesson video clips. It helps agents plan narration, video admission, billing checks, task recovery, and delivery review for talking-head course production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device credential with broad authority to access media tools and spend credits.

Mitigation: Install only after reviewing the requested Beatra authority, keep the credential in the documented private local state, and require explicit user confirmation before billable generation steps.

Risk: The bundled client silently checks for and can install package updates by default.

Mitigation: Review the update behavior before installation and use the documented update command to disable automatic checks when the deployment requires manual update control.

Risk: Talking-head video generation can misuse likeness or voice rights if inputs are not authorized.

Mitigation: Require explicit likeness and voice authorization, clone consent, pronunciation confirmation, and separate approval of narration before each video generation stage.

## Reference(s):

- [Course Video Studio on ClawHub](https://clawhub.ai/beatra-ai/skills/course-video-studio)
- [Course Video Workflow](references/workflow.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include staged workflow instructions, admission-card details, task and billing reporting guidance, and recovery steps.]

## Skill Version(s):

0.1.1 (source: release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
