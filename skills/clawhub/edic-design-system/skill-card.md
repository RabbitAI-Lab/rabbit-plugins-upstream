## Description:

Generates token-driven, accessible, framework-agnostic HTML/CSS for UI components, full pages, documents, emails, and assets that follow the EDIC design system.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cgartlab](https://clawhub.ai/user/cgartlab)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and agent users use this skill to build or refactor EDIC-styled web UI, documentation, reports, email templates, and CJK-optimized visual artifacts. It is suited to content sites, brand pages, internal documents, and AI-assisted UI prototypes that should follow the EDIC token and component conventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Examples document loading EDIC CSS and JavaScript from an unpinned @main CDN URL.

Mitigation: For production use, vendor the assets or pin the CDN URL to a reviewed release or commit.

Risk: Optional Google Fonts links can create third-party browser requests.

Mitigation: Use the documented system font stack, self-host fonts, or omit Google Fonts where third-party requests are a concern.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cgartlab/skills/edic-design-system)
- [Server-resolved GitHub provenance](https://github.com/cgartlab/edic-design-system/tree/main/skills/edic-design-system)
- [EDIC website](https://edic.cgartlab.com/)
- [EDIC usage docs](https://edic.cgartlab.com/docs.html)
- [EDIC structured tokens](https://edic.cgartlab.com/tokens.json)
- [EDIC complete token reference](artifact/references/TOKENS.md)
- [EDIC scene recipes](artifact/references/RECIPES.md)
- [EDIC page-level patterns](artifact/references/PATTERNS.md)
- [EDIC component HTML examples](artifact/references/EXAMPLES.md)
- [EDIC anti-patterns and replacements](artifact/references/ANTI-PATTERNS.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with HTML/CSS code blocks and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated UI should use EDIC design tokens, semantic HTML, dark-mode-compatible styling, and accessibility checks; email output uses inline sRGB styles as documented by the skill.]

## Skill Version(s):

1.9.3 (source: release metadata; artifact frontmatter reports 1.10.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
