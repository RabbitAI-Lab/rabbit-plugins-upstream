## Description: <br>
Searches WeChat Official Accounts for trending cultural tourism articles, ranks them by read count, clusters them by topic, and generates an HTML report with category statistics and links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content operators, tourism marketers, and researchers use this skill to monitor WeChat cultural tourism trends, compare location or topic coverage, and produce recurring HTML reports for daily review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Subscription mode creates persistent scheduled tasks and has unsafe handling of shell commands and API keys. <br>
Mitigation: Prefer one-off report generation until subscription command handling is fixed and API keys are no longer written into scheduled-task files. <br>
Risk: Generated HTML reports may include unescaped fetched content. <br>
Mitigation: Use a scoped output directory, review reports before sharing, and avoid opening reports in sensitive browser sessions. <br>
Risk: The skill may open the generated browser report automatically. <br>
Mitigation: Run it only in environments where opening local reports is acceptable, and make browser opening an explicit user choice where possible. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/cultural-tourism-wechat-feed) <br>
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFoxHub](https://redfox.hk) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Files] <br>
**Output Format:** [Markdown summary with a category table plus a generated HTML report file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY and can generate scheduled daily reports when subscription mode is used.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
