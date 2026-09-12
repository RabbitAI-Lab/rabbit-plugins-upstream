## Description:

Windows server operations toolbox that helps agents diagnose and manage disk usage, IIS, services, updates, performance, security audits, networking, backups, containers, multi-server administration, monitoring, trend prediction, and alerting with PowerShell-centered guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Windows administrators and IT operations teams use this skill to ask an agent for operational diagnostics, audit checks, PowerShell command guidance, and confirmed remediation workflows across Windows Server environments. It is suited to routine server maintenance, incident triage, monitoring setup, compliance checks, and multi-server administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Advanced modules can create scheduled tasks or make persistent operational changes.

Mitigation: Review modules 28, 30, and 31 before installation, test outside production first, require explicit confirmation for changes, and verify scheduled task cleanup afterward.

Risk: Remote multi-server workflows can store credentials and run commands across servers.

Mitigation: Use least-privilege, non-shared credentials; restrict WinRM access; and review each remote command before execution.

Risk: Monitoring and alerting workflows may expose host, metric, threshold, or webhook details.

Mitigation: Store webhook URLs in environment variables, limit access to generated output files, and rotate any webhook that may have been exposed.

## Reference(s):

- [Skill definition and module overview](artifact/SKILL.md)
- [CIS Benchmark checks](artifact/references/compliance/cis-benchmark.yaml)
- [等保 2.0 checks](artifact/references/compliance/dp-2.0.yaml)
- [Monitoring thresholds](artifact/references/thresholds.yaml)
- [Automated remediation guide](artifact/references/modules/module-27-自动化修复向导.md)
- [Performance baseline and trend analysis](artifact/references/modules/module-28-性能基线-&-趋势分析.md)
- [Remote multi-server management](artifact/references/modules/module-30-远程多服务器管理.md)
- [Lightweight scheduled monitoring](artifact/references/modules/module-31-轻量常驻监控.md)
- [Trend prediction](artifact/references/modules/module-32-趋势预测.md)
- [Alert push configuration](artifact/references/modules/module-33-告警推送.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with PowerShell command blocks, configuration snippets, diagnostic summaries, and operational checklists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended for Windows PowerShell 5.1+ workflows; several modules require administrator approval or explicit user confirmation before changes are made.]

## Skill Version(s):

3.3.0 (source: frontmatter and server release evidence, released 2026-09-11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
