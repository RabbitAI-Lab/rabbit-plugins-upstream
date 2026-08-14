## Description:

QuantAll is a local MCP skill that lets an agent run vectorized Python calculations over A-share market data for factor analysis, strategy backtests, IC analysis, screening, and visualization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mifochen](https://clawhub.ai/user/mifochen)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use QuantAll when they need an agent to compute quantitative stock-analysis results against a local market database instead of only summarizing market commentary. Typical tasks include factor analysis, strategy backtesting, stock screening, heat-map exploration, and maintaining local A-share market data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can start a background localhost MCP service and modify MCP configuration.

Mitigation: Confirm service startup and configuration changes with the user before execution, and stop or disable the service when it is no longer needed.

Risk: The skill can install Python packages, write local databases/results, and persist a Tushare API token locally.

Mitigation: Use it only in an intended local quant-analysis environment, disclose package installation and file writes, and avoid storing secrets unless the user explicitly approves.

Risk: `execute_python_script` and `run_task_file` can run local files with weak containment.

Mitigation: Do not run those tools on untrusted files; inspect task files or scripts first and ask for confirmation before execution.

## Reference(s):

- [QuantAll Playbook](references/quantall_playbook.md)
- [QuantAll ClawHub Skill Page](https://clawhub.ai/mifochen/skills/quant-all-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Analysis]

**Output Format:** [Markdown or text responses with JSON-like analysis results, Python snippets, shell commands, and MCP configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local configuration, database, token, script, and result files when the user approves those actions.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
