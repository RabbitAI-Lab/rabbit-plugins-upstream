## Description:

Use when users need visual direction, interface hierarchy, layout decisions, design specifications, or prototypes before implementing a Web or mini program UI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Developers and designers use this skill to plan visual direction, specify interface styling, and create web or mini-program UI prototypes before implementation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may prompt an agent to fetch UI assets from the internet using shell commands.

Mitigation: Specify permitted asset sources and download locations, and require confirmation before running curl, wget, Invoke-WebRequest, or similar commands.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/binggg/skills/ui-design-guide)
- [UI Design Activation Checklist](checklist.md)

## Skill Output:

**Output Type(s):** [Guidance, Code]

**Output Format:** [Markdown design specification with optional frontend prototype code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Design specification precedes interface code; prototypes default to at most four pages unless more are requested.]

## Skill Version(s):

1.18.80 (source: ClawHub release metadata; bundled skill frontmatter lists 2.35.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
