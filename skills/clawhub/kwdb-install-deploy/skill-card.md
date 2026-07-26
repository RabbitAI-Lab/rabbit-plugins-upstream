## Description: <br>
Triggered when the user wants to install or deploy KaiwuDB (kwdb, kaiwudb). Helps users complete script-based deployment of KaiwuDB clusters, including configuration file modification, installation command execution, cluster initialization, and status checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kwdb](https://clawhub.ai/user/kwdb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations engineers use this skill to install or deploy KaiwuDB on Linux systems, including single-node and cluster deployments. It guides configuration confirmation, installation command execution, initialization, status checks, and failure handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: KaiwuDB deployment may require privileged access such as root, sudo, docker-group membership, or passwordless SSH. <br>
Mitigation: Install only on intended deployment systems and use a controlled deployment account with the narrowest practical privileges. <br>
Risk: A user-provided KaiwuDB installation package could be untrusted or malformed. <br>
Mitigation: Use a trusted KaiwuDB package and verify its checksum or source when available before running deployment commands. <br>
Risk: Incorrect ports, IP addresses, data directories, or security-mode settings can break deployment or expose services unexpectedly. <br>
Mitigation: Confirm every deployment parameter with the user before execution, including displayed defaults. <br>
Risk: Repeated automatic retries after a failed installation can compound configuration or environment problems. <br>
Mitigation: Read the installation logs, report the error and likely causes, exit the installation flow, and wait for explicit user instructions before retrying. <br>


## Reference(s): <br>
- [KaiwuDB Script Deployment Guide](references/installation_guide.md) <br>
- [KaiwuDB Common Issues and Solutions](references/troubleshooting.md) <br>
- [KWDB Install Deploy on ClawHub](https://clawhub.ai/kwdb/skills/kwdb-install-deploy) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompts the user to confirm deployment parameters before execution and reports installation failures from logs.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
