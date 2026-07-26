## Description: <br>
Fetch trending topics from X (Twitter). Analyze user interests from natural language, retrieve top hot topics per domain, and summarize background, key opinions, and controversies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiangsier-xyz](https://clawhub.ai/user/jiangsier-xyz) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to identify current X/Twitter topics for a stated interest area and summarize the topic background, common opinions, and controversies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an X API bearer token, and mishandling that token could expose account access. <br>
Mitigation: Store the token in a secure environment or secret manager, avoid committing it to files, and rotate it if exposure is suspected. <br>
Risk: Chosen search keywords are sent to X and may reveal sensitive interests or investigative intent. <br>
Mitigation: Avoid private or sensitive queries and use only search terms suitable for processing by the X API. <br>
Risk: Recent public posts can be incomplete, misleading, or volatile as evidence for public opinion. <br>
Mitigation: Treat generated summaries as situational context and verify important claims against primary sources before acting on them. <br>


## Reference(s): <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>
- [Tweepy documentation](https://docs.tweepy.org/) <br>
- [X Developer Portal](https://developer.twitter.com/en/portal/dashboard) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries with supporting JSON from the X API query script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an X API bearer token and user-selected search keywords; defaults to English, non-retweet recent posts.] <br>

## Skill Version(s): <br>
1.4.1 (source: frontmatter, changelog, ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
