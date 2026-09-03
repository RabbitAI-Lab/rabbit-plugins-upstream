## Description:

Search ads running on TikTok by keyword and/or industry, pull the top-performing ads with a performance highlight, and open one ad in full with its objective, engagement, the countries it ran in, its landing page and a playable video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing researchers use this skill to query Scavio's TikTok ads endpoints for competitor ads, top-performing ads, ad details, engagement metrics, landing pages, and playable video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requests to Scavio as a third-party service and consumes API credits for each TikTok Ads endpoint call.

Mitigation: Use it only when third-party Scavio API use is acceptable, monitor credit usage, and top up only when needed.

Risk: SCAVIO_API_KEY is required for authenticated requests.

Mitigation: Store the key in an environment variable or secret store and avoid committing it to source code.

Risk: Search and top results include cover images but not playable videos, and returned video or cover URLs can expire quickly.

Mitigation: Call the detail endpoint for playable video URLs and fetch time-limited URLs promptly instead of storing them.

## Reference(s):

- [Scavio API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=tiktok-ad-library-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=tiktok-ad-library-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/tiktok-ad-library-api)
- [Scavio publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, API calls, JSON]

**Output Format:** [Markdown guidance with inline shell, Python, curl, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses use structured JSON and consume one Scavio credit per TikTok Ads endpoint call.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
