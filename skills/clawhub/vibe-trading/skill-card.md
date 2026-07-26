## Description: <br>
Vibe Trading is a finance research toolkit for agent-assisted backtesting, factor analysis, options pricing, trade-journal analysis, shadow-account reports, and market-data workflows across multiple asset classes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[warren618](https://clawhub.ai/user/warren618) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and traders use this skill to connect an agent to Vibe Trading finance tools for market data, backtesting, factor analysis, options analysis, trade-journal review, and multi-agent research workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional external MCP server loading can broaden what the agent is able to run or access. <br>
Mitigation: Use only trusted external MCP servers and prefer explicit enabledTools allowlists instead of wildcards. <br>
Risk: Finance connectors and research workflows may involve market-data, broker, or LLM credentials. <br>
Mitigation: Use trusted credentials only, keep generated configuration and strategy files inside a controlled workspace, and review connector settings before use. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown or structured text with optional JSON, code/configuration snippets, shell commands, and generated report files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce research reports, backtest metrics, strategy files, and connector/account readouts depending on selected tools and configured credentials.] <br>

## Skill Version(s): <br>
0.1.12 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
