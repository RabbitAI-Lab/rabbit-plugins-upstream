## Description:

Turn authorized stills and already-written intern onboarding notes into one intern onboarding talk per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, hiring managers, and people teams use this skill to turn authorized photos and already-written onboarding notes into short first-day talking clips for interns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform billable Beatra operations.

Mitigation: Review live model pricing, show the stage-specific confirmation card, and wait for user approval before each paid clone, speech, or video request.

Risk: The skill stores and reuses a shared local bearer token for broad Beatra account authority.

Mitigation: Authorize only when the shared Beatra scopes are acceptable, keep credential files private, and revoke the device from Beatra or run the bundled uninstall flow when access is no longer needed.

Risk: The bundled client silently updates its package by default.

Mitigation: Disable automatic updates before use in stable or reviewed environments with the documented update command.

## Reference(s):

- [Intern Onboarding Talks on ClawHub](https://clawhub.ai/beatra-ai/skills/intern-onboarding-avatar)
- [Intern Onboarding Talks homepage](https://beatra.ai/skills/intern-onboarding-avatar)
- [Intern onboarding talking-clip workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Files, Guidance]

**Output Format:** [Markdown with inline JSON and shell command examples; generated media is delivered as separate files or artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill plans a free clip list first, then can guide separate paid clone, speech, and video tasks with live pricing, task polling, usage, and billing results.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
