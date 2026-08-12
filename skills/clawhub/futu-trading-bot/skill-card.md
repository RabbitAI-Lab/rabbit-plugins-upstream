## Description:

Use Futu Trade Bot Skills to run account, quote, and trade workflows with real HK market data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jeffersonling1217-png](https://clawhub.ai/user/jeffersonling1217-png)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to query Futu account and Hong Kong market data, prepare trading workflows, and execute simulated or confirmed live brokerage actions through Futu OpenD.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Futu OpenD and perform live brokerage operations when configured for real trading.

Mitigation: Default to SIMULATE, require explicit confirmation for live actions, and review exact order parameters before execution.

Risk: A direct path may bypass confirmation checks for live brokerage actions.

Mitigation: Use the documented wrapper functions only and avoid importing or calling internal trade_service objects directly.

Risk: Trading credentials and account data may be present in local configuration or optional cache files.

Mitigation: Keep credentials in a private config file, prefer trade_password_md5, and only persist account information when explicitly requested.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jeffersonling1217-png/skills/futu-trading-bot)
- [Publisher profile](https://clawhub.ai/user/jeffersonling1217-png)
- [README](README.md)
- [Account Manager documentation](docs/account.md)
- [Config Manager documentation](docs/config.md)
- [Quote Service documentation](docs/quote.md)
- [Strategy Helpers documentation](docs/strategy.md)
- [Trade Service documentation](docs/trade.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Python and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include account, quote, order, strategy, and preflight results from local Futu OpenD workflows.]

## Skill Version(s):

1.0.9 (source: pyproject.toml, ClawHub release metadata, artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
