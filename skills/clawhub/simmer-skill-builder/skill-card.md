## Description:

Generate complete, installable OpenClaw trading skills from natural language strategy descriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading-skill builders use this skill to turn natural language strategy ideas, campaign briefs, or strategy posts into installable OpenClaw/Simmer skill folders with documentation, configuration, and runnable trading logic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated skills may be published publicly or run before the user has confirmed the final files, slug, version, account, and visibility.

Mitigation: Require local human review before publishing or execution, and keep generated bots in dry-run or paper mode until tested.

Risk: Remote package execution with unpinned CLI versions can change behavior between runs.

Mitigation: Prefer pinned CLI versions instead of @latest for publishing and validation commands.

Risk: Trading API keys or wallet private keys could be exposed through source files, logs, or published artifacts.

Mitigation: Keep secrets in environment variables or secret stores, scan generated artifacts before publication, and never include keys in generated code or documentation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/simmer/skills/simmer-skill-builder)
- [Simmer SDK API Reference](references/simmer-api.md)
- [Simmer Skill Template](references/skill-template.md)
- [Example: Weather Trader](references/example-weather-trader.md)
- [Example: Mert Sniper](references/example-mert-sniper.md)
- [Example: LLM Probability Oracle](references/example-llm-oracle.md)
- [Bring Your Own Data](https://docs.simmer.markets/skills/byo-data-source)
- [AgentSkills](https://agentskills.io)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance plus generated skill files such as SKILL.md, clawhub.json, Python scripts, and configuration.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated trading skills are expected to default to dry-run behavior and require human review before publishing or live execution.]

## Skill Version(s):

1.3.11 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
