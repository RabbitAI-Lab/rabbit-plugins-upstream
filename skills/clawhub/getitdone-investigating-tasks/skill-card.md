## Description:

Explains a GetItDone task's status, notes, attachments, dependencies, and available video context without changing the task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

GetItDone users can investigate one task's details, blockers, attachments, and available video context without modifying the task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Task notes and attachments may contain private work information.

Mitigation: Review GetItDone OAuth scopes before connecting and request only tasks the user asks about.

Risk: Video summaries may omit audio and events between sampled frames.

Mitigation: Describe video findings as frame-based observations and avoid claiming audio was transcribed.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only summary; video descriptions use still frames, not audio transcription.]

## Skill Version(s):

1.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
