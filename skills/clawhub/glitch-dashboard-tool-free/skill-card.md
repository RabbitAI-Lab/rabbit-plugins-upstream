## Description: <br>
统一仪表盘基础版 helps an agent manage a local web dashboard for task queues, system metrics, log filtering, and quick CLI status checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External personal users use this skill to ask an agent to start and operate a lightweight local dashboard, monitor CPU, memory, load, uptime, and network status, inspect or manage task queues, filter logs, and run quick status checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent local CLI control for dashboard operations, including starting services, calling external APIs or callbacks, and clearing queues. <br>
Mitigation: Require explicit confirmation before starting services, calling external APIs or callbacks, or clearing queues, and review proposed commands before execution. <br>
Risk: The documented configuration check can list environment variables that may reveal API keys, tokens, or secrets. <br>
Mitigation: Avoid the broad secret-check command and do not expose environment variables or API keys unless the values are necessary and safe to reveal. <br>
Risk: A local dashboard port and API key storage can expose operational data if left unsecured. <br>
Mitigation: Bind the dashboard to a trusted interface, protect access with appropriate local controls, and store API keys outside repositories or shared logs. <br>
Risk: Queue-clearing behavior can remove pending work or operational context. <br>
Mitigation: Preview or export the queue state before clearing it, and confirm that no pending task needs to be preserved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/glitch-dashboard-tool-free) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash and JSON examples and structured command/status output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May start a local dashboard service, inspect local system state, clear or manage a task queue, and return JSON, text, or CSV-style results depending on the requested output_format.] <br>

## Skill Version(s): <br>
1.0.2 (source: evidence.json release.version; artifact/SKILL.md frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
