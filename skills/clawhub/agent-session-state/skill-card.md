## Description:

Helps OpenClaw agents keep per-channel decision notes and recover context across long sessions using a write-ahead logging workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[richgoodson](https://clawhub.ai/user/richgoodson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers operating OpenClaw agents use this skill to maintain channel-specific working notes, record decisions before replying, and recover project context after compaction or session restarts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Different channels whose names normalize to the same file slug may share persistent session notes.

Mitigation: Before multi-channel or multi-tenant use, require immutable unique channel IDs, namespace files by workspace or account, and verify stored channel identity before reading or writing.

## Reference(s):

- [Agent Session State on ClawHub](https://clawhub.ai/richgoodson/skills/agent-session-state)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown session notes and text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes per-channel notes to memory/sessions/ and supports distillation into longer-term memory.]

## Skill Version(s):

2.2.0 (source: skill metadata and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
