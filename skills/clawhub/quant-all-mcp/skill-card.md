## Description: <br>
QuantAll helps an agent use a local Python-based stock-market computation environment for full-market factor analysis, strategy backtesting, IC analysis, screening, visualization, and database-assisted workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mifochen](https://clawhub.ai/user/mifochen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they want an agent to install, configure, start, and operate QuantAll for quantitative A-share market analysis. It supports local factor computation, backtesting, stock screening, heat-map exploration, database update workflows, and scripted task execution after user approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release includes a local MCP service, local database writes, Tushare credential-file use, and Python/package execution on the user's machine. <br>
Mitigation: Install and enable it only after the user understands those local effects, reviews the configuration changes, and accepts package execution and database-write behavior. <br>
Risk: The execute_python_script and run_task_file capabilities are high-risk if untrusted prompts or files influence tool use. <br>
Mitigation: Run only trusted files that have been inspected, and avoid enabling the skill in conversations where untrusted prompts or files may steer execution. <br>
Risk: The security verdict is suspicious because the skill combines disclosed stock-analysis behavior with under-scoped local code execution and background service capabilities. <br>
Mitigation: Review the skill and its security guidance before deployment, and keep the skill disabled unless those local execution capabilities are required for the task. <br>


## Reference(s): <br>
- [QuantAll ClawHub Skill Page](https://clawhub.ai/mifochen/skills/quant-all-mcp) <br>
- [QuantAll Playbook](references/quantall_playbook.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code, shell commands, and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to create a Python virtual environment, install packages, update MCP configuration, start a localhost service, write local configuration files, and run trusted local task or script files with user consent.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
