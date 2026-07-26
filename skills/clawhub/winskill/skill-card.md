## Description: <br>
Winskill is a Windows Server operations toolbox that helps agents diagnose disk usage, IIS, services, Windows Update, performance, security logs, registry startup items, storage, networking, certificates, firewall rules, Docker, Kubernetes, and guided repair workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Windows administrators, operations engineers, and support agents use this skill to generate PowerShell-based diagnostic and maintenance guidance for Windows Server environments. It is intended for local server triage, audit, cleanup, and confirmed repair workflows rather than unattended changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Repair and cleanup flows can stop services, reset networking, clear caches, or delete temporary files. <br>
Mitigation: Run diagnosis-only steps first, review the proposed command list and impact, require explicit user confirmation, and schedule changes during a maintenance window. <br>
Risk: Some procedures require administrator privileges on Windows servers and may affect availability. <br>
Mitigation: Limit execution to authorized administrators, confirm backups or restore points where applicable, and avoid production execution without change approval. <br>
Risk: The release makes read-only and offline safety claims that do not cover every repair behavior. <br>
Mitigation: Treat the skill as a repair-capable administrative toolbox and review each generated command before running it. <br>


## Reference(s): <br>
- [Winskill ClawHub skill page](https://clawhub.ai/fyniujin/skills/winskill) <br>
- [Docker Engine on Windows Server documentation](https://docs.docker.com/engine/install/windows-server/) <br>
- [Install kubectl on Windows documentation](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with PowerShell command blocks, tables, and Chinese-language operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes read-only diagnostic flows plus confirmed administrator repair and cleanup procedures.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
