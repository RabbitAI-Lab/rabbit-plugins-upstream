## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using a GitLab agent use this skill to reflect on project improvements, prepare focused merge requests, and identify their own stale merge requests for closure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill targets a fixed GitLab project and may create or close merge requests without user approval.

Mitigation: Confirm the project is the intended destination and require approval before creating or closing merge requests.

Risk: Proposed merge request content could disclose confidential information.

Mitigation: Review proposed content before publishing, and use project-limited GitLab credentials.

## Reference(s):

- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)
- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Merge request descriptions and project updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Focus each merge request on one issue and assign new merge requests to the agent.]

## Skill Version(s):

1.115.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
