## Description: <br>
Fetch trending topics from X (Twitter), analyze user interests from natural language, retrieve top hot topics per domain, and summarize background, key opinions, and controversies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiangsier-xyz](https://clawhub.ai/user/jiangsier-xyz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they want an agent to find recent X/Twitter discussions, map a prompt to topic keywords, fetch relevant English posts, and summarize topic background, opinions, and controversies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an X API bearer token and sends selected topic keywords from user prompts to X/Twitter. <br>
Mitigation: Use a scoped token, avoid submitting sensitive prompt content as search keywords, and enable the skill only where sending those queries to X is acceptable. <br>
Risk: Returned posts may not represent verified or platform-wide trends. <br>
Mitigation: Present summaries as analysis of recent returned English posts and avoid treating them as authoritative trend measurements. <br>
Risk: The Tweepy dependency is declared with a lower-bound version. <br>
Mitigation: Pin Tweepy to an approved version before use in stricter or reproducible environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jiangsier-xyz/skills/x-hots) <br>
- [X Developer Portal](https://developer.twitter.com/en/portal/dashboard) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Analysis, Guidance] <br>
**Output Format:** [Markdown summaries with shell command examples and JSON result structures] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an X API bearer token; script results are limited by X API access, recent-search scope, English-language filtering, and rate limits.] <br>

## Skill Version(s): <br>
1.5.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
