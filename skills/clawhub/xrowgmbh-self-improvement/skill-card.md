## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab agents use this skill to reflect on project improvements, create focused GitLab merge requests, assign those requests to themselves, and close stale self-created requests when appropriate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use GitLab access to create merge requests from a broad self-improvement prompt.

Mitigation: Install it only for agents that should manage merge requests for the named GitLab project, and require review before merge requests are created.

Risk: The skill can close older self-created merge requests after a period of inactivity.

Mitigation: Use a GitLab token with the minimum required permissions and add a confirmation requirement before closing merge requests.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)
- [helm-openclaw GitLab Project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance with proposed merge request content and GitLab CLI actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GitLab CLI access through glab and a GitLab token environment variable.]

## Skill Version(s):

1.84.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
