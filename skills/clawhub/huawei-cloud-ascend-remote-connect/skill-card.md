## Description: <br>
Provides temporary SSH remote connection for Huawei Cloud Ascend devices with dynamic host, port, user, and password input, plus disk management, NPU monitoring, container management, security auditing, and log analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure engineers use this skill to connect to Huawei Cloud Ascend servers over SSH, monitor NPU health, manage disks and containers, and troubleshoot remote systems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill has broad SSH administration authority over remote systems. <br>
Mitigation: Install only when broad SSH administration is intended, use a dedicated non-root account with tightly scoped sudo, and test on non-production hosts before granting access to important systems. <br>
Risk: Credential and host-verification choices can expose sensitive systems if passwords or host trust are handled weakly. <br>
Mitigation: Prefer SSH keys, avoid passing passwords on the command line where possible, verify host keys, and limit access to trusted hosts. <br>
Risk: Raw or direct command execution can modify or damage remote hosts. <br>
Mitigation: Disable or restrict raw command execution, keep confirmation prompts for sensitive actions, and review commands before execution. <br>


## Reference(s): <br>
- [Skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-ascend-remote-connect) <br>
- [IAM Permission Policy](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Troubleshooting Guide](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured command output with stdout, stderr, exit code, and troubleshooting guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute remote SSH commands against user-specified hosts and return command results or error messages.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
