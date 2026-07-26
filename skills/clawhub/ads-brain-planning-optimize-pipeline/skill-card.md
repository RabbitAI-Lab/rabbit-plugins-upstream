## Description: <br>
规划 Agent 新框架中的优化 Pipeline。面向投放改善目标生成优化策略，支持存量对象、待创建草案、策略变量和目标导向优化；诊断只是可选协作依据，不等同于优化本身。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lizejia668-code](https://clawhub.ai/user/lizejia668-code) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Ad operations teams and planning agents use this skill to turn campaign goals and evidence summaries into optimization plans for existing delivery objects, draft launch plans, and strategy variables. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recommendations may affect ad spend or campaign performance if treated as executable changes. <br>
Mitigation: Keep the skill advisory and require a separate execution-confirmation system before budget, bid, audience, creative, or campaign changes. <br>
Risk: The skill depends on ad-account performance summaries, audience insights, creative data, and forecast tools. <br>
Mitigation: Use only authorized account data and review recommendations against campaign policy, data-access rules, and business constraints. <br>
Risk: The skill is written for Chinese customer-facing optimization output. <br>
Mitigation: Add a clear language fallback before serving non-Chinese users. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lizejia668-code/skills/ads-brain-planning-optimize-pipeline) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Chinese Markdown with structured JSON-style planning fields, warnings, next-action guidance, and draft patch recommendations when applicable] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory output only; campaign changes require separate execution confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
