## Description:

Writes and debugs CSS for layout, cascade, responsiveness, theming, browser compatibility, accessibility, and rendering performance issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to diagnose CSS failures and produce stylesheet fixes, component styles, responsive patterns, compatibility guidance, and production hardening recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read and maintain local CSS preferences and project-context notes in ~/Clawic/data/css/.

Mitigation: Review or clear those files before use if project conventions or preferences should not be reused across sessions.

Risk: CSS fixes can introduce layout, accessibility, performance, or browser-compatibility regressions when applied without project-specific testing.

Mitigation: Review generated changes and test relevant target browsers, 320px reflow, 200% zoom, focus visibility, contrast, reduced motion, and layout shift before shipping.

## Reference(s):

- [ClawHub CSS skill page](https://clawhub.ai/ivangdavila/skills/css)
- [Clawic CSS skill page](https://clawic.com/skills/css)
- [CSS skill definition](artifact/SKILL.md)
- [Setup](artifact/setup.md)
- [Memory template](artifact/memory-template.md)
- [Compatibility](artifact/compatibility.md)
- [Performance](artifact/performance.md)
- [Responsive techniques](artifact/responsive.md)
- [Accessibility-related CSS floor](artifact/SKILL.md#accessibility-floor)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with CSS examples and occasional shell or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May tailor examples using disclosed user preferences stored under ~/Clawic/data/css/.]

## Skill Version(s):

1.0.4 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
