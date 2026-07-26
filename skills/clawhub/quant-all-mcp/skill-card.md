## Description: <br>
QuantAll is a local stock-market vectorized analysis MCP that lets an agent run Python-based factor calculations, strategy backtests, IC analysis, stock screening, and visualizations over A-share market data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mifochen](https://clawhub.ai/user/mifochen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they want an agent to perform local quantitative stock analysis, including factor evaluation, strategy backtesting, screening, and market-data visualization. It is intended to trigger only for explicit quantitative analysis requests rather than general stock-market conversation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates a local Python environment, installs packages, edits MCP configuration, creates local configuration or database files, and starts a localhost background service. <br>
Mitigation: Confirm these local changes with the user before installation or startup, and install only when the user wants a local QuantAll stock-analysis service. <br>
Risk: The optional UpdateStock workflow may store or use a Tushare API token and local market database configuration. <br>
Mitigation: Treat API tokens and database paths as local user-controlled configuration, and explain any database path changes before applying them. <br>
Risk: The documented dangerouslyDisableSandbox workaround broadens local execution risk. <br>
Mitigation: Avoid using dangerouslyDisableSandbox unless the user deliberately accepts the broader local execution risk. <br>


## Reference(s): <br>
- [QuantAll Playbook](references/quantall_playbook.md) <br>
- [ClawHub skill page](https://clawhub.ai/mifochen/skills/quant-all-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code, shell commands, configuration snippets, and analysis summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May summarize large local analysis results rather than displaying raw detail outputs.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and requirements.txt) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
