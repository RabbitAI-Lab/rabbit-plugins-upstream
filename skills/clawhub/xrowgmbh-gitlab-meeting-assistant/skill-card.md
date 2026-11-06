## Description:

Capture feature and bug requests as sanitized GitLab issues during planning meetings, only when explicitly asked.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Planning meeting participants use the assistant to capture discussed feature and bug requests as sanitized issues in the GitLab project they explicitly select. Issues are created only on a clear request and are confidential from the outset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting material may contain sensitive information or secrets that could be copied into GitLab.

Mitigation: Sanitize every issue field and attachment, remove secrets, and review created issues for sensitive details.

Risk: An issue could be sent to the wrong project or created without confidentiality controls.

Mitigation: Use only the explicitly selected project and an appropriately scoped integration; create confidentially from the outset and keep the content as a draft if confidentiality cannot be set.

## Reference(s):

- [GitLab Meeting Assistant on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-meeting-assistant)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Sanitized English GitLab issue titles and descriptions with acceptance criteria where applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates an issue only after an explicit request; issue content is sanitized and created as confidential.]

## Skill Version(s):

1.130.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
