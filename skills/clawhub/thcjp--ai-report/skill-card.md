## Description: <br>
Ai Report helps agents analyze financial reports, summarize F-score financial health signals, generate risk warnings, and produce structured finance analysis outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External finance analysts, investors, and developers use this skill to ask an agent for financial statement analysis, F-score summaries, portfolio or deal risk review, and report-style outputs from provided company or market data. Outputs should be reviewed by a qualified human before investment, accounting, or business decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan classifies the skill as suspicious because it requests command execution and external financial-data/API use while scope and data handling are under-explained. <br>
Mitigation: Review before installing, restrict use to finance-report analysis, and avoid providing confidential portfolio, company, or account data unless the recipient APIs and systems are understood. <br>
Risk: The skill may propose dependency installation, shell commands, API calls, monitoring, or export actions. <br>
Mitigation: Require explicit approval before installing dependencies, running commands, calling APIs, monitoring data, or exporting files. <br>
Risk: Financial analysis, risk warnings, and market predictions can be incomplete or misleading if inputs, data sources, or assumptions are wrong. <br>
Mitigation: Treat outputs as decision support only and have a qualified reviewer validate source data, assumptions, calculations, and conclusions before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-report) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and structured JSON examples, with optional shell commands and Python snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose dependency installation, API key configuration, financial-data API use, analysis reports, exports, or monitoring steps; require approval before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
