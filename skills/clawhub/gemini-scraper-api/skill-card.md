## Description:

Sends prompts through Scavio's Gemini API and returns answers, cited URLs, and recommended products for AI visibility analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and brand-monitoring teams use the skill to inspect Gemini answers, citations, and product mentions across prompts and assess AI visibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to Scavio's API and could contain sensitive information.

Mitigation: Avoid sending secrets or sensitive personal data unless the use case and account terms permit it.

Risk: Each answered prompt consumes credits, especially across large prompt lists.

Mitigation: Confirm the scope and expected credit usage before running batches.

Risk: A single variable answer could be mistaken for Gemini's consistent recommendation.

Mitigation: Preserve the returned wording and citations, and use repeated runs when reporting visibility or mention rates.

## Reference(s):

- [Scavio Gemini API documentation](https://scavio.dev/docs/gemini-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=gemini-scraper-api)
- [Scavio API rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=gemini-scraper-api)
- [ClawHub skill release](https://clawhub.ai/scavio-ai/skills/gemini-scraper-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown answer with cited URLs and recommended products from structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers can vary between runs; cited URLs and product details depend on the response.]

## Skill Version(s):

1.0.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
