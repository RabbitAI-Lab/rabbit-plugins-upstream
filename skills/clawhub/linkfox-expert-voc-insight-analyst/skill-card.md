## Description:

Amazon review VOC insight analyst for structured analysis of audiences, use scenarios, positive feedback, negative feedback, unmet needs, and purchase motivations from ASIN, listing, or review data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and agents use this skill to turn Amazon competitor review, ASIN, title, and bullet-point inputs into a structured VOC report. The skill can also fetch supporting LinkFox ecommerce data and write longer Markdown reports when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package is broader than a VOC review analyst and includes ecommerce automation, scheduling, file upload, payment, and skill-creation capabilities.

Mitigation: Install only when the full LinkFox ecommerce automation bundle is intended, and require explicit confirmation before scheduling, billing, payment, or skill-creation actions.

Risk: Supporting tools can use API credentials and call remote LinkFox services.

Mitigation: Verify the LinkFox gateway configuration before use and keep API keys scoped to the minimum required access.

Risk: File upload behavior can produce public upload URLs.

Mitigation: Do not upload private or sensitive files unless the user has explicitly accepted public-link exposure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-voc-insight-analyst)
- [Root skill definition](artifact/SKILL.md)
- [Amazon reviews API reference](artifact/skills/linkfox-amazon-reviews-list/references/api.md)
- [Amazon product detail API reference](artifact/skills/linkfox-amazon-product-detail/references/api.md)
- [Report layout reference](artifact/skills/linkfox-report-generator/references/analysis-layouts.md)
- [Task scheduler API reference](artifact/skills/linkfox-task-scheduler/references/api.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown tables and concise text summaries, with longer reports written to Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primarily Chinese output; requires user-provided review/listing data or authorized LinkFox API access for data retrieval.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
