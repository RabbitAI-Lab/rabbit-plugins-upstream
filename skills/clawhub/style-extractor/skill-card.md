## Description:

Extracts a complete UI design system from a URL, screenshot, or frontend project source and packages it as a reusable WorkBuddy style skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[namepain](https://clawhub.ai/user/namepain)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and UI migration teams use this skill to audit visual style from webpages, screenshots, or source projects, then produce governed three-layer design tokens and a reusable style skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can fetch user-provided webpages and inspect style-related files in projects selected by the user.

Mitigation: Use it only with URLs, screenshots, and repositories intended for analysis; avoid private or internal sources containing secrets unless that analysis is intentional.

Risk: Screenshot-based and pattern-based extraction can include inferred or assumed design-token values.

Mitigation: Review evidence grades and known gaps before adopting generated tokens or using the packaged style skill for production UI work.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/namepain/style-extractor)
- [ClawHub skill page](https://clawhub.ai/namepain/skills/style-extractor)
- [Extraction checklist](artifact/references/extraction-checklist.md)
- [Output format specification](artifact/references/output-format.md)
- [Validation checklist](artifact/references/validation-checklist.md)
- [Common pitfalls](artifact/references/common-pitfalls.md)
- [Kryon design-token article](https://mp.weixin.qq.com/s/SwzGgLLW9RC2fTDw1cWRZQ)
- [skillui package](https://www.npmjs.com/package/skillui)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown files with YAML frontmatter, design-token tables, code blocks, and validation notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated style skills include SKILL.md plus references for colors, typography, spacing, components, and known gaps.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter declares 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
