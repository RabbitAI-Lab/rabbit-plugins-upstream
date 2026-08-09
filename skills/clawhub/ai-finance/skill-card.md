## Description: <br>
Ai Finance provides AI-assisted financial analysis, natural-language quantitative research, financial calculations, investment-decision support, and trading-analysis workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to generate structured finance-analysis outputs from market data, financial reports, and user-provided analysis requests. It is intended for advisory analysis and workflow assistance, not unattended trading or account-impacting actions without human approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill describes automated trading, recurring financial tasks, and account-impacting finance workflows. <br>
Mitigation: Use outputs as advisory analysis only unless a separate workflow adds explicit human approval, cancellation controls, and audit logging for trading or scheduled actions. <br>
Risk: The skill may require API keys for financial data sources. <br>
Mitigation: Store API keys in environment variables or a managed secret store, keep privileges least-scoped, rotate keys regularly, and avoid embedding credentials in prompts or files. <br>
Risk: Financial analysis can be inaccurate, stale, or based on delayed or unavailable market data. <br>
Mitigation: Verify important outputs against trusted data sources and require human review before investment, trading, or compliance decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-finance) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with structured JSON examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference finance API keys, market data sources, scheduled workflows, and exported analysis results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
