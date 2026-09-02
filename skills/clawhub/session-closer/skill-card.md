## Description:

Session Closer guides agents through a structured end-of-session closeout that records a journal entry with a summary, full file surface, self-caught failure delta, behavioral fingerprint, optional pattern updates, and close summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[highnoonoffice](https://clawhub.ai/user/highnoonoffice)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to close coding or orchestration sessions with consistent records of work performed, files touched, decisions made, and follow-up risks. It is most useful where session continuity, behavioral reflection, and explicit handoff notes matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can push repository changes or send session details externally without enough user control.

Mitigation: Require explicit user approval before any git push or external notification, and confirm the target repository, branch, and destination channel.

Risk: Journal entries and close summaries can expose sensitive filenames, repository changes, credentials, or private session notes.

Mitigation: Review and redact closeout content before sharing it outside the local workspace, and avoid including secrets or private session details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/highnoonoffice/skills/session-closer)
- [Project homepage](https://github.com/highnoonoffice/hno-skills)
- [Journal Format](references/journal-format.md)
- [Pattern Keys](references/pattern-keys.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown journal entries, concise text summaries, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include file-surface lists and external-destination summaries; users should review sensitive details before sharing.]

## Skill Version(s):

1.1.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
