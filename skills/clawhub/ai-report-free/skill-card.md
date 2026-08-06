## Description: <br>
AI财报分析 helps agents analyze financial reports, summarize F-score-style signals, and produce risk-warning outputs for finance workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to support financial-report analysis, F-score summaries, risk warnings, financial forecasting, and credit-risk review. Outputs should be reviewed by a qualified human before investment, lending, or other material financial decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence flags the skill as suspicious because it requests host command execution and API-key based integrations without clear limits or user-control safeguards. <br>
Mitigation: Install only after review, grant exec and API-key access only when needed, run in a constrained environment, avoid admin privileges, and require user approval for commands. <br>
Risk: The skill may process sensitive financial data and API credentials. <br>
Mitigation: Provide only necessary data, use least-privilege API keys, avoid exposing secrets in prompts or files, and prefer isolated environments for financial processing. <br>
Risk: Automated financial analysis or risk warnings can be incomplete, inaccurate, or unsuitable for material decisions. <br>
Mitigation: Require human review of outputs and source data before using results for investment, lending, compliance, or other consequential financial decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-report-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON and Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require user-provided financial data, API-key configuration, and agent exec access; review generated commands and financial outputs before use.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
