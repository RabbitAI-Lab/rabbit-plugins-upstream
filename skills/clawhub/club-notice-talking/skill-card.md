## Description:

Turn a user-supplied club-activity script and authorized stills into one club activity talking clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External teachers and club advisors use this skill to plan and create 2 to 8 short talking clips from authorized stills and supplied activity-script points such as event name, time, place, and joining instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device credential with spending and broad media-generation capability.

Mitigation: Install only after reviewing the requested Beatra access, keep the credential private, and revoke or reauthorize access through the documented Beatra connection flow when needed.

Risk: User-selected stills, voice samples, and generated media are uploaded to Beatra for media-generation work.

Mitigation: Use only files the user can authorize, inspect inputs before upload, and avoid treating file access alone as consent for likeness or voice use.

Risk: Automatic package updates are enabled by default.

Mitigation: Use the documented update controls to disable automatic updates or perform explicit update checks when manual review is required.

Risk: Paid clone, speech, and video stages can consume Beatra credits and may create duplicate charges if retried incorrectly.

Mitigation: Confirm each paid stage separately, use one opaque request identity per approved call, and recover uncertain tasks by polling or retrying only byte-identical arguments with the same request identity.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/club-notice-talking)
- [Beatra skill homepage](https://beatra.ai/skills/club-notice-talking)
- [Activity-script talking-clip workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans separate 2 to 15 second clips and, when the user approves paid stages, can result in speech audio and talking-video media artifacts.]

## Skill Version(s):

0.1.2 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
