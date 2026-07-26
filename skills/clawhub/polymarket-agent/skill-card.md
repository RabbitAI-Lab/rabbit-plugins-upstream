## Description: <br>
Research Polymarket markets, whale flow and smart money; optionally trade a Polygon wallet behind deterministic risk guard-rails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andretuta](https://clawhub.ai/user/andretuta) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to research Polymarket markets, monitor large trades and trader activity, inspect wallet state, and optionally prepare or execute guarded limit orders with an explicitly configured wallet. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can manage a dedicated Polymarket wallet and potentially place real orders. <br>
Mitigation: Keep dry-run enabled until tested, fund only a dedicated wallet with money the user accepts losing, and require explicit user authorization for orders. <br>
Risk: A Polygon private key can be exposed if configured through the legacy environment-variable path. <br>
Mitigation: Prefer the encrypted keystore created by setup; use POLYMARKET_KEY only as a gated fallback with POLYMARKET_ALLOW_ENV_KEY=1. <br>
Risk: Autonomous mode can place time-boxed orders without per-order confirmation. <br>
Mitigation: Avoid enabling autonomous mode unless the user accepts that posture; keep it time-boxed, capped, and subject to the kill switch. <br>
Risk: Market descriptions, trader names, and news content can be misleading or contain prompt-injection text. <br>
Mitigation: Treat external content as untrusted data, summarize it for the user, and never convert it into trading action without explicit user authorization. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/andretuta/skills/polymarket-agent) <br>
- [ClawHub Security Audit](https://clawhub.ai/andretuta/skills/polymarket-agent/security-audit) <br>
- [OpenClaw](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown analysis with CLI commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include market research summaries, wallet state, whale alerts, dry-run order summaries, and guarded trading instructions.] <br>

## Skill Version(s): <br>
2.1.3 (source: server release metadata and pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
