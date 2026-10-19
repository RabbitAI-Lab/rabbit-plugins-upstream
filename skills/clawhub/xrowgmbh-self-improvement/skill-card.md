## Description:

Guides an agent to propose improvements to a GitLab project through merge requests and close stale self-authored merge requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to record worthwhile improvements as separate GitLab merge requests for the helm-openclaw project and manage older self-authored requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's personal-growth description does not clearly disclose that it can create or close merge requests using GitLab credentials.

Mitigation: Use it only for the intended project; require a dry run and explicit confirmation before creating or closing any merge request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)
- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Text and GitLab merge request descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or close merge requests in the named GitLab project.]

## Skill Version(s):

1.111.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
