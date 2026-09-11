## Description:

Look up TikTok profiles, search videos and users, explore hashtags, read comments, and traverse the social graph (followers/followings). Eleven endpoints, all at 1 credit per request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to retrieve structured TikTok profile, video, comment, hashtag, follower, and following data through Scavio's API for trend research, creator analysis, and short-form video context gathering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok lookup parameters and the Scavio API key are sent to Scavio when the skill is used.

Mitigation: Use the skill only when that data sharing is acceptable, keep SCAVIO_API_KEY in a secret store or environment variable, and avoid placing it in source files or prompts.

Risk: Comment and follower/following endpoints can enable bulk profiling or surveillance if used indiscriminately.

Mitigation: Limit collection to lawful, authorized, and proportionate research tasks and avoid unnecessary pagination or aggregation of personal data.

Risk: The optional LangChain package adds a package-installation dependency outside the direct HTTPS examples.

Mitigation: Prefer the documented direct HTTPS API calls unless the optional package has been reviewed or isolated in the deployment environment.

## Reference(s):

- [Scavio TikTok API documentation](https://scavio.dev/docs/tiktok-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=tiktok-scraper-api)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/tiktok-scraper-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON-oriented API examples and shell setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; endpoints return structured JSON from Scavio and each TikTok request is documented as costing 1 credit.]

## Skill Version(s):

1.0.3 (source: server release evidence; artifact frontmatter reports 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
