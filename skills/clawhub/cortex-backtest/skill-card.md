## Description:

Cortex Backtest helps agents configure and use the Cortex quantitative strategy backtesting engine for JQ-style daily strategy backtests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnluicn](https://clawhub.ai/user/johnluicn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and quantitative strategy researchers use this skill to configure Cortex workspaces, turn strategy ideas into JQ-style daily backtest code, run Cortex CLI backtests, and interpret generated result files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead an agent to modify persistent workspace records such as TOOLS.md or experience documents.

Mitigation: Review proposed file changes and require explicit user confirmation before updating or deleting persistent records.

Risk: The skill includes setup flows that may use sudo or write under /opt or /etc.

Mitigation: Prefer workspace or tenant configuration modes, and require explicit confirmation before any sudo or system-level path changes.

Risk: Backtest workspace files and Cortex configuration may be created or changed during setup or execution.

Mitigation: Constrain writes to the intended workspace or tenant directory and inspect generated configuration before running backtests.

## Reference(s):

- [Cortex API Reference](artifact/references/cortex-api-reference.md)
- [Cortex CLI Usage](artifact/references/cortex-cli-usage.md)
- [Cortex Experience Notes](artifact/references/cortex-experience.md)
- [ClawHub Skill Page](https://clawhub.ai/johnluicn/skills/cortex-backtest)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands, Python examples, configuration snippets, and backtest result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose workspace setup steps, strategy files, Cortex CLI commands, and interpretation of backtest outputs.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
