## Description: <br>
Analyze OpenClaw session logs to report token usage, costs, and performance metrics grouped by agent and model. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[khaney64](https://clawhub.ai/user/khaney64) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect local OpenClaw session history and summarize API spending, token usage, model costs, cache usage, and session details across agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local OpenClaw session logs, which can contain session IDs, local paths, cost history, and usage patterns. <br>
Mitigation: Run it only on directories you intend to inspect and use --agent, --offset, --provider, or --path to narrow the report when less data is needed. <br>
Risk: Detailed, JSON, or Discord-formatted output may expose sensitive usage details if shared outside the intended audience. <br>
Mitigation: Review generated output before sharing and remove session IDs, local paths, costs, or usage history that should remain private. <br>


## Reference(s): <br>
- [ClawHub Session Cost Skill Page](https://clawhub.ai/khaney64/skills/session-cost) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Text summaries, compact tables, JSON, Discord-friendly Markdown, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can filter by agent, provider, time offset, custom path, session ID, detail mode, table mode, and output format.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
