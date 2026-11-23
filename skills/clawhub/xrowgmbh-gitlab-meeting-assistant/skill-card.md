## Description:

Capture features and bugs as sanitized GitLab issues during planning meetings, only on the requester's explicit instruction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Meeting participants use the skill to capture discussed feature requests and bugs as sanitized GitLab issues in the project they explicitly select. It creates an issue only after a clear request addressed to the assistant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitLab work-item content is required to be in English, which may lose nuance from meetings held in other languages.

Mitigation: Keep chat replies in the requester's chosen language, and mark missing details as open rather than guessing.

Risk: Security analysis is partial because several local references could not be resolved.

Mitigation: Resolve and review the local references before relying on the workflow.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-meeting-assistant)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [English GitLab issue titles and Markdown descriptions, plus brief chat replies in the requester's chosen language]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sanitized issue content; creates confidential issues in the explicitly selected project only on a clear request.]

## Skill Version(s):

1.151.6 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
