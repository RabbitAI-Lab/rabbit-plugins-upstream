## Description: <br>
天翼云 CLI 工具帮助开发者和运维人员通过命令行管理天翼云资源，覆盖 ECS、VPC、EBS、ELB、CCE、Redis、MySQL、Kafka、IAM、APM、CFW 等 32+ 个服务模块、943+ 个 API 和 898+ 个命令。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fengyucn](https://clawhub.ai/user/fengyucn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operations teams use this skill to install and operate ctyun-cli, configure Tianyi Cloud credentials, and run commands for resource inventory, monitoring, pricing, networking, storage, container, database, IAM, and firewall tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The CLI uses Tianyi Cloud access keys and can operate on cloud resources. <br>
Mitigation: Use least-privilege credentials, prefer environment variables or protected profiles, and install the skill only in environments intended for Tianyi Cloud administration. <br>
Risk: Secrets or account details may appear in shell history, saved configuration, or debug logs. <br>
Mitigation: Avoid passing secrets directly as command arguments, protect saved profile and shell startup files, and review debug logs before sharing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fengyucn/skills/ctyun) <br>
- [PyPI package](https://pypi.org/project/ctyun-cli/) <br>
- [Project homepage](https://github.com/fengyucn/ctyun-cli) <br>
- [Issue tracker](https://github.com/fengyucn/ctyun-cli/issues) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes CLI installation, authentication, command examples, and service-specific usage notes.] <br>

## Skill Version(s): <br>
1.30.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
