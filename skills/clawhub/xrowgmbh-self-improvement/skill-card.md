## Description:

Guides a GitLab agent to propose worthwhile improvements through merge requests and close its own stale merge requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using a GitLab agent can document substantive improvements in focused merge requests, assign those requests to themselves, and close their own inactive requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent could open, assign, or close GitLab merge requests without adequate review.

Mitigation: Use a minimally scoped GitLab token on a repository where these actions are acceptable, and require manual confirmation outside the skill before creating or closing any merge request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)
- [helm-openclaw project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Text guidance and GitLab merge requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab and GITLAB_TOKEN; may create, assign, or close merge requests.]

## Skill Version(s):

1.102.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
