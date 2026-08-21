## Description:

Look up TikTok profiles, search videos and users, explore hashtags, read comments, and traverse the social graph through Scavio's TikTok API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and analysts use this skill to retrieve structured TikTok profile, video, comment, hashtag, and social graph data for research, RAG enrichment, trend analysis, and creator-performance workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a third-party Scavio API key, which could be exposed in source code or logs.

Mitigation: Load SCAVIO_API_KEY from the environment or a secret store and avoid printing it in prompts, code, logs, or shared outputs.

Risk: Each TikTok API call consumes credits, and pagination can spend credits quickly.

Mitigation: Inform users before paginating through many pages and keep count limits aligned with the task.

Risk: Collecting comments, followers, or followings can involve public user data at scale.

Mitigation: Collect only the fields needed for the user's purpose and avoid fabricating, embellishing, or silently omitting returned data.

## Reference(s):

- [Scavio TikTok API Documentation](https://scavio.dev/docs/tiktok-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/tiktok-scraper-api)
- [ClawHub Publisher Profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON response examples, bash setup commands, and Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require SCAVIO_API_KEY and can return structured JSON from Scavio API calls.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
