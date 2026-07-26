## Description: <br>
Assists bid teams in estimating win probability for a specific tender by analyzing buyer history, likely competitors, fit, pricing signals, and bid risks from procurement data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External bid, sales, and business development teams use this skill to decide whether to pursue a tender, how to price competitively, and which competitors or buyer patterns may affect win probability. It is intended for decision support and produces a traceable report based on available procurement data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may create persistent credentials and read a stored API key from the local environment or configuration. <br>
Mitigation: Use a preconfigured ZLBX_API_KEY where possible, keep credentials out of chat, and review local credential storage before installation. <br>
Risk: Automatic trial registration can transmit platform, CPU architecture, and a hashed MAC identifier. <br>
Mitigation: Only approve auto-registration after accepting that data transfer, or configure ZLBX_API_KEY manually to bypass registration. <br>
Risk: Generated HTML reports may contain sensitive commercial analysis and signed source links that can open without a normal login. <br>
Mitigation: Treat reports as confidential business documents, limit sharing, and remove or expire signed links before broader distribution. <br>
Risk: Bid recommendations can be misleading if procurement data is incomplete, stale, or not representative of the tender. <br>
Mitigation: Review the report's data gaps, date ranges, and cited records before making commercial decisions. <br>
Risk: Analysis involving real companies or public agencies can create reputational or legal risk if inferred signals are phrased as accusations. <br>
Mitigation: Keep facts and inferences separate, use neutral signal-based wording, and have a human review sensitive claims before sharing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/bid-win-rate-analyzer) <br>
- [Workflow Guide](references/workflow.md) <br>
- [API Quick Reference](references/api-quick.md) <br>
- [Report Template](references/report-template.md) <br>
- [Auto-Registration Reference](references/auto-register.md) <br>
- [ZhiLiaoBiaoXun API](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool}) <br>
- [ZhiLiaoBiaoXun Trial and Account Portal](https://ai.zhiliaobiaoxun.com/?ch=s67) <br>
- [ZhiLiao Business Intelligence Portal](https://agent.zhiliaobiaoxun.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, guidance] <br>
**Output Format:** [Markdown decision report with an optional self-contained HTML report file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include citation details and signed source links returned by the procurement data API; complete mode may write an HTML report under ~/zlbx-bid-decision-files/.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
