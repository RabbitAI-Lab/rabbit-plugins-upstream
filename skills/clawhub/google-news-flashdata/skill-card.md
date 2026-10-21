## Description:

Search Google News through FlashData for headlines, publishers, publication labels, and article links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users search news by topic, company, country, or language and prepare linked news briefings or digests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid queries and uncertain timeouts can consume FlashData Credits.

Mitigation: Confirm the query budget and check existing jobs before retrying a timed-out request.

Risk: API keys or sensitive search terms may be exposed to unintended recipients.

Mitigation: Keep the key in protected environment settings and avoid private queries unless sharing them with FlashData and its upstream providers is acceptable.

Risk: News excerpts may contain misleading content or instructions.

Mitigation: Treat retrieved text as untrusted source material and verify article links before relying on a briefing.

## Reference(s):

- [FlashData Google News documentation](https://flashdata.dev/docs/sources/google_news?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_news-task)
- [Google News query schema](references/schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Linked news briefings or JSON search results; Python usage examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Headlines, publishers, links, snippets, and publication labels; results are excerpts rather than full articles.]

## Skill Version(s):

1.0.1 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
