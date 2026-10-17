## Description:

Guides agents to create accessible, token-driven EDIC interfaces, pages, documents, and emails in an editorial olive-green style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cgartlab](https://clawhub.ai/user/cgartlab)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to generate or refactor EDIC-styled web components, full pages, documents, and emails with consistent typography, colors, accessibility, and dark-mode support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the skill globally can apply EDIC styling to unrelated work.

Mitigation: Install it in a project-scoped skill directory unless broad styling guidance is intentional.

Risk: The example toast code inserts message text through innerHTML, which is unsafe for untrusted input.

Mitigation: Use textContent or DOM node construction for user-controlled toast messages.

Risk: Chinese placeholder text in examples may not match the product language.

Mitigation: Localize example text before using it in a product.

## Reference(s):

- [EDIC website](https://edic.cgartlab.com/)
- [EDIC usage documentation](https://edic.cgartlab.com/docs.html)
- [EDIC structured tokens](https://edic.cgartlab.com/tokens.json)
- [Scene recipes](references/RECIPES.md)
- [Page-level patterns](references/PATTERNS.md)
- [Component examples](references/EXAMPLES.md)
- [Design tokens](references/TOKENS.md)
- [Anti-patterns and replacements](references/ANTI-PATTERNS.md)

## Skill Output:

**Output Type(s):** [Code, Guidance]

**Output Format:** [Markdown with HTML, CSS, and occasional JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Token-driven web styles with dark-mode and accessibility guidance; email examples use compatible static styles.]

## Skill Version(s):

2.8.2 (source: ClawHub release, skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
