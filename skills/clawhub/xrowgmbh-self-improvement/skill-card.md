## Description:

Guides a GitLab agent to propose focused improvements to the helm-openclaw project through merge requests and close its own inactive proposals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab agents use this skill to identify meaningful improvements to helm-openclaw, submit separate merge requests for unrelated issues, and manage their own inactive proposals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A generic self-improvement description masks instructions to use GitLab credentials to change merge requests in a specific project.

Mitigation: Review before installation; use only when intending to operate on helm-openclaw with GITLAB_TOKEN, and require explicit confirmation before creating, assigning, splitting, or closing merge requests.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)
- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Text and GitLab merge requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create, assign, or close merge requests in the designated project.]

## Skill Version(s):

1.106.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
