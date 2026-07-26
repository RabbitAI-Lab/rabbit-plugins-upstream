## Description: <br>
Retrieve real-time hardware metrics from Apple Silicon Macs using mactop's TOON format. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[metaspartan](https://clawhub.ai/user/metaspartan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to retrieve and summarize local Apple Silicon hardware metrics such as CPU, RAM, GPU, power, thermals, network, disk I/O, and Thunderbolt bus information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Metric output may reveal machine model, resource usage, thermal state, and I/O counters. <br>
Mitigation: Avoid sharing captured output when those local system details are sensitive. <br>
Risk: The skill depends on installing and running the Homebrew mactop package locally. <br>
Mitigation: Install only when comfortable adding that package and running local read-only hardware monitoring commands. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline bash commands and readable metric summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local hardware model, utilization, thermal state, and I/O counters.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
