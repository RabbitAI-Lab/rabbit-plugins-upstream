## Description:

SE Ranking AI visibility analyst (extension). Tracks AI Share-of-Voice across ChatGPT, Gemini, Perplexity, AI Overviews, and AI Mode in a single query.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

SEO and growth teams use this skill to query SE Ranking for AI visibility, organic SERP positions, backlink profiles, and competitor keyword gaps. It helps compare brand Share-of-Voice across major AI answer surfaces and report percentages with sample-size confidence notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SEO queries, brand names, keywords, URLs, and backlink targets may be sent to the external SE Ranking API.

Mitigation: Use the skill only for data that may be shared with SE Ranking and review vendor terms before sending sensitive SEO or customer information.

Risk: The skill asks the agent to check a local Claude settings file for SERANKING_API_KEY, which could expose unrelated configuration if handled broadly.

Mitigation: Limit checks to the presence of SERANKING_API_KEY under env and avoid reading or displaying unrelated secrets or settings content.

Risk: SE Ranking API unit accounting can incur usage cost during visibility checks.

Mitigation: Track expected unit use before queries and log spend across vendors as described by the skill.

## Reference(s):

- [SE Ranking API documentation](https://seranking.com/api.html)
- [ClawHub skill page](https://clawhub.ai/asale-ai/skills/seo-seranking)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with percentages, confidence notes, and inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SE Ranking API unit-cost notes and checks for SERANKING_API_KEY configuration.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact metadata reports 2.2.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
