## Description: <br>
This skill helps testers observe test execution across function behavior, interface responses, logs, UI rendering, data consistency, and performance, then record anomalies and follow-up questions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
QA engineers and developers use this skill during test execution to capture structured observations, correlate each observation with a test case, and identify anomalies across functional, log, UI, data, dependency, and performance signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad troubleshooting or test-execution language may activate this workflow when the user intended a narrower task. <br>
Mitigation: When the task is ambiguous, explicitly confirm whether to use this observation workflow before allowing shell or log-inspection steps. <br>
Risk: The workflow may involve shell commands, log inspection, screenshots, or external monitoring in the target test environment. <br>
Mitigation: Run it in a controlled environment and review requested commands, logs, and tool access before execution. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown execution observation report with traceable observation IDs, test-case links, anomaly lists, and environment issue notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Observations should use unique OBS-XXXX IDs and link to TC-XXXX test case IDs; command or tool use should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
