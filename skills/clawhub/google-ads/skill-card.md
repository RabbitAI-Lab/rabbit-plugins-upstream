## Description: <br>
Query, audit, and optimize Google Ads campaigns through API operations with the google-ads Python SDK or browser automation for users without API access. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jdrhyne](https://clawhub.ai/user/jdrhyne) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Marketing teams, performance marketers, and developers use this skill to inspect Google Ads performance, identify wasted spend and conversion tracking issues, and prepare campaign, keyword, report, and budget actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose sensitive Google Ads account data and credential material through API configuration files, environment variables, browser sessions, reports, or logs. <br>
Mitigation: Use only Google Ads accounts the agent is authorized to access, keep credentials local, and avoid printing credential files, tokens, reports, or account details into chat or logs unless explicitly needed. <br>
Risk: The skill includes live campaign-changing workflows such as pausing campaigns or keywords, changing budgets, exporting data, sending reports to Google Sheets, or scheduling emails. <br>
Mitigation: Require explicit user confirmation before any budget, pause, keyword, export, download, Google Sheets, or email-scheduling action, and verify the selected account and date range before acting. <br>


## Reference(s): <br>
- [Google Ads API Setup](references/api-setup.md) <br>
- [Google Ads Browser Automation Workflows](references/browser-workflows.md) <br>
- [Google Ads web interface](https://ads.google.com/aw/) <br>
- [ClawHub release page](https://clawhub.ai/jdrhyne/skills/google-ads) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports and recommendations with inline Python, YAML, shell commands, and browser workflow steps.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include proposed Google Ads API queries, browser actions, report exports, and campaign mutations; sensitive account-changing actions require explicit confirmation.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
