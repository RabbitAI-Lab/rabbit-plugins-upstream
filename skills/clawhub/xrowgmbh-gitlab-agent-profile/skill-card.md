## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to update a GitLab agent profile with monthly contribution charts and proof records. It summarizes merged merge requests and owner commits across selected projects while keeping private and internal project details out of public records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An undocumented fallback can automatically download and run unpinned software in the authenticated environment.

Mitigation: Use a reviewed, preinstalled converter or remove the automatic npm fallback before running.

Risk: Incorrect project, profile repository, output-path, or private-activity publication settings could expose unintended information.

Mitigation: Confirm the target projects, profile repository, output paths, and publication of private activity totals; use narrowly scoped credentials and keep scheduling disabled until reviewed.

## Reference(s):

- [GitLab Agent Profile on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, Static charts, JSON data]

**Output Format:** [SVG and WebP contribution charts plus JSON proof records]

**Output Parameters:** [Configurable number of completed calendar months; defaults to 12]

**Other Properties Related to Output:** [Public records are date-sorted; private and internal activity is represented only in anonymized monthly totals.]

## Skill Version(s):

1.114.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
