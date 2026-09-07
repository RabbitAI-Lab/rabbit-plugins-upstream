## Description:

Search ads running on TikTok by keyword and/or industry, pull the top-performing ads with a performance highlight, and open one ad in full with its objective, engagement, countries, landing page, and playable video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing researchers use this skill to find TikTok ads for brands, competitors, keywords, products, or industries and inspect returned performance and creative details from Scavio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send query parameters and the Scavio API key to Scavio and consume account credits.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store, review broad or repeated searches before running them, and monitor usage.

Risk: Search and top results do not include playable video files, and returned media links can expire quickly.

Mitigation: Call the detail endpoint for playable video URLs and fetch returned media promptly instead of storing signed links.

Risk: Ad copy, brands, metrics, landing pages, and countries can be misrepresented if an agent fills gaps from assumption.

Mitigation: Return only values present in the API response and state when requested fields are unavailable.

## Reference(s):

- [Scavio documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=tiktok-ad-library-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=tiktok-ad-library-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/tiktok-ad-library-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python and curl examples; API responses are structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Scavio API calls consume credits and returned media URLs may expire quickly.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
