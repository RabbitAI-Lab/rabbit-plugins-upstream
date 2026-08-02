## Description: <br>
公众号账号诊断工具对任意公众号账号进行四维度量化评分，包括内容健康度、用户活跃度、内容核心数据和运营规范性，并对标行业平均水平输出可落地的运营优化建议。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users such as WeChat official account owners, social media operators, MCN agencies, brands, and content creators use this skill to diagnose account health, benchmark peers, and plan content or operations improvements from Redfox API data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles a Redfox API key and may suggest persistent shell configuration. <br>
Mitigation: Use a dedicated Redfox API key and review any proposed environment-variable changes before allowing the agent to modify shell startup files. <br>
Risk: Queried WeChat account names, IDs, and returned metrics may be sent to Redfox and stored in local output files. <br>
Mitigation: Confirm the account data is appropriate to send to Redfox, and review or delete generated raw data, structured JSON, and HTML report files after use. <br>
Risk: Remote sync, subscription, calendar reminder, and report-file creation behavior can persist beyond a single diagnostic request. <br>
Mitigation: Explicitly confirm each sync, subscription, reminder, or file-generation action before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/redfox-data/skills/wechat-account-analyzer) <br>
- [Redfox Hub](https://redfox.hk/) <br>
- [Core Workflow](references/core_workflow.md) <br>
- [Workflow Guide](references/workflow_guide.md) <br>
- [API Guide](references/api_guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, HTML files, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown diagnostic reports, structured JSON data, optional HTML reports, and setup commands or configuration guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports follow a fixed five-section diagnostic structure and may save raw API data, structured report data, and generated HTML report files locally.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
