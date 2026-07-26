## Description: <br>
Analyzes WeChat Official Accounts across reading volume, engagement rate, update frequency, and RedFox Index, benchmarks them against industry averages, and produces actionable optimization recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External WeChat account owners, new-media operators, brand teams, and MCN agencies use this skill to diagnose WeChat Official Account performance, compare peer accounts, and plan data-driven content and operations improvements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queried WeChat account identifiers and returned account data are sent to and received from redfox.hk. <br>
Mitigation: Use the skill only for accounts you are comfortable querying through RedFox, and confirm the API key source, scope, expiry, and revocation path before use. <br>
Risk: The skill handles REDFOX_API_KEY and may read shell profile files when the environment variable is not set. <br>
Mitigation: Configure the key through a secure environment or secret mechanism, avoid pasting it into prompts or files, and rotate it if exposed. <br>
Risk: Returned data and generated reports can be stored locally as raw JSON, structured report JSON, and HTML files. <br>
Mitigation: Review generated output files before sharing or committing them, and remove local reports that contain sensitive account data. <br>
Risk: Subscription and sync flows can create delayed rechecks or reminder tasks. <br>
Mitigation: Enable follow-up sync or calendar reminders only after explicit user consent, and review any created task before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/wechat-account-analyzer) <br>
- [Publisher profile](https://clawhub.ai/user/redfox-data) <br>
- [Core workflow](references/core_workflow.md) <br>
- [API guide](references/api_guide.md) <br>
- [Workflow guide](references/workflow_guide.md) <br>
- [RedFoxHub](https://redfox.hk/) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files, Guidance] <br>
**Output Format:** [Five-section Markdown diagnostic report, structured JSON status and report data, and optional HTML report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY, queries redfox.hk with account identifiers, and may write raw data, report data, and HTML files locally.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
