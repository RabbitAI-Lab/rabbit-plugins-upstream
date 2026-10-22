## Description:

Guides agents in using ScrapeBadger APIs to retrieve web, search, marketplace, social media, real estate, and AI answer data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[0xghostcasper](https://clawhub.ai/user/0xghostcasper)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to select ScrapeBadger endpoints and retrieve public web, commerce, search, social media, and property data, or cited AI answers, through an API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested search terms, URLs, images, screenshots, and prompts are sent to ScrapeBadger; ChatGPT and Perplexity requests may also reach those services.

Mitigation: Do not submit secrets, private URLs, regulated data, or proprietary prompts unless approved for your environment.

Risk: Requests use an API key and may incur usage credits.

Mitigation: Keep the API key in an environment variable, avoid exposing it in outputs, and review endpoint credit costs before use.

## Reference(s):

- [ScrapeBadger documentation](https://docs.scrapebadger.com)
- [ScrapeBadger skill on ClawHub](https://clawhub.ai/0xghostcasper/skills/scrapebadger)
- [ScrapeBadger dashboard](https://scrapebadger.com/dashboard?utm_source=openclaw-skill&utm_medium=referral)
- [ScrapeBadger MCP server](https://mcp.scrapebadger.com/mcp)

## Skill Output:

**Output Type(s):** [API calls, Text, Markdown, JSON, Guidance]

**Output Format:** [Endpoint-specific API responses and plain-text or Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCRAPEBADGER_API_KEY; requests may consume credits.]

## Skill Version(s):

1.8.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
