## Description:

Searches Google News through FlashData for headlines, publishers, publication labels, links, and snippets to support topic research and news digests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

External users and researchers use this skill to find news coverage by topic, company, country, or language and prepare sourced briefings or digests with article links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: News searches use paid FlashData Credits; a timed-out request may still incur a charge.

Mitigation: Agree on a budget, run only needed requests, and check existing jobs rather than automatically resubmitting timed-out requests.

Risk: The skill needs a FlashData API key and sends queries to FlashData and upstream providers.

Mitigation: Keep the key in protected environment configuration, avoid sensitive search terms, and review the pinned package before use if needed.

Risk: Retrieved news text may be misleading or contain instructions directed at the agent.

Mitigation: Treat retrieved text as untrusted source material and preserve article links and date labels for verification.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rocosen/skills/google-news-flashdata)
- [FlashData Google News documentation](https://flashdata.dev/docs/sources/google_news?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_news-task)
- [FlashData Google News CLI package](https://www.npmjs.com/package/@flashdata-dev/google-news)
- [Query schema](artifact/references/schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Sourced news briefing or digest with headlines, publishers, article links, and original date labels]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search excerpts rather than full articles; returned counts may be lower than requested and date labels may be relative.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
