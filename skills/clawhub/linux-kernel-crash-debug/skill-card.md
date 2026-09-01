## Description:

Debug Linux kernel crashes with evidence-first vmcore analysis, the crash utility, and memory/concurrency debugging workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crazyss](https://clawhub.ai/user/crazyss)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and kernel engineers use this skill to analyze Linux kernel panics, vmcores, lockups, OOM events, memory corruption, deadlocks, and related crash signatures. It helps preserve evidence, validate symbols and dump quality, run bounded crash-utility workflows, and produce testable root-cause reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: vmcore files and trace output may contain credentials, keys, process memory, hostnames, paths, and customer data.

Mitigation: Use the skill only for authorized crash work, keep dumps and derived output access-controlled, and do not upload or share them without explicit approval and approved sanitization.

Risk: Live-host mutations such as service changes, boot configuration changes, debugfs or procfs writes, module changes, and live tracing can disrupt systems or expose runtime data.

Mitigation: Default to offline read-only analysis; require explicit approval for the exact host and action, define a narrow time-bounded capture, record baseline state, and apply cleanup in the same session.

Risk: SysRq crash actions and kdump tests deliberately panic or reboot a host.

Mitigation: Agents should not execute deliberate panic or kdump test actions; hand the final trigger to authorized personnel following an approved drill with console access, backups, workload evacuation, and rollback.

Risk: Interactive crash sessions or broad crash queries can block an agent or produce excessive output.

Mitigation: Use the bundled agent-crash wrapper for non-interactive execution with timeouts and output truncation, then narrow follow-up queries as needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/crazyss/skills/linux-kernel-crash-debug)
- [Project Homepage](https://github.com/crazyss/linux-kernel-crash-debug)
- [Evidence-First Kernel Crash Workflow](references/evidence-first-workflow.md)
- [Agentic Debugging Heuristics](references/agentic-heuristics.md)
- [Debugging Case Studies](references/case-studies.md)
- [Kernel Debug Tools Guide](references/debug-tools-guide.md)
- [Kdump Setup Guide](references/kdump-setup-guide.md)
- [vmcore File Format](references/vmcore-format.md)
- [ARM64 Crash Parameters](references/arm64-crash-params.md)
- [ARM64 Lock Analysis](references/arm64-lock-analysis.md)
- [Advanced Commands Reference](references/advanced-commands.md)
- [References Index](references/sources.md)
- [Crash Utility Documentation](https://crash-utility.github.io/)
- [Crash Utility Whitepaper](https://crash-utility.github.io/crash_whitepaper.html)
- [Linux Kernel Kdump Documentation](https://docs.kernel.org/admin-guide/kdump/kdump.html)
- [Linux Kernel VMCOREINFO Documentation](https://docs.kernel.org/admin-guide/kdump/vmcoreinfo.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell and crash command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes bounded crash-wrapper command suggestions and root-cause reporting guidance.]

## Skill Version(s):

1.4.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
