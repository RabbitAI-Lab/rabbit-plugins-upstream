## Description:

Generate token-driven, accessible, framework-agnostic HTML/CSS for EDIC-aligned UI components, full pages, documents, emails, and visual assets using the Editorial x Olive Green design system.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cgartlab](https://clawhub.ai/user/cgartlab)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and content teams use this skill to generate or refactor EDIC-styled web pages, UI components, documents, reports, and email templates with CJK-aware typography, dark-mode support, and token-driven HTML/CSS.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated UI may include locale-specific Chinese labels that do not fit the consuming project's language or audience.

Mitigation: Review generated text and labels for the target locale before release.

Risk: Examples may reference external CDN or font links when demonstrating EDIC styles.

Mitigation: Approve, pin, self-host, or replace external assets according to the consuming project's dependency policy.

Risk: Project-wide installation can influence future UI generation beyond EDIC-specific tasks.

Mitigation: Prefer project-scoped installation unless EDIC styling should apply broadly.

## Reference(s):

- [EDIC Skill Definition](artifact/SKILL.md)
- [EDIC Skill README](artifact/README.md)
- [Scene Recipes](artifact/references/RECIPES.md)
- [Page-Level Patterns](artifact/references/PATTERNS.md)
- [Component HTML Examples](artifact/references/EXAMPLES.md)
- [Token Reference](artifact/references/TOKENS.md)
- [Anti-Patterns and Correct Replacements](artifact/references/ANTI-PATTERNS.md)
- [Structured Design Tokens](artifact/tokens.json)
- [EDIC Website](https://edic.cgartlab.com/)
- [EDIC Usage Docs](https://edic.cgartlab.com/docs.html)
- [EDIC Structured Tokens](https://edic.cgartlab.com/tokens.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTML/CSS code blocks, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should use EDIC design tokens, CJK-aware typography, accessible markup, dark-mode coverage, and email-safe static styles when generating email templates.]

## Skill Version(s):

2.8.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
