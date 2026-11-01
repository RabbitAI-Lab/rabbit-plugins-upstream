## Description:

Builds and debugs Figma files for auto layout, components, variables, libraries, prototypes, Dev Mode handoff, and scriptable plugin or REST API workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, design-system maintainers, and product engineers use this skill to diagnose and structure Figma files, prepare handoff, plan variables, components, and libraries, and draft plugin or REST API automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated plugin or REST API workflows may read or modify sensitive Figma files if used with broad access.

Mitigation: Use narrow-scoped Figma tokens, review generated automation before running it, and avoid unvetted plugins on confidential files.

Risk: Local preference memory may record user-specific Figma workflow context.

Mitigation: Review and manage files under ~/Clawic/data/figma/ according to the user's privacy and retention expectations.

## Reference(s):

- [ClawHub Figma Skill](https://clawhub.ai/ivangdavila/skills/figma)
- [Clawic Figma Skill Page](https://clawic.com/skills/figma)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Configuration]

**Output Format:** [Markdown guidance with ordered Figma UI steps and optional plugin or REST API code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local Figma preference memory under ~/Clawic/data/figma/; Figma canvas changes require user execution unless using plugin or REST API workflows.]

## Skill Version(s):

1.0.2 (source: artifact/SKILL.md frontmatter and evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
