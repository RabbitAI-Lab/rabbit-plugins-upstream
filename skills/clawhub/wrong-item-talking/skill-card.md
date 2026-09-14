## Description:

Creates one short talking wrong-item explanation clip per authorized still from a teacher-supplied wrong-item script.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and education-content creators use this skill to turn authorized still images and existing wrong-item explanation points into short talking clips for mistake-cause, correction-path, and common-error reminders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation links a Beatra account and stores a reusable local token.

Mitigation: Install only when the shared Beatra credential model is acceptable, keep the credential file private, and use the bundled uninstall flow when disconnecting.

Risk: The bundled client can perform broader Beatra operations than the wrong-item clip workflow needs.

Mitigation: Review requested operations before execution and approve paid clone, speech, and video stages separately.

Risk: Silent automatic updates can replace package-owned code by default.

Mitigation: Disable automatic updates when change control is required and use the documented update check flow before accepting a newer release.

## Reference(s):

- [Wrong Item Talking Clips on ClawHub](https://clawhub.ai/beatra-ai/skills/wrong-item-talking)
- [Wrong Item Talking Clips homepage](https://beatra.ai/skills/wrong-item-talking)
- [Wrong-item-script talking-clip workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Beatra MCP endpoint](https://mcp.beatra.ai/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans clip slots before paid operations and reports generated task outputs, MIME details, durations, sizes, and net charged credits when returned.]

## Skill Version(s):

0.1.3 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
