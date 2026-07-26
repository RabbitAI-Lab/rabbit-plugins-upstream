## Description: <br>
Goto Cloudserver Manager helps agents operate cloud servers across Alibaba Cloud, Tencent Cloud, and Huawei Cloud, including database installation, schema creation, monitoring checks, and health reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[feixuelingcloud](https://clawhub.ai/user/feixuelingcloud) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and small infrastructure teams use this skill to inspect cloud server status, prepare databases, apply database schemas, manage firewall and monitoring setup, and generate operational reports through an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud credentials could be exposed or overused because the skill handles provider access keys and remote execution channels. <br>
Mitigation: Use least-privilege, short-lived credentials, inject secrets from a managed secret store or scoped environment, and avoid pasting production secrets into chat. <br>
Risk: Database restores, reboots, firewall changes, and security group changes can disrupt production infrastructure. <br>
Mitigation: Review every generated plan before confirmation, require backups and a rollback path for production changes, and keep high-impact actions behind explicit human approval. <br>
Risk: A local executor fallback can broaden the execution surface when the skill is connected to real infrastructure. <br>
Mitigation: Disable or remove the local executor fallback before using the skill against real cloud accounts or production servers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/feixuelingcloud/skills/goto-cloudserver-manager) <br>
- [README](artifact/README.md) <br>
- [Policy configuration](artifact/config/policies.yaml) <br>
- [Provider configuration](artifact/config/providers.yaml) <br>
- [Node Exporter install guide](artifact/monitoring/node_exporter/install_guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, execution plans, generated SQL or schema content, configuration updates, and shell or PowerShell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May trigger API calls or remote command execution when the host agent is configured with cloud credentials and the user confirms write operations.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata, SKILL.md frontmatter, pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
