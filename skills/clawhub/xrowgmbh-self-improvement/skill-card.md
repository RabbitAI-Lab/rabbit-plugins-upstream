## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Agents working on the helm-openclaw GitLab project use this skill to identify worthwhile improvements, document each in a separate merge request, and close their own merge requests that remain unaccepted for 10 days after recent activity or review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may create or close GitLab merge requests without clear user authorization.

Mitigation: Confirm the target project and allowed changes before execution, and review and authorize each merge request creation or closure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)
- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown merge request descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One improvement per merge request; skips cosmetic or low-value ideas.]

## Skill Version(s):

1.149.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
