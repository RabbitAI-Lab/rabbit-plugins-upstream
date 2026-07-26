## Description: <br>
Financial Calculator Pro helps agents calculate future value tables, present value, discounts, markup pricing, and compound interest for investment growth, pricing strategy, loan valuation, and scenario comparison. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tarigha](https://clawhub.ai/user/tarigha) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to perform financial calculations, compare rates and time periods, and generate CLI or web UI outputs for investment, loan, discount, and pricing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional web UI runs a local Flask server and may bind beyond localhost. <br>
Mitigation: Use it on a trusted network and bind the server to localhost when a tighter local-only setup is needed. <br>
Risk: The launcher may install Flask into a virtual environment and the UI loads Chart.js from a CDN. <br>
Mitigation: Review dependency installation in the target environment and bundle Chart.js locally when external CDN loading is not acceptable. <br>
Risk: Financial inputs may contain sensitive personal or business details. <br>
Mitigation: Avoid entering highly sensitive financial details unless the local environment and network are trusted. <br>


## Reference(s): <br>
- [Financial Formulas Reference](references/formulas.md) <br>
- [Financial Calculator Pro ClawHub listing](https://clawhub.ai/tarigha/skills/financial-calculator) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, code, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON calculation results; the optional web UI renders interactive tables and charts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [CLI output is JSON; the local Flask web UI can render interactive tables and Chart.js charts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
