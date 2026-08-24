## Description:

Meta Ad Library search by keyword, Facebook Page id or ad archive id, returning the full ad creative, run dates, the Meta platforms each ad ran on, and spend, reach and impressions on political and issue ads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketing analysts, and research teams use this skill to search public Facebook and Instagram ads by keyword, Facebook Page id, or ad archive id. It helps agents retrieve structured ad creative, run dates, platform placement, cursor pagination, and political or issue ad disclosure data through Scavio's Meta Ad Library API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires a Scavio API key and sends Meta ad search terms, page IDs, and archive IDs to Scavio.

Mitigation: Confirm that this data sharing is acceptable before use and load the API key from an environment variable or secret store.

Risk: Unbounded cursor pagination can consume Scavio credits.

Mitigation: Set a page or credit budget before crawling and stop when has_next_page is false.

Risk: Commercial ad spend and reach fields may be null because Meta publishes those figures for political and issue ads only.

Mitigation: Do not treat null spend or reach as zero; explain the disclosure limitation when reporting results.

## Reference(s):

- [Scavio Meta Ads Search Documentation](https://scavio.dev/docs/meta-ads-search?utm_source=clawhub&utm_medium=skill&utm_campaign=meta-ad-library-api)
- [Scavio API Key Setup](https://scavio.dev/?utm_source=clawhub&utm_medium=skill&utm_campaign=meta-ad-library-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=clawhub&utm_medium=skill&utm_campaign=meta-ad-library-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, API calls, JSON]

**Output Format:** [Markdown guidance with shell commands, code examples, API request bodies, and structured JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and uses cursor pagination for multi-page ad searches.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
