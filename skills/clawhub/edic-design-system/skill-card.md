## Description:

Generate UI components, full pages, documents, emails, and assets that follow the EDIC design system, including editorial olive styling, OKLch tokens, dark-mode readiness, and CJK-optimized typography.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cgartlab](https://clawhub.ai/user/cgartlab)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and content teams use this skill to have an agent produce EDIC-compliant HTML, CSS, Markdown, documents, emails, and UI guidance for content-heavy websites, brand pages, reports, portfolios, and CJK-focused prototypes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated UI may be biased toward EDIC olive editorial styling or Chinese/CJK examples even when the user requested different brand, language, or framework conventions.

Mitigation: Tell the agent to preserve the requested language, accessibility labels, framework conventions, and brand colors whenever they differ from EDIC defaults.

Risk: Generated snippets that assume EDIC assets may not render correctly if the host page has not loaded the required stylesheet or optional script.

Mitigation: Verify that the target page links the EDIC stylesheet before using generated components, and include the optional script when theme toggles or interactive helpers are required.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/cgartlab/edic-design-system/tree/main/skills/edic-design-system)
- [ClawHub skill page](https://clawhub.ai/cgartlab/skills/edic-design-system)
- [EDIC website](https://edic.cgartlab.com/)
- [EDIC usage docs](https://edic.cgartlab.com/docs.html)
- [Structured tokens](https://edic.cgartlab.com/tokens.json)
- [Scene recipes](references/RECIPES.md)
- [Page-level patterns](references/PATTERNS.md)
- [Component HTML examples](references/EXAMPLES.md)
- [Token reference](references/TOKENS.md)
- [Anti-patterns and replacements](references/ANTI-PATTERNS.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown and HTML/CSS snippets with optional shell commands or configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are expected to use EDIC design tokens, semantic structure, accessibility attributes, and dark-mode-compatible styling.]

## Skill Version(s):

1.9.2 (source: ClawHub release metadata; artifact frontmatter and README state 1.10.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
