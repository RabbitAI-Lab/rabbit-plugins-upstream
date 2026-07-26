## Description: <br>
Provisions the oracle ML inference daemon with onnxruntime via uv. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to set up the oracle plugin's local ONNX inference environment for skill quality evaluation by creating a uv-managed Python environment, installing onnxruntime, and verifying provisioning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Provisioning relies on external oracle plugin code that performs the actual environment setup and may control daemon startup behavior. <br>
Mitigation: Review the referenced oracle plugin code before running the uv command and install only when local ONNX inference setup is intended. <br>
Risk: Initial setup downloads Python dependencies and can fail when uv or network access is unavailable. <br>
Mitigation: Confirm uv is installed and network access is available, then report provisioning errors clearly to the user. <br>


## Reference(s): <br>
- [Nm Oracle Setup on ClawHub](https://clawhub.ai/athola/skills/nm-oracle-setup) <br>
- [Oracle plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/oracle) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with an inline bash command block] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports provisioning success or failure and surfaces uv, network, and external plugin review guidance to the user.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
