## Description:

Guides an agent to propose focused improvement merge requests in the helm-openclaw GitLab project and close stale self-authored merge requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents maintaining the helm-openclaw project use this skill to record worthwhile improvements as separate GitLab merge requests and manage their own stale requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses GitLab credentials to manage merge requests in a specific external project.

Mitigation: Install only for the intended project and review the GitLab token's permissions before use.

Risk: An agent could create, assign, or close merge requests without the user's intent.

Mitigation: Require explicit approval before creating, assigning, or closing merge requests.

## Reference(s):

- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)
- [ClawHub skill listing](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [GitLab merge-request proposals and status updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create, assign, or close merge requests in the named GitLab project.]

## Skill Version(s):

1.105.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
