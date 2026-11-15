## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to review an agent's learning, prepare worthwhile improvement ideas as GitLab merge requests, and close their own merge requests that have remained unaccepted for 10 days after recent activity or review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make authenticated GitLab changes, including creating and closing merge requests without task-specific approval.

Mitigation: Review each proposed merge request and approve its creation or closure before allowing the skill to act.

## Reference(s):

- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, GitLab merge requests]

**Output Format:** [Written findings and improvement ideas in a GitLab merge request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a merge request for each worthwhile improvement idea.]

## Skill Version(s):

1.147.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
