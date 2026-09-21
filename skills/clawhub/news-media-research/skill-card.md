## Description:

Researches public news from major international, US, business, and policy publishers through the Crawlora API -- headlines, article text, search, live coverage, and section/topic archives -- returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, researchers, and developers use this skill to retrieve publisher-specific public headlines, article content, search results, live coverage snapshots, and section or topic archives as normalized JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the Crawlora API key and requested public article URLs, publisher routes, and search terms to a third-party service.

Mitigation: Use it only for approved public-news research and avoid secrets, internal-only URLs, personal data, or confidential research queries unless third-party sharing is approved.

Risk: Publisher feeds and live-story routes are bounded snapshots and may omit subscriber-only, metered, challenged, video, podcast, or live-blog content.

Mitigation: Preserve source URLs and timestamps, avoid presenting a feed as complete coverage, and use comparison-oriented research workflows when synthesis across outlets is needed.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API service](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/news-media-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON responses from Crawlora with Markdown instructions and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and supports documented GET routes for public publisher content.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
