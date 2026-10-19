## Description:

Guides agents to create accessible, token-driven EDIC interfaces, pages, documents, and emails in an editorial olive-green style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cgartlab](https://clawhub.ai/user/cgartlab)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use this skill to build or refactor EDIC-styled components, web pages, documents, and emails with consistent design tokens and accessible markup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Global installation makes EDIC guidance available in future sessions beyond the current project.

Mitigation: Install at project scope unless persistent global guidance is intended.

Risk: The toast example interpolates content into innerHTML, which is unsafe for user-controlled messages.

Mitigation: Create DOM nodes and set user-controlled messages with textContent instead.

Risk: Chinese-first labels may be inappropriate for products targeting other languages.

Mitigation: Specify the target locale and translate labels and document language before use.

## Reference(s):

- [EDIC website](https://edic.cgartlab.com/)
- [EDIC usage documentation](https://edic.cgartlab.com/docs.html)
- [EDIC structured tokens](https://edic.cgartlab.com/tokens.json)
- [Scene recipes](references/RECIPES.md)
- [Page patterns](references/PATTERNS.md)
- [Component examples](references/EXAMPLES.md)
- [Design tokens](references/TOKENS.md)
- [Anti-patterns](references/ANTI-PATTERNS.md)

## Skill Output:

**Output Type(s):** [Code, Markdown, Guidance]

**Output Format:** [HTML/CSS snippets, Markdown documents, or text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Token-driven web/UI with dark-mode and CJK support; email uses compatible static styles.]

## Skill Version(s):

2.9.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
