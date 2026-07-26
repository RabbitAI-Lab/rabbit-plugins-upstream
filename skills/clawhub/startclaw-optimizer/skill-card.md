## Description: <br>
StartClaw-Optimizer helps agents route tasks, schedule execution, throttle browser activity, compact subagent context, and monitor usage to reduce token and model costs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[idanmann10](https://clawhub.ai/user/idanmann10) <br>

### License/Terms of Use: <br>
StartClaw Internal Use License <br>


## Use Case: <br>
Developers and agent operators use this skill to reduce agent workflow cost and context growth by selecting lower-cost models for simple tasks, scheduling work with retries, limiting browser concurrency, compacting long subagent contexts, and monitoring budget usage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local optimizer logs may expose raw session identifiers or sensitive conversation metadata. <br>
Mitigation: Redact or hash session keys and avoid writing sensitive conversation details to shared logs. <br>
Risk: Model routing and context compaction may affect answer quality or omit useful context. <br>
Mitigation: Review routing outcomes and compacted summaries for high-impact tasks before relying on the result. <br>
Risk: Unverified package installation could introduce supply-chain drift from the reviewed artifact. <br>
Mitigation: Pin the package version and verify the package source or hash before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/idanmann10/skills/startclaw-optimizer) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>
- [package.json](package.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with JavaScript and shell examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model-selection recommendations, cost estimates, scheduler behavior, browser concurrency limits, context-compaction summaries, and dashboard usage metrics.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
