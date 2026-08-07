## Description:

Windows-health helps agents diagnose Windows disk pressure and performance issues with read-only PowerShell evidence, Microsoft-aligned cleanup guidance, and explicit authorization gates before deletion or migration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiaoyifu1203](https://clawhub.ai/user/jiaoyifu1203)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and support agents use this skill to inspect Windows storage pressure, startup behavior, and performance symptoms before deciding what to clean, archive, keep, or leave for manual review. It is intended to produce evidence-backed reports and candidate actions, not to make destructive changes without explicit per-path authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic reports can expose local file paths, cache sizes, startup entries, process names, and recent filename shortcuts.

Mitigation: Review the report before sharing it and avoid publishing local diagnostic details that identify private files, applications, or workflows.

Risk: Cleanup, migration, duplicate removal, cloud actions, DISM commands, or reminders can change local or cloud state if approved without review.

Mitigation: Approve only specific proposed actions after checking the exact path, expected effect, recoverability, and rollback notes.

Risk: Windows component cleanup and startup changes can affect system recovery or boot behavior.

Mitigation: Keep WinSxS and administrator-level changes as plan-only guidance unless the user separately confirms the official Microsoft path, permission requirement, and any irreversible effect.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jiaoyifu1203/skills/windowshealth)
- [Microsoft authoritative baseline](artifact/references/microsoft-authoritative.md)
- [Safety and platform boundaries](artifact/references/safety-and-platforms.md)
- [PowerShell scan commands](artifact/references/scan-commands.md)
- [Report, execution, and rollback](artifact/references/report-and-execution.md)
- [cleanmgr command](https://learn.microsoft.com/zh-cn/windows-server/administration/windows-commands/cleanmgr)
- [Storage Sense](https://learn.microsoft.com/zh-cn/windows/configuration/storage/storage-sense)
- [Clean up the WinSxS folder](https://learn.microsoft.com/zh-cn/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder)
- [Clean boot in Windows](https://support.microsoft.com/help/929135)
- [Startup apps in Windows](https://support.microsoft.com/windows/9115d841-735e-488d-e749-9ba301d441e6)
- [Monitor Windows client performance](https://learn.microsoft.com/zh-cn/training/modules/monitor-troubleshoot-windows-client-performance/4-monitor-windows-client-performance)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with inline PowerShell commands and structured recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should distinguish read-only diagnostics, candidate commands, explicit authorization requirements, rollback notes, and evidence limitations.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
