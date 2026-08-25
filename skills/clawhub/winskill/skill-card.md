## Description:

Windows server operations toolbox for disk analysis, cleanup, IIS and service checks, Windows Update diagnostics, performance monitoring, security auditing, compliance checks, repair workflows, and remote multi-server management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Windows administrators and operations engineers use Winskill to ask an agent for PowerShell-based diagnostics, reports, maintenance guidance, and confirm-before-action repair workflows across Windows Server environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repair, cleanup, service, and network commands can interrupt services, remove files, or change host state.

Mitigation: Require an explicit user confirmation step, show the planned commands and affected resources first, and keep an audit trail for any executed action.

Risk: Remote multi-server management may store credentials and run commands across multiple hosts.

Mitigation: Use only approved Windows administrative contexts, avoid stored remote credentials unless accepted by the operator, and scope remote execution to named servers and reviewed commands.

Risk: Security and compliance checks can produce incomplete or environment-specific findings.

Mitigation: Treat generated reports as operational guidance for administrator review rather than authoritative compliance certification.

Risk: Performance baselines and monitoring workflows may create local output or scheduled data collection artifacts.

Mitigation: Confirm collection scope, retention, and output paths before enabling persistent or repeated monitoring.

## Reference(s):

- [ClawHub winskill release page](https://clawhub.ai/fyniujin/skills/winskill)
- [CIS Benchmark compliance checklist](references/compliance/cis-benchmark.yaml)
- [Dengbao 2.0 compliance checklist](references/compliance/dp-2.0.yaml)
- [Automated repair guide module](references/modules/module-27-自动化修复向导.md)
- [Remote multi-server management module](references/modules/module-30-远程多服务器管理.md)
- [System file integrity repair module](references/modules/module-23-系统文件完整性检查与修复（SFC---DISM）.md)
- [Docker and Kubernetes container management module](references/modules/module-26-Docker---K8s-容器管理.md)
- [Docker Engine on Windows Server documentation](https://docs.docker.com/engine/install/windows-server/)
- [kubectl on Windows documentation](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with PowerShell command blocks, checklists, status reports, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some workflows produce local reports or configuration snippets and require explicit confirmation before high-impact actions.]

## Skill Version(s):

3.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
