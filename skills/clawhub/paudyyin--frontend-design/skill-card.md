## Description:

Frontend Design helps agents create distinctive, accessible frontend interfaces with deliberate palette, typography, layout, brand-reference, design-system, Tailwind/shadcn, and UI guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paudyyin](https://clawhub.ai/user/paudyyin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and design-oriented agents use this skill when building or redesigning UI components, pages, dashboards, landing pages, brand systems, and frontend visual assets that need accessible, distinctive design direction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional persistence workflow can overwrite Markdown files outside its intended folder when crafted paths are provided.

Mitigation: Keep output inside the current workspace, avoid untrusted project names, page names, and output directories, and back up important Markdown files before using persistence.

Risk: The skill may recommend package-install or npx commands as part of frontend implementation guidance.

Mitigation: Review package-install commands before running them and confirm the packages match the current project.

Risk: Prior design context may influence output when memory reuse is enabled.

Mitigation: Disable memory reuse when prior design context should not affect a new project.

## Reference(s):

- [Frontend Design ClawHub Skill Page](https://clawhub.ai/paudyyin/skills/frontend-design)
- [Skill Definition](SKILL.md)
- [Anti-Slop Checklist](references/anti-slop.md)
- [Design Systems Guide](references/design-systems.md)
- [Design Routing Guide](references/design/design-routing.md)
- [Design System Token Architecture](references/design-system/token-architecture.md)
- [shadcn/ui Components Guide](references/ui-styling/shadcn-components.md)
- [Tailwind Responsive Guide](references/ui-styling/tailwind-responsive.md)
- [Slide Generation Skill](references/slides/SKILL.md)
- [UX Priorities](references/ux-priorities.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional code blocks, shell commands, JSON-like design-system recommendations, and persisted Markdown design-system files when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use local CSV and reference searches; optional persistence writes design-system Markdown files.]

## Skill Version(s):

2.4.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
