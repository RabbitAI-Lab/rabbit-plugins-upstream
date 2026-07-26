## Description: <br>
Automated Linux server patching and Docker container updates for OpenClaw, with PatchMon integration for host detection and support for Ubuntu, Debian, RHEL-family, Amazon Linux, CentOS, and SUSE systems. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jgm2025](https://clawhub.ai/user/jgm2025) <br>

### License/Terms of Use: <br>
MIT License <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to patch Linux hosts over SSH, query PatchMon for machines needing updates, and optionally update Docker Compose workloads during maintenance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make broad infrastructure changes across hosts, including package upgrades, Docker image pulls, container recreation, and pruning. <br>
Mitigation: Use dry-run mode first, require manual confirmation before applying Docker or fleet-wide changes, and restrict execution to explicit host allowlists and maintenance windows. <br>
Risk: The security scan summary identifies unsafe credential, sudo, and command-handling patterns that users should review carefully. <br>
Mitigation: Use a dedicated low-privilege PatchMon account, verified HTTPS, tightly scoped sudo or root-owned wrapper scripts, SSH key authentication, and hardened credential storage. <br>
Risk: Only Ubuntu is described as fully tested; other supported distributions are documented as untested. <br>
Mitigation: Test unverified distributions in a non-production environment and validate the selected package manager workflow before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jgm2025/skills/linux-patcher) <br>
- [PatchMon project](https://github.com/PatchMon/PatchMon) <br>
- [PatchMon documentation](https://docs.patchmon.net) <br>
- [PatchMon integration guide](references/patchmon-setup.md) <br>
- [Setup guide](SETUP.md) <br>
- [Workflow diagrams](WORKFLOWS.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown] <br>
**Output Format:** [Markdown guidance with bash commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or run patching workflows that affect remote hosts, sudo-managed package managers, and Docker Compose services.] <br>

## Skill Version(s): <br>
3.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
