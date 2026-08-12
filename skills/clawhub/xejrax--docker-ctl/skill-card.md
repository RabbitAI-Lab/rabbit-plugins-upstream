## Description: <br>
Inspect containers, logs, and images via podman. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xejrax](https://clawhub.ai/user/xejrax) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to inspect local containers, view logs, list images, and check container details through podman. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Container logs and inspect output may include environment variables, tokens, service names, or other sensitive operational details. <br>
Mitigation: Review and redact command output before sharing it outside the local trusted environment. <br>
Risk: The skill lets an agent inspect the local container runtime. <br>
Mitigation: Install and use it only where agent access to local container metadata is acceptable. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Text] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include container logs and inspection text from the local container runtime.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
