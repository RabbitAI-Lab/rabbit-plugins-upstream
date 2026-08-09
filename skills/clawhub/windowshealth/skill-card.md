## Description:

Windows-health helps agents diagnose Windows storage, performance, startup, and cleanup issues using read-only PowerShell evidence and Microsoft-aligned safety gates before any delete, archive, migration, DISM, or reminder action.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiaoyifu1203](https://clawhub.ai/user/jiaoyifu1203)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support agents, and Windows users use this skill to produce evidence-based disk, cache, startup, and performance diagnostics before proposing cleanup or archival actions. It is intended for Windows and WSL troubleshooting workflows where deletion, migration, startup changes, DISM commands, and reminders require explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local diagnostics may expose process names, startup entries, recent shortcut names, cache paths, and large-file paths.

Mitigation: Run scans only in trusted local contexts and redact generated reports before sharing them outside the diagnostic workflow.

Risk: Generated cleanup commands could remove or alter data if executed without careful review.

Mitigation: Treat commands as proposals, confirm exact paths and action types, and require explicit authorization before deletion, migration, startup changes, reminders, or DISM actions.

Risk: Administrator-level DISM, WinSxS, startup, and system-service changes can have system-wide or irreversible effects.

Mitigation: Keep administrator actions in plan-only guidance unless separately confirmed; analyze component store state before cleanup and call out irreversible ResetBase behavior.

Risk: Cloud archive workflows can confuse local downloaded copies with cloud-retained originals.

Mitigation: Verify OneDrive or cloud state, write a manifest, confirm sync, and distinguish local-space release from deleting cloud archive data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jiaoyifu1203/skills/windowshealth)
- [Microsoft authoritative baseline](artifact/references/microsoft-authoritative.md)
- [Safety and platform boundaries](artifact/references/safety-and-platforms.md)
- [PowerShell scan commands](artifact/references/scan-commands.md)
- [Report, execution, and rollback](artifact/references/report-and-execution.md)
- [Windows cleanmgr command](https://learn.microsoft.com/zh-cn/windows-server/administration/windows-commands/cleanmgr)
- [Automating Disk Cleanup Tool](https://learn.microsoft.com/zh-cn/troubleshoot/windows-server/backup-and-storage/automating-disk-cleanup-tool)
- [Windows Storage Sense](https://learn.microsoft.com/zh-cn/windows/configuration/storage/storage-sense)
- [Clean up the WinSxS folder](https://learn.microsoft.com/zh-cn/windows-hardware/manufacture/desktop/clean-up-the-winsxs-folder)
- [Clean boot support guidance](https://support.microsoft.com/help/929135)
- [Startup apps support guidance](https://support.microsoft.com/windows/9115d841-735e-488d-e749-9ba301d441e6)
- [Monitor Windows client performance](https://learn.microsoft.com/zh-cn/training/modules/monitor-troubleshoot-windows-client-performance/4-monitor-windows-client-performance)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, Configuration]

**Output Format:** [Markdown diagnostic reports with inline PowerShell command blocks and explicit candidate actions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first workflow; destructive or state-changing commands are proposals that require explicit per-path confirmation.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
