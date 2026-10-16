## Description:

Guides a GitLab agent to propose improvements to the helm-openclaw project through merge requests and close stale self-created requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to have a GitLab agent propose focused improvements to helm-openclaw, assign its own merge requests, and close its stale merge requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The personal-growth label obscures instructions to modify merge requests in a specific GitLab project.

Mitigation: Install only if GitLab merge request management for helm-openclaw is intended; review the skill instructions first.

Risk: An agent with GitLab credentials could create, assign, or close merge requests without appropriate review.

Mitigation: Use a least-privilege token and require explicit confirmation before each merge request change.

## Reference(s):

- [helm-openclaw project](https://gitlab.com/xrow-public/helm-openclaw)
- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown merge request proposals and GitLab merge request actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab and a GitLab token; may create, assign, or close merge requests.]

## Skill Version(s):

1.110.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
