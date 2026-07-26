## Description: <br>
Agent-native CLI guidance for managing Alibaba Cloud ECS instances without public IPs, covering Workbench CLI installation, credential setup, remote commands, file transfer, port forwarding, sessions, and troubleshooting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sdk-team](https://clawhub.ai/user/sdk-team) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to operate Alibaba Cloud ECS instances through the Workbench CLI, especially for instances without public IP addresses. It helps with remote command execution, file transfer, port forwarding, instance listing, credential setup, session management, and troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installer commands use remote shell scripts for Linux, macOS, and Windows setup. <br>
Mitigation: Review installer source before running curl-to-bash or irm-to-iex commands, and install only when Workbench CLI access is intended. <br>
Risk: The skill helps operate Alibaba Cloud ECS resources, including remote commands, file transfer, and port forwarding. <br>
Mitigation: Use least-privilege RAM policies, avoid long-lived AK/SK credentials where possible, and stop Workbench sessions or port forwards when finished. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-workbench-cli) <br>
- [Workbench CLI Linux and macOS installer](https://workbench-cli.oss-cn-hangzhou.aliyuncs.com/install.sh) <br>
- [Workbench CLI Windows installer](https://workbench-cli.oss-cn-hangzhou.aliyuncs.com/install.ps1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, configuration examples, JSON snippets, and troubleshooting tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may include commands that operate cloud resources and should be reviewed before execution.] <br>

## Skill Version(s): <br>
0.0.1-beta.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
