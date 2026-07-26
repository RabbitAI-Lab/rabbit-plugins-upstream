## Description: <br>
Routes Tavily web searches across multiple API keys with quota-aware selection, failover, rate-limit cooldowns, and status reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fangtang0206](https://clawhub.ai/user/fangtang0206) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to run Tavily-backed search across multiple API keys while tracking key health, quota, rate-limit cooldowns, and failover behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live Tavily keys may be exposed through config/keys.json or runtime state files. <br>
Mitigation: Before using live keys, ensure config/keys.json and state/quota.json are ignored from version control and prefer environment variables or a secret manager for shared or production environments. <br>
Risk: Raw curl diagnostics or parallel key tests can burn quota or trigger broad cooldowns. <br>
Mitigation: Use the bundled router commands for normal operation, avoid parallel key tests, and stop testing after the first 429 or other clear failure signal. <br>
Risk: Cooldown behavior may be inconsistent with the documentation because the security evidence notes that cooldown_minutes is cast to int while docs recommend 0.5. <br>
Mitigation: Patch or test the cooldown fallback with non-production quota before relying on fractional cooldown settings with live Tavily keys. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/fangtang0206/skills/tavily-quota-router) <br>
- [README](README.md) <br>
- [Quickstart](QUICKSTART.md) <br>
- [Security Hardening](references/security-hardening.md) <br>
- [State Machine Walkthrough](references/state-machine-2026-07-08.md) <br>
- [Tavily 401/403 Recovery Pattern](references/tavily-401-403-recovery-pattern.md) <br>
- [Tavily 429 Retry-After Handling](references/tavily-429-retry-after-2026-07-17.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, shell commands, JSON command output, and Python/configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search command output can include JSON results, selected key index, usage snapshot, and status or error fields.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
