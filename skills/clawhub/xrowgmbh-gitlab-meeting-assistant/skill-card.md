## Description:

Capture features and bugs as sanitized GitLab issues during planning meetings, only on the requester's explicit instruction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Meeting participants and teams use this skill to turn explicitly requested feature and bug discussions into sanitized GitLab issues in the project they select.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting content may contain personal or confidential details that should not be copied into GitLab.

Mitigation: Inspect the complete issue content and attachments, replace identifying details, remove secrets, and omit anything that cannot be sanitized safely.

Risk: The available security scan was partial, and several local references were unresolved.

Mitigation: Review unresolved referenced materials before installation.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-meeting-assistant)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Sanitized GitLab issue titles and descriptions; brief chat replies in the requester's chosen language]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Issue content is written in English; issue creation occurs only on explicit request.]

## Skill Version(s):

1.134.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
