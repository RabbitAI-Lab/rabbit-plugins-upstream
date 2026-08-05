## Description:

Generates professional single-file HTML technical documentation and proposals with international and Chinese technical-spec design systems, syntax highlighting, responsive layouts, and reusable SVG document components.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fbbyqsyea](https://clawhub.ai/user/fbbyqsyea)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical writers, and solution engineers use this skill to turn technical content, architecture analysis, workflow explanations, research reports, and proposals into polished single-file HTML documents with CSS and diagram guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML may include active JavaScript and browser-executed behavior.

Mitigation: Review generated documents before opening or sharing, sanitize untrusted input, and remove scripts that are not needed for the document.

Risk: Generated documents may reference remote fonts or CDN-hosted assets.

Mitigation: Replace remote fonts and libraries with local or approved internal assets when privacy, offline use, or strict supply-chain control matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fbbyqsyea/skills/premium-html-studio)
- [Skill instructions](artifact/SKILL.md)
- [International CSS design system](artifact/templates/css-system.css)
- [Chinese technical-spec CSS design system](artifact/templates/css-system-cn.css)
- [Reusable SVG components](artifact/templates/svg-components.svg)
- [Prism.js syntax highlighting](https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js)
- [Mermaid diagrams](https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js)
- [FlexSearch client-side search](https://cdn.jsdelivr.net/npm/flexsearch@0.7.31/dist/flexsearch.bundle.js)
- [Schema.org structured data](https://schema.org)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with HTML, CSS, JavaScript, and SVG code snippets for single-file HTML documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include browser-executable HTML and optional references to remote fonts or CDN-hosted libraries.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
