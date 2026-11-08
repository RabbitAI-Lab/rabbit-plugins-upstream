## Description:

Capture features and bugs as sanitized GitLab issues during planning meetings, only on the requester's explicit instruction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Teams use this skill during GitLab planning meetings to turn explicitly requested feature or bugfix discussions into sanitized, confidential issues in the project selected for that meeting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting transcripts and attachments may contain confidential details or secrets that should not be copied into GitLab.

Mitigation: Sanitize all issue content and attachments before each write, remove secrets completely, and omit material that cannot be safely anonymized.

Risk: The skill requires authored GitLab issue content to be in English, which may not match the meeting language.

Mitigation: Make the English issue-content requirement clear to the team; keep spoken and chat replies in the requester's chosen language.

Risk: The security review reports incomplete local reference checks, so its evidence is not complete.

Mitigation: Review the skill and its references before relying on it, and account for the incomplete scan evidence.

## Reference(s):

- [GitLab Meeting Assistant on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-meeting-assistant)
- [xrowgmbh publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [Text, Markdown, GitLab issues]

**Output Format:** [Sanitized English issue title and description, plus a concise chat response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Issues are created only on explicit instruction and are confidential by default.]

## Skill Version(s):

1.132.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
