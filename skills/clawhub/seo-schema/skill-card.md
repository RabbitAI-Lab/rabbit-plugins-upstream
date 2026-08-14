## Description:

Detect, validate, and generate Schema.org structured data, with JSON-LD preferred.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO practitioners, and content teams use this skill to inspect pages or provided HTML for structured data, validate rich-result eligibility, and generate paste-ready JSON-LD markup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated structured data may be inaccurate or incomplete for the target page.

Mitigation: Review generated JSON-LD against the live page content and supported rich-result requirements before publishing.

Risk: The skill may generate report or JSON files in the workspace.

Mitigation: Run it only in workspaces where generated SEO reports and schema files are expected.

Risk: Broad activation terms such as schema, structured data, rich results, JSON-LD, and markup may trigger the skill during adjacent SEO tasks.

Mitigation: Confirm the user is asking for structured-data detection, validation, or generation before applying the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/asale-ai/skills/seo-schema)
- [Deprecated Schema.org rich result types (2024-2026)](references/deprecated-types-2024-2026.md)
- [Schema.org](https://schema.org)
- [Google Search: Simplifying our Search rich results](https://developers.google.com/search/blog/2025/06/simplifying-search-results)
- [Google Search: HowTo and FAQ rich result changes](https://developers.google.com/search/blog/2023/08/howto-faq-changes)
- [Google Search: FAQ structured data](https://developers.google.com/search/docs/appearance/structured-data/faqpage)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown reports and JSON-LD snippets, with optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce SCHEMA-REPORT.md and generated-schema.json in the workspace.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
