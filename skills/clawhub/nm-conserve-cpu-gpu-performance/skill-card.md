## Description: <br>
Establishes CPU/GPU baselines before resource-intensive operations. Use before builds, training runs, or any task that pins cores or GPUs for over a minute. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to establish resource baselines, scope heavy commands, instrument CPU/GPU work, throttle shared compute usage, and log follow-up actions before builds, tests, training runs, or retries that may consume significant resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Monitoring commands can expose process names or command arguments in captured logs. <br>
Mitigation: Review baseline and monitoring output before sharing it externally. <br>
Risk: The skill can lead an agent to run local resource-inspection commands before heavy work. <br>
Mitigation: Install it only when deliberate CPU/GPU planning and resource logging are desired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-cpu-gpu-performance) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve) <br>
- [Publisher profile](https://clawhub.ai/user/athola) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, markdown] <br>
**Output Format:** [Markdown with inline shell commands and concise run summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Expected output summarizes baseline metrics, selected scope, instrumentation, throttling tactics, and follow-up items.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
