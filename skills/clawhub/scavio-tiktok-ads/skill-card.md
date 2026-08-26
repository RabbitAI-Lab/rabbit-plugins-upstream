## Description:

Search ads running on TikTok by keyword and/or industry, pull the top-performing ads with a performance highlight, and open one ad in full with its objective, engagement, the countries it ran in, its landing page and a playable video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, developers, and agent builders use this skill to research TikTok ads, competitors, industries, and top-performing creative through Scavio's structured API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends TikTok ad research queries to Scavio and requires a Scavio API key.

Mitigation: Use the skill only when sharing those queries with Scavio is acceptable, and store SCAVIO_API_KEY in an environment variable or secret manager rather than source control.

Risk: Each documented TikTok Ads endpoint call consumes one Scavio API credit.

Mitigation: Confirm the requested search or detail lookup before running API calls, and monitor credits_remaining in API responses.

Risk: Playable video and cover URLs are short-lived and search or top results do not include playable video files.

Mitigation: Call the detail endpoint when a playable video URL is needed and fetch returned media promptly instead of storing signed URLs.

## Reference(s):

- [Scavio TikTok Ad Library API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=tiktok-ad-library-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=tiktok-ad-library-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-tiktok-ads)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with Python and curl examples for JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY and returns structured TikTok ad data from Scavio endpoints.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
