## Description: <br>
Execute coding work as a cached dependency graph with local quality gates, parallel agents, localized retries, resume support, token telemetry, and an interactive report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gwaghmar](https://clawhub.ai/user/gwaghmar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to plan, execute, validate, retry, and summarize coding work through a local dependency graph workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: First use downloads a local runtime through npx and creates run state, cache, and reports under `.graph`. <br>
Mitigation: Review the external package path and local `.graph` artifacts before use in environments that restrict remote package execution or generated workspace state. <br>
Risk: Generated plans and shell commands could make incorrect code changes if followed without review. <br>
Mitigation: Run the skill's required quality gate, review proposed node scopes and commands, and require explicit instruction before committing, pushing, deploying, or creating a pull request. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gwaghmar/skills/graph-skill) <br>
- [Graph protocol schema](references/protocol.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, markdown] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local ASCII and HTML run reports, cache/retry records, quality-gate summaries, and token telemetry when available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
