## Description:

Capture features and bugs as sanitized GitLab issues during planning meetings, only on the requester's explicit instruction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Meeting participants use this skill to turn explicitly requested feature and bugfix discussions into sanitized GitLab issues in the project they select.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitLab issue content must be authored in English, which may not suit every meeting workflow.

Mitigation: Check that English issue content is appropriate for the project; the skill allows spoken and chat replies in the requester's chosen language.

Risk: Meeting details or secrets could be disclosed in an issue if outgoing content or attachments are not sanitized.

Mitigation: Inspect the complete issue payload and attachments, remove identifying information and secrets, and omit content that cannot be sanitized safely.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-meeting-assistant)
- [Publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [GitLab issue titles and descriptions, plus brief conversational replies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Issue creation requires an explicit request and the selected project; authored issue content is sanitized and created confidentially.]

## Skill Version(s):

1.135.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
