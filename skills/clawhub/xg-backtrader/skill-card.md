## Description:

A Backtrader-focused assistant that helps users design, generate, explain, backtest, optimize, and analyze quantitative trading strategies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[li152](https://clawhub.ai/user/li152)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and quantitative analysts use this skill to turn trading ideas into Backtrader-based Python strategies, backtest workflows, analysis reports, and optimization guidance. It is also useful for learning Backtrader concepts such as data feeds, Cerebro, analyzers, orders, broker settings, resampling, and live-trading migration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Copy-ready examples may execute command-line or configuration text as Python.

Mitigation: Review generated scripts before running them and avoid eval-style parsing for user-supplied CLI or configuration values.

Risk: The skill covers live broker connections and trading workflows.

Mitigation: Use paper or demo broker accounts first, verify order behavior, and avoid deploying generated live-trading code without independent review.

Risk: Generated examples may include API tokens, credentials, or file paths for market data and broker integrations.

Mitigation: Keep secrets out of code, load credentials from a secure environment, and confirm file paths before any script writes or deletes data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/li152/skills/xg-backtrader)
- [Artifact skill definition](artifact/SKILL.md)
- [Backtrader overview reference](artifact/references/1什么是 Backtrader.txt)
- [Data source reference](artifact/references/36数据源.txt)
- [Strategy reference](artifact/references/37Strategy.txt)
- [Order reference](artifact/references/38Order.txt)
- [Broker reference](artifact/references/39Broker.txt)
- [Analyzer reference](artifact/references/41分析器.txt)
- [Live trading reference](artifact/references/44实盘.txt)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with Python code blocks, shell command snippets, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated examples may reference local data files, third-party market data packages, and broker integrations; review paths, credentials, and account mode before execution.]

## Skill Version(s):

1.0.0 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
