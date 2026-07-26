## Description: <br>
Terraform and OpenTofu configuration, modules, testing, state management, and HCL review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure engineers use this skill to write, review, test, troubleshoot, and maintain Terraform or OpenTofu modules, HCL, tfvars, tftest files, and state-management workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Terraform or OpenTofu recommendations can affect infrastructure, state, access controls, or cloud costs when applied by an agent or operator. <br>
Mitigation: Review generated configuration and plans before apply, use least-privilege credentials, keep remote state encrypted and locked, and run validation and scanning commands such as terraform fmt, terraform validate, tflint, trivy, or checkov. <br>
Risk: The release security guidance notes that use of operational workflows may involve configured API tokens, admin CLIs, or local notes. <br>
Mitigation: Install only when the publisher is trusted for the intended workflows and use least-privilege tokens for any connected services. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with HCL and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent guidance for Terraform and OpenTofu workflows; does not include executable automation in the artifact.] <br>

## Skill Version(s): <br>
4.2.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
