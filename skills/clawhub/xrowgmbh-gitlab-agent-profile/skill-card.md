## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers maintaining a GitLab agent profile use this skill to collect monthly contribution activity and update a static chart with public proof records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The WebP fallback may download and run an unpinned npm package when ImageMagick is unavailable.

Mitigation: Prefer an available ImageMagick renderer, or review and pin the fallback package before running the update.

Risk: The security scan was partial because five local references could not be resolved.

Mitigation: Review the unresolved references and their sources before installing or running the skill.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)
- [Publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [Files, SVG charts, WebP charts, JSON]

**Output Format:** [Static SVG and WebP charts with JSON proof records]

**Output Parameters:** [Monthly activity for the 12 most recently completed calendar months by default]

**Other Properties Related to Output:** [Public records are listed individually; private and internal activity is summarized by month, kind, and category.]

## Skill Version(s):

1.137.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
