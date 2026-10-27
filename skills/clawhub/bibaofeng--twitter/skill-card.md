## Description:

Searches and reads X (Twitter) profiles, timelines, mentions, followers, tweet search, trends, lists, communities, and Spaces, and supports posting, liking, unliking, following, and unfollowing after OAuth authorization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bibaofeng](https://clawhub.ai/user/bibaofeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Twitter/X data for social listening, account research, trend tracking, and post discovery. They can also publish posts or perform account engagement through AIsa after OAuth authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change a Twitter/X account by posting, liking, unliking, following, or unfollowing after OAuth authorization.

Mitigation: Confirm the target account, post content, and engagement target before execution, and do not report success unless the relay returns success.

Risk: Twitter/X queries, post content, media uploads, and the AIsa API key are sent to AIsa or to a configured relay URL.

Mitigation: Use a dedicated, revocable API key and configure only trusted HTTPS relay endpoints.

Risk: Status, authorization, or posting output may expose sensitive authorization details or API key material.

Mitigation: Treat those outputs as sensitive and rotate the API key if it appears in logs, transcripts, or shared output.

## Reference(s):

- [AIsa Twitter Engagement](references/engage_twitter.md)
- [AIsa Twitter OAuth](references/post_twitter.md)
- [AIsa API Reference](https://docs.aisa.one/reference/)
- [AIsa](https://aisa.one)
- [ClawHub Twitter Skill](https://clawhub.ai/bibaofeng/skills/twitter)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with shell commands and JSON API or client output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires AISA_API_KEY; optional relay URL and timeout settings are supported.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
