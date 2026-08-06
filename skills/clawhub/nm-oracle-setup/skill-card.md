## Description: <br>
Provisions the Oracle ML inference daemon with ONNX Runtime via uv. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to set up a local Oracle ONNX inference environment, install ONNX Runtime with uv, and verify that the daemon dependency environment is ready. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Provisioning downloads Python dependencies with uv and creates a local virtual environment for ONNX inference. <br>
Mitigation: Install only after trusting the Oracle plugin source and approving local dependency downloads for the target environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-oracle-setup) <br>
- [Oracle plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/oracle) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports setup success or failure and suggests uv or network checks when provisioning fails.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
