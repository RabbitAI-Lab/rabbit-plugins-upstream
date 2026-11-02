## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

GitLab agents use this skill to identify worthwhile improvements in xrow-public/helm-openclaw, draft a separate merge request for each improvement, and close their own merge requests that have gone unaccepted for 10 days after recent activity or review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs publishing findings to xrow-public/helm-openclaw and closing older merge requests without a user-review step.

Mitigation: Use only for explicitly authorized work on the project, review findings for private information, and require approval before publishing or closing merge requests. Limit token access to the intended project and inspect the referenced gitlab-agent skill before enabling it.

## Reference(s):

- [xrow-public/helm-openclaw project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, API Calls]

**Output Format:** [Markdown merge request findings and ideas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings should address one improvement per merge request.]

## Skill Version(s):

1.125.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
