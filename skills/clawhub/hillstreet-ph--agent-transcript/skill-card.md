## Description:

Requested GitHub PR/issue agent transcripts: redact, trim, preview, and insert safely.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Developers working on GitHub pull requests or issues use this skill when they explicitly request a relevant agent transcript. It helps find local session logs, prepare a scoped and reviewed Markdown transcript, and preview or insert it only with authorization for the named PR or issue.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local session logs may contain unrelated or sensitive information.

Mitigation: Keep discovery local, trim to the PR or issue scope, inspect the transcript, and omit it if sensitive content remains unresolved.

Risk: A preview could be mistaken for permission to publish a transcript.

Mitigation: Insert only after authorization specifically covers transcript publication to the named PR or issue.

## Reference(s):

- [ClawHub agent-transcript release](https://clawhub.ai/hillstreet-ph/skills/agent-transcript)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Trimmed, task-scoped Markdown transcript]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review for relevance and sensitive content; omit if sensitive content remains unresolved.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
