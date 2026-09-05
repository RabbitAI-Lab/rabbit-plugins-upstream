## Description:

Generate UI components, full pages, documents, emails, and assets that follow the EDIC design system using OKLch tokens, dark-mode-ready styling, CJK-oriented typography, and framework-agnostic HTML/CSS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cgartlab](https://clawhub.ai/user/cgartlab)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and content teams use this skill to generate EDIC-styled web components, pages, documents, emails, and UI prototypes with consistent tokens, typography, accessibility conventions, and dark-mode behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated examples may default to Chinese labels, zh-CN markup, and Simplified Chinese font stacks.

Mitigation: Ask the agent to adapt language, locale, and fonts for the target audience before using generated UI in production.

Risk: Generated pages may include external CDN or font resources.

Mitigation: Replace external asset links with approved internal hosting or pinned dependencies when project policy requires controlled asset delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cgartlab/skills/edic-design-system)
- [EDIC website](https://edic.cgartlab.com/)
- [EDIC usage docs](https://edic.cgartlab.com/docs.html)
- [EDIC structured tokens](https://edic.cgartlab.com/tokens.json)
- [EDIC Scene Recipes](artifact/references/RECIPES.md)
- [EDIC Page-Level Patterns](artifact/references/PATTERNS.md)
- [EDIC Component HTML Examples](artifact/references/EXAMPLES.md)
- [EDIC Complete Token Reference](artifact/references/TOKENS.md)
- [EDIC Anti-Patterns and Correct Replacements](artifact/references/ANTI-PATTERNS.md)
- [Bundled design tokens](artifact/tokens.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown containing HTML/CSS code, design-system guidance, and occasional shell command or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include complete runnable HTML fragments; email output uses inline sRGB styles instead of EDIC CSS tokens.]

## Skill Version(s):

1.9.4 (source: server release evidence; artifact frontmatter and README list 1.10.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
