## Description:

Turn user-supplied merchant inspection notices and authorized stills into one market inspection talking clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Market-supervision offices use this skill to turn supplied merchant inspection notices and authorized stills into short, separate talking clips that read only the supplied notice text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package stores a broad persistent Beatra Device Token on disk.

Mitigation: Install only after reviewing the authorization scope, keep the local Beatra state private, never expose the token in chat or logs, and revoke or uninstall the connection when it is no longer needed.

Risk: The package silently self-updates executable package files by default.

Mitigation: Review the auto-update posture before installation, consider disabling silent checks with the provided command, and use the documented manual check path when a controlled update process is required.

Risk: Clone, speech, video, and cancellation operations can spend credits or affect paid asynchronous tasks.

Mitigation: Require explicit user approval for each paid stage, read live pricing before submission, use opaque request IDs, poll existing tasks, and retry only byte-identical uncertain requests.

Risk: The workflow can misuse likeness, voice, or inspection context if source rights and notice text are unclear.

Mitigation: Use only authorized stills, authorized voice samples, and user-supplied merchant notice text; do not invent violations, enforcement conclusions, outcomes, or approvals.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/market-inspect-talking)
- [Beatra Skill Homepage](https://beatra.ai/skills/market-inspect-talking)
- [Merchant Notice Talking-Clip Workflow](references/workflow.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Installation Registration](references/installation-registration.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Tasks and Results](references/tasks-and-results.md)
- [MCP Connection](references/mcp-connection.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance, files]

**Output Format:** [Markdown guidance with JSON payloads, shell commands, task status summaries, and delivered media artifact details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one 2-15s talking clip per still, normally 2 to 8 clips; reports MIME type, duration, size, and net charged credits when present.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
