## Description: <br>
Control remote Windows machines via SSH for command execution, GPU status checks, script runs, and file transfers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiaoyaner0201](https://clawhub.ai/user/xiaoyaner0201) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to administer a configured Windows host over SSH, including running commands, checking NVIDIA GPU status with nvidia-smi, and moving files with SCP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad remote Windows command execution and file-transfer capability. <br>
Mitigation: Use a dedicated least-privilege SSH key and account, avoid Administrator unless required, and review destructive commands and transfers before execution. <br>
Risk: The SSH and SCP scripts disable host-key checking, which weakens remote host identity verification. <br>
Mitigation: Remove StrictHostKeyChecking=no before deployment and rely on known_hosts verification for the intended Windows host. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xiaoyaner0201/skills/windows-remote) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/xiaoyaner0201) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Text] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces command guidance for SSH, SCP, and nvidia-smi workflows against a user-configured Windows host.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
