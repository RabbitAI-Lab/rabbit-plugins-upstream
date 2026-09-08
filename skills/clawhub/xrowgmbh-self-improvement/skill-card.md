## Description:

Guides a GitLab agent to identify improvements for the helm-openclaw project, propose them in merge requests, and close stale self-authored merge requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab agents use this skill to reflect on potential project improvements, prepare focused merge requests, and close stale self-authored merge requests for the helm-openclaw project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use an authenticated GitLab token to create and close merge requests in the hard-coded helm-openclaw project.

Mitigation: Use a least-privilege token scoped to the intended project, and manually review proposed merge requests and closure candidates before accepting changes.

Risk: Self-improvement proposals can introduce incorrect or misleading guidance into a skill or project workflow.

Mitigation: Review and scan generated changes before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)
- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown prose and GitLab merge request content with possible shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab and GITLAB_TOKEN for authenticated GitLab actions against the helm-openclaw project.]

## Skill Version(s):

1.90.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
