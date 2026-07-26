## Description: <br>
Establishes CPU/GPU baselines before resource-intensive operations and guides agents to scope, instrument, throttle, and document heavy builds, tests, or training runs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill before CPU- or GPU-intensive work to capture baseline utilization, choose narrower validation scopes, profile resource use, throttle shared compute, and record follow-up work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Profiling and resource-check commands can expose host utilization details or affect shared systems when run in quota-managed environments. <br>
Mitigation: Review commands such as uptime, process listings, and GPU monitoring before execution on shared hosts, and apply local policies for access to utilization data. <br>
Risk: The skill may still recommend heavy builds, tests, or training runs when narrower validation is not enough. <br>
Mitigation: Set CPU/GPU budgets first, prefer targeted smoke or module-level runs, and document why any full-suite or long training run is necessary. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-cpu-gpu-performance) <br>
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Markdown] <br>
**Output Format:** [Markdown summary with inline shell commands and resource notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes baseline metrics, selected scope, instrumentation captured, throttling tactics, and follow-up items.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
