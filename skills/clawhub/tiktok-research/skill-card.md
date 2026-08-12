## Description:

Researches TikTok profiles, videos, hashtags, search, trending content, and Creative Center ads intelligence via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and marketing researchers use this skill to gather public TikTok profile, video, hashtag, search, trending, and Creative Center ad intelligence through Crawlora instead of direct scraping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok handles, video IDs, keywords, ad research targets, and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only for public or non-sensitive research, avoid confidential investigations or sensitive personal data, and keep the API key in CRAWLORA_API_KEY rather than hardcoding it.

Risk: CRAWLORA_API_BASE can redirect requests to a different endpoint if set.

Mitigation: Set CRAWLORA_API_BASE only when the destination is trusted and expected for the task.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/tiktok-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands; Crawlora API calls return JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; list and search endpoints may be cursor-paginated.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
