## Description:

Capture features and bugs as sanitized GitLab issues during planning meetings, only on the requester's explicit instruction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Teams using GitLab for planning meetings can use this skill to turn explicitly requested feature and bugfix discussions into sanitized, confidential issues in the project they select.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitLab work-item content is written in English, which may not fit teams that need issue content in another language.

Mitigation: Confirm that English issue content fits the project's workflow before using the skill.

Risk: Meeting material may contain confidential information, identifying details, or secrets that should not be copied into GitLab issues.

Mitigation: Sanitize all outgoing content and attachments before each write; anonymize identifying details and remove secrets completely.

Risk: The security analysis was partial because some local references could not be resolved, so it does not provide complete evidence.

Mitigation: Review the skill and any unresolved references before relying on the scan assessment.

## Reference(s):

- [GitLab Meeting Assistant on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-meeting-assistant)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Sanitized English-language GitLab issue content and brief conversational replies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Feature and bugfix issues are created as confidential; authored issue content is sanitized.]

## Skill Version(s):

1.148.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
