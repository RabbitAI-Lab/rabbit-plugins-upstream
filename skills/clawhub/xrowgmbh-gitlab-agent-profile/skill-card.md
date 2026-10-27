## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to maintain a GitLab agent profile with monthly contribution charts and proof records, including anonymized totals for private or internal activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An undisclosed npm fallback can download and run third-party code with access to the job's credentials.

Mitigation: Before running, replace the automatic npm download with an explicitly installed, reviewed converter and limit GitLab access to the intended projects.

Risk: Published private-activity totals may reveal information about private or internal work.

Mitigation: Review the published private-activity totals before enabling scheduled pushes.

## Reference(s):

- [GitLab Agent Profile on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)
- [xrowgmbh publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [Files, JSON, Guidance]

**Output Format:** [Static SVG and WebP charts, a JSON proof file, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Monthly contribution totals and scores; public records are listed while private and internal activity is summarized by month and category.]

## Skill Version(s):

1.122.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
