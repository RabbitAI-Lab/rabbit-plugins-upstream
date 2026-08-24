## Description:

Researches social-media profiles, posts, and engagement across Instagram, TikTok, Threads, Bluesky, X, Pinterest, LinkedIn, Facebook, and Reddit via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and social-media researchers use this skill to query public profiles, posts, engagement, searches, trending topics, competitor activity, influencer signals, and brand mentions through documented Crawlora API endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send the Crawlora API key to an overridden API host.

Mitigation: Keep CRAWLORA_API_BASE unset unless the alternate host is intentionally trusted.

Risk: The helper script can call paths or POST bodies beyond the stated social-media research purpose.

Mitigation: Prefer only the documented social-media endpoints in reference/endpoints.md.

Risk: Social-media handles, post IDs, search terms, and the API key are sent through the Crawlora helper.

Mitigation: Use the skill only when those inputs are appropriate to share with Crawlora and keep CRAWLORA_API_KEY out of committed files and query strings.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/social-media-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON API responses with optional Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses public social-media data available through Crawlora endpoints.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
