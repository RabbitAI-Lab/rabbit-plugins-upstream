## Description:

Search ads running on TikTok by keyword and/or industry, pull the top-performing ads with a performance highlight, and open one ad in full with its objective, engagement, the countries it ran in, its landing page and a playable video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing researchers use this skill to search TikTok ads, compare competitor creatives, retrieve top-performing ads, and inspect a specific ad's objective, engagement, countries, landing page, and playable video when the API returns it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API calls use the user's SCAVIO_API_KEY and may consume Scavio credits.

Mitigation: Keep the key out of source control, load it from the environment or a secret store, and verify Scavio pricing and terms before use.

Risk: TikTok ad data, metrics, landing pages, and media URLs can be misrepresented if an agent extrapolates beyond API results.

Mitigation: Return only values present in API responses, do not fabricate ad copy or engagement metrics, and call the detail endpoint before claiming a playable video URL.

Risk: Playable video and cover URLs are short-lived signed links.

Mitigation: Fetch media promptly and avoid treating signed URLs as durable records.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/tiktok-ad-library-api)
- [Scavio API Documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=tiktok-ad-library-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=tiktok-ad-library-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API examples and structured JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY for authenticated Scavio API calls; each documented TikTok Ads endpoint costs 1 credit.]

## Skill Version(s):

1.0.3 (source: server evidence release.version; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
