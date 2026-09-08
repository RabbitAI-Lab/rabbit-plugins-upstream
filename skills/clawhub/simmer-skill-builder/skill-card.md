## Description:

Generates complete, installable OpenClaw trading skill folders from natural language prediction-market strategy descriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading-skill builders use this skill to turn rough prediction-market strategy ideas, campaign briefs, or strategy posts into complete Simmer/OpenClaw skill folders with docs, config, validation, and dry-run trading scaffolding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated trading skills can create scripts intended for real-money market execution.

Mitigation: Review strategy logic and configuration, run in dry-run or sim mode first, and use live execution only after confirming risk controls.

Risk: Generated skill files may include proprietary strategy details or accidentally expose sensitive information before publication.

Mitigation: Keep generated skills local until explicitly choosing to publish, review every generated file, and never embed API keys or secrets in generated code.

Risk: A safety-bypass option can disable safeguards during live trading.

Mitigation: Avoid --no-safeguards for live trading and keep agent-side and server-side safety checks enabled.

Risk: Package installation can affect the user's local agent environment.

Mitigation: Pin or isolate package installs where possible before running generated skills.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/simmer/skills/simmer-skill-builder)
- [AgentSkills Open Standard](https://agentskills.io)
- [Simmer SDK API Reference](references/simmer-api.md)
- [Simmer Skill Template](references/skill-template.md)
- [Example: LLM Probability Oracle](references/example-llm-oracle.md)
- [Example: Mert Sniper](references/example-mert-sniper.md)
- [Example: Weather Trader](references/example-weather-trader.md)
- [Bring Your Own Data Documentation](https://docs.simmer.markets/skills/byo-data-source)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance plus generated skill files such as SKILL.md, JSON configuration, Python code, and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated trading skills are expected to default to dry-run behavior and require explicit review before publishing or live execution.]

## Skill Version(s):

1.3.10 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
