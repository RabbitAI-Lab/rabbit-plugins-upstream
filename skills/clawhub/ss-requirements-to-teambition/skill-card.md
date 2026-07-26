## Description: <br>
从 SaleSmartly 客服会话中采集带标签的对话，经 AI 分析提取需求或 BUG，并创建或更新 Teambition 任务。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zpeng6834-arch](https://clawhub.ai/user/zpeng6834-arch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Support, product, and operations teams use this skill to convert tagged SaleSmartly customer conversations into structured Teambition follow-up tasks for AI product requirements and bugs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A packaged SaleSmartly API key may expose a workspace if reused. <br>
Mitigation: Remove and rotate the packaged key before installation, then replace scripts/config.json with a private key controlled by the installing workspace administrator. <br>
Risk: Raw customer support conversations are written to local JSON files and copied into Teambition tasks. <br>
Mitigation: Confirm customer-data handling policies permit this transfer, restrict access to generated files and Teambition projects, and rely on the skill's short retention window or a stricter local retention policy. <br>
Risk: Scheduled automation can create or update Teambition tasks without a human reading each conversation first. <br>
Mitigation: Review generated task summaries before enabling cron and run the workflow with least-privilege SaleSmartly and Teambition credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zpeng6834-arch/skills/ss-requirements-to-teambition) <br>
- [Teambition MCP setup guide](artifact/references/tb_mcp_setup.md) <br>
- [Configuration field guide](artifact/references/config_fields.md) <br>
- [Analysis and task creation template](artifact/references/analysis_template.md) <br>
- [Execution guide](artifact/references/execution_guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON task payloads, shell commands, and local JSON session files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can create or update Teambition tasks through MCP and write SaleSmartly session exports when configured.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
