## Description:

Search ads running on TikTok by keyword and/or industry, pull the top-performing ads with a performance highlight, and open one ad in full with its objective, engagement, the countries it ran in, its landing page and a playable video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, marketers, and ad researchers use this skill to query Scavio's TikTok ad-library API for competitor ads, top-performing ads, ad metrics, landing pages, and playable video details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests require a Scavio API key and may expose credentials if the key is hard-coded or committed.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store and keep it out of source control.

Risk: Each TikTok Ads endpoint consumes 1 Scavio API credit.

Mitigation: Confirm the user's intent and expected query scope before making API calls that spend credits.

Risk: Returned video and cover URLs have short expirations.

Mitigation: Use returned media URLs promptly and avoid presenting them as durable archival links.

Risk: The agent could overstate ad data beyond the API response.

Mitigation: Return only API-provided ad copy, brands, metrics, landing pages, and media details.

## Reference(s):

- [Scavio API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=tiktok-ad-library-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=tiktok-ad-library-api)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/tiktok-ad-library-api)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON API responses and example Python and curl commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each endpoint returns structured JSON and consumes 1 Scavio API credit.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
