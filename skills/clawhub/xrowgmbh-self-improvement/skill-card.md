## Description:

Guides a GitLab-enabled agent to identify self-improvement changes for helm-openclaw and manage related merge requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to have a GitLab-capable agent reflect on useful project improvements, open focused merge requests, and close older self-authored merge requests that have gone stale.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent using this skill may create merge requests in GitLab.

Mitigation: Require human approval before any live GitLab mutation and review proposed merge request content before submission.

Risk: The skill may close older merge requests created by the same agent.

Mitigation: Limit the GitLab token to the narrowest necessary project permissions and review closure actions before execution.

Risk: The self-improvement framing may understate that GitLab credentials enable project changes.

Mitigation: Install only when GitLab project automation is intended, and disclose the glab and GITLAB_TOKEN requirements to operators.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)
- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands]

**Output Format:** [Markdown, code changes, and GitLab command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the glab CLI and a GITLAB_TOKEN for live GitLab actions.]

## Skill Version(s):

1.82.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
