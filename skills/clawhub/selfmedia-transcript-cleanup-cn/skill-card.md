## Description:

Cleans authorized Chinese transcript text while preserving meaning, speakers, timestamps, and uncertainty, and returns an edit log plus items that need confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as interviewers, creators, and editors use this skill to make supplied Chinese interview, oral-history, and video-caption transcripts easier to read while retaining the original claims and clearly marking uncertain passages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional installation command does not pin an installer version or repository revision.

Mitigation: Review and choose a trusted installer version and repository revision before running the command.

Risk: Unreviewed cleanup edits could misrepresent the supplied transcript.

Mitigation: Compare the clean draft and edit list with the original, and retain the skill's uncertainty markers for anything that cannot be confirmed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xxjrq/skills/selfmedia-transcript-cleanup-cn)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown with sections for the cleaned transcript, itemized edits, and items needing confirmation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts supplied transcript text up to 6,000 Chinese characters or about 20 minutes; preserves speaker and timestamp markers when provided.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
