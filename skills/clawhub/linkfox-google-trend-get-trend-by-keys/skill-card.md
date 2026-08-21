## Description:

Google Trends keyword trend analysis for comparing normalized search interest by keyword, region, and custom date range.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Google Trends-style keyword interest, compare regional or seasonal patterns, and present normalized trend values for market or keyword research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends keyword requests and possible feedback content to LinkFox services.

Mitigation: Install only if third-party processing by LinkFox is acceptable for the intended queries, and avoid submitting sensitive keywords or feedback content.

Risk: The skill uses API keys and includes phone/SMS onboarding flows for account access.

Mitigation: Prefer temporary environment variables or a secret manager for API keys, and run onboarding commands only when explicitly intended.

Risk: The skill can initiate billing flows and credit-consuming API calls.

Mitigation: Confirm expected credit use before repeated calls and review any payment or plan-selection command before execution.

Risk: The skill writes query outputs and cache data under a local linkfox directory.

Mitigation: Clear local linkfox output and cache directories after use when queries or results are sensitive.

## Reference(s):

- [谷歌趋势-关键词趋势信息 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-google-trend-get-trend-by-keys)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API results and saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Google Trends values are normalized to a 0-100 scale; each tool call handles one keyword and may consume LinkFox credits.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
