## Description:

Queries recent Google Trends topics through LinkFox for a selected time window and supported region, then helps summarize trending searches, relative search volume, and breakout changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to discover recent Google search trends across supported markets, compare relative interest, and identify fast-rising topics for regional trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trend requests, API credentials, and session metadata are sent to LinkFox endpoints.

Mitigation: Review the configured LINKFOX_* endpoint variables and use only credentials intended for LinkFox trend queries.

Risk: Onboarding can collect phone/SMS login data and initiate billing or order flows when credits are insufficient.

Mitigation: Use phone registration or payment onboarding only when the user explicitly wants a LinkFox account or paid credits.

Risk: The skill stores full responses and cache files under the local workspace.

Mitigation: Run it from an appropriate workspace and review or delete saved LinkFox response files when the trend data should not persist.

Risk: Automatic feedback reporting can send feedback content to LinkFox.

Mitigation: Avoid including sensitive user or project details in feedback and review the feedback behavior before deployment.

## Reference(s):

- [Skill release page](https://clawhub.ai/linkfox-ai/skills/linkfox-google-trend-get-trend-by-time)
- [谷歌趋势-时下流行 API 参考](artifact/references/api.md)
- [解决认证和积分问题](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries and tables, JSON API responses, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved as local JSON files; large responses may be summarized unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
