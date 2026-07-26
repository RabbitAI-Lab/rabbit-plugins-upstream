## Description: <br>
Queries LinkFox Google Trends keyword trend data to analyze normalized search interest over time by keyword, supported region, and optional date range. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to request Google Trends normalized search-interest data for keyword and market trend analysis across supported regions and date ranges. It helps an agent present trend values, peaks, troughs, seasonality, and relevant caveats for the selected keyword. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: LinkFox may receive keyword queries, API credentials, session or app metadata, and possible feedback content. <br>
Mitigation: Use an approved LinkFox account and API key, avoid sensitive keywords or feedback content, and keep the gateway pinned to the official LinkFox host. <br>
Risk: Authentication or quota failures can lead to a remote onboarding-skill installation path. <br>
Mitigation: Review or disable the remote onboarding path before deployment, and require explicit user authorization before downloading or installing onboarding assets. <br>
Risk: Responses and cache entries are retained in local linkfox data directories. <br>
Mitigation: Confirm that saved response and cache directories are acceptable for the workspace, and clean them according to local data retention policy. <br>


## Reference(s): <br>
- [谷歌趋势-关键词趋势信息 API 参考](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-google-trend-get-trend-by-keys) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses; full responses are saved as JSON files and small responses may print inline.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts one keyword plus optional region and date range; uses a 24-hour local cache and summarizes responses larger than 8 KB unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
