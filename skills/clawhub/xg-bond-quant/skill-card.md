## Description:

A convertible-bond quantitative analysis assistant that helps agents retrieve market and factor data, run strategy backtests, and summarize portfolio analytics from the 小果 quantitative strategy system.

This skill is ready for commercial/non-commercial use.

## Publisher:

[li152](https://clawhub.ai/user/li152)

### License/Terms of Use:

MIT-0

## Use Case:

Convertible-bond investors, quantitative researchers, and strategy developers use this skill to analyze convertible-bond history, technical factors, backtests, correlations, covariance, portfolio optimization, and return metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses authenticated access to a market-data and strategy-management server.

Mitigation: Use only trusted servers, prefer HTTPS, and do not include real passwords or authorization codes in examples or logs.

Risk: The security evidence flags broad strategy creation, publication, deletion, and bulk-deletion capabilities.

Mitigation: Require explicit user confirmation before mutating strategy actions and keep backups of strategy and factor data.

Risk: The security evidence flags custom-code and local file-writing capabilities.

Mitigation: Review custom code before execution and restrict file-writing actions to intended project or data directories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/li152/skills/xg-bond-quant)
- [xg_quant_trader tutorial/project](https://gitcode.com/qq_50882340/xg_quant_trader)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python snippets, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose authenticated data access, strategy-management actions, custom factor code, and local file-writing workflows; users should confirm mutating actions before execution.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
