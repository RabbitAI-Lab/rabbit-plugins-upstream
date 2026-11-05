## Description:

Organizes classroom notes into Cornell-style cues, notes, and summaries, then archives and retrieves them by subject and topic.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students use the skill to turn class notes into Cornell-style study notes, organize them by subject and topic, and retrieve related notes when reviewing. With the archive enabled and the student's permission, it can also summarize note usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional archive may retain children's notes and usage counts on the host platform.

Mitigation: Check the host's storage and deletion behavior before uploading children's information; use “这次不要记忆” for session-only use or “删除我的笔记” to remove saved notes.

Risk: Reference guidance may conflict with the main skill's limits on retaining recall states and creating retest reminders.

Mitigation: Follow the main skill rules: keep recall states within the current session and send reminders only with the student's consent.

## Reference(s):

- [Cornell note format guide](artifact/references/cornell-format-guide.md)
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-cornell-notes)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language Cornell-style notes, cue questions, summaries, retrieval results, and usage reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Archive and cross-skill summaries depend on host platform capabilities and user consent; recall status is session-only.]

## Skill Version(s):

2.12.5 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
