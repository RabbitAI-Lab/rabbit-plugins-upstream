## Description:

Generate complete, installable OpenClaw trading skills from natural language strategy descriptions, including SKILL.md, Python trading logic, and configuration files ready to install and run.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading-skill builders use this agent skill to turn rough trading ideas, strategy posts, or campaign briefs into complete OpenClaw skill folders with documented trading logic, configuration, validation, and publishing steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated trading skills may be published publicly or switched into live trading before the strategy and files are fully reviewed.

Mitigation: Keep dry-run defaults, require explicit live-trading intent, and perform a final human review before publishing or running generated skills.

Risk: Mutable remote tooling used through npx or pip may change behavior between runs.

Mitigation: Pin package versions before running generated install, validation, or publishing commands.

Risk: Generated files could accidentally expose wallet material, API keys, or other private credentials.

Mitigation: Keep wallet and private keys out of generated files, use environment variables or secret storage, and scan files before publication.

## Reference(s):

- [Simmer SDK API Reference](references/simmer-api.md)
- [Simmer Skill Template](references/skill-template.md)
- [Example: LLM Probability Oracle](references/example-llm-oracle.md)
- [Example: Weather Trader](references/example-weather-trader.md)
- [Example: Mert Sniper](references/example-mert-sniper.md)
- [Acceptance Fixture: Lunar Claude + Polymarket Quant Machine](references/fixture-lunar-quant.md)
- [AgentSkills](https://agentskills.io)
- [Bring Your Own Data](https://docs.simmer.markets/skills/byo-data-source)
- [Simmer Skills Building](https://docs.simmer.markets/skills/building)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance plus generated skill files such as SKILL.md, Python scripts, JSON configuration, and shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated trading skills should default to dry-run behavior and require human review before live trading or public publishing.]

## Skill Version(s):

1.3.10 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
