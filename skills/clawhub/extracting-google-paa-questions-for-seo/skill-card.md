## Description:

Extracts Google People Also Ask questions for SEO content planning using apidojo's Google Search scraper on Apify, returning PAA questions, SERP position, related keywords, and content structure recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External SEO strategists, content writers, and editors use this skill to collect Google People Also Ask questions for keywords, classify intent, score content opportunity, and produce an SEO content brief.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SEO search terms are sent to Apify and may contain confidential client, campaign, or regulated-topic information.

Mitigation: Use non-sensitive keywords, avoid confidential or regulated terms, and confirm the data-sharing posture with the client or data owner before running searches.

Risk: The REST fallback pattern places APIFY_TOKEN in a URL parameter, which can be exposed through shell history, process listings, logs, or shared command snippets.

Mitigation: Prefer the MCP/helper flow or another secure authorization method, store APIFY_TOKEN in an environment variable or secrets manager, and avoid pasting tokenized URLs into chats or tickets.

Risk: Google PAA availability and results can vary by keyword, region, language, device mode, and page depth, so a single run may produce incomplete or misleading content priorities.

Mitigation: Run keyword variants, record country, language, mobile, and pagination settings, deduplicate similar questions, and review the final brief before using it for content planning.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/extracting-google-paa-questions-for-seo)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown brief with tables, ranked question lists, FAQ suggestions, and optional shell commands or API payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SERP query counts, unique PAA counts, intent labels, opportunity scores, and featured snippet flags.]

## Skill Version(s):

1.0.0 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
