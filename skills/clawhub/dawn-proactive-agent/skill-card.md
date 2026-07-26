## Description: <br>
Dawn Agent v1.5 self-evolution proactive architecture. P0-P4 framework for autonomous ETF trading agent with self-reflection, state machine, audit trail, multi-dimension scoring, and safety guardrails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chen6896qqwee](https://clawhub.ai/user/chen6896qqwee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and trading-agent operators use this skill to run and inspect a Python workflow for A-share ETF strategy checks, paper-trading order execution, audit logging, reflection, and guardrails. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can execute paper-trading orders and invoke sibling local skills. <br>
Mitigation: Use a sandbox or paper-trading account, verify sibling skills before use, and require explicit confirmation before running scheduled jobs or the --execute path. <br>
Risk: Audit, state, and strategy files may contain sensitive portfolio strategy data. <br>
Mitigation: Apply retention and redaction controls before sharing logs or using the skill with real trading workflows. <br>
Risk: The skill uses network resources for market data and broader local workspace access. <br>
Mitigation: Review and tighten the network allowlist and filesystem scope before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chen6896qqwee/skills/dawn-proactive-agent) <br>
- [Session trace sample](samples/proactive_demo.md) <br>
- [Eastmoney market data API used by artifact](https://push2.eastmoney.com/api/qt/clist/get?pn=1&pz=30&po=1&np=1&fltt=2&invt=2&fid=f62&fs=m:90+t:2&fields=f12,f14,f62,f184,f66) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown and terminal text with Python scripts, shell commands, and JSON audit or state files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces strategy logs, audit records, reflection records, market summaries, guardrail decisions, and optional paper-trading order actions.] <br>

## Skill Version(s): <br>
1.5.0 (source: server release metadata and artifact changelog, released 2026-07-06) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
