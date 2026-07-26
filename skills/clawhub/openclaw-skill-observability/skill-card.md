## Description: <br>
Provides tools to monitor OpenClaw health by reporting recent errors and estimating API usage costs over the last 24 hours. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erain](https://clawhub.ai/user/erain) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Bot owners and developers use this skill to check recent OpenClaw session costs and failed or aborted sessions from an agent conversation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recent error reports may expose sensitive local operational details such as paths, stack traces, session IDs, titles, usage details, or accidentally logged secrets. <br>
Mitigation: Install only where users are authorized to view OpenClaw telemetry, and review or redact outputs before sharing them. <br>
Risk: API cost reports are estimates and may differ from provider billing because they rely on recent session data and a fixed pricing table. <br>
Mitigation: Use cost output for operational awareness and verify charges against provider billing records before making financial decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/erain/skills/openclaw-skill-observability) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown] <br>
**Output Format:** [Markdown summaries, lists, and cost tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Cost reports are estimates based on recent local session data and a fixed pricing table.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
