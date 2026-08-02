## Description: <br>
Debug Linux kernel crashes, kernel panics, vmcore dumps, memory corruption, deadlocks, and ARM64 lock issues using crash, kdump, and related memory-debugging tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[crazyss](https://clawhub.ai/user/crazyss) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, SREs, and kernel engineers use this skill to triage Linux vmcore files, inspect kernel panic evidence, analyze deadlocks and memory faults, and prepare kdump or crash-utility workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Privileged live-kernel tracing, kdump tests, SysRq panic commands, debugfs writes, or boot-configuration changes can disrupt systems. <br>
Mitigation: Use disposable, lab, or approved maintenance systems unless live-host inspection is explicitly authorized with backups, console access, and a rollback plan. <br>
Risk: vmcore files and trace output can contain credentials, keys, process memory, and business data. <br>
Mitigation: Treat dumps and traces as sensitive data; restrict access, use encrypted or approved storage, sanitize before sharing, and securely dispose of raw dumps. <br>
Risk: Kernel crash analysis can produce misleading conclusions when vmlinux, debug symbols, architecture parameters, or vmcore data do not match. <br>
Mitigation: Verify that vmlinux exactly matches the vmcore kernel version, includes debug symbols, and uses the correct architecture-specific crash parameters before relying on findings. <br>
Risk: Interactive crash sessions and broad memory queries can hang an agent session or produce excessive output. <br>
Mitigation: Prefer the bundled non-interactive wrapper workflows and bounded crash commands, then narrow queries when more detail is needed. <br>


## Reference(s): <br>
- [Project homepage](https://github.com/crazyss/linux-kernel-crash-debug) <br>
- [ClawHub skill page](https://clawhub.ai/crazyss/skills/linux-kernel-crash-debug) <br>
- [Crash Utility Documentation](https://crash-utility.github.io/) <br>
- [Crash Utility Whitepaper](https://crash-utility.github.io/crash_whitepaper.html) <br>
- [Linux Kdump Documentation](https://docs.kernel.org/admin-guide/kdump/kdump.html) <br>
- [VMCOREINFO Documentation](https://docs.kernel.org/admin-guide/kdump/vmcoreinfo.html) <br>
- [ARM64 Kdump Documentation](https://docs.kernel.org/arch/arm64/kdump.html) <br>
- [Advanced Commands Reference](references/advanced-commands.md) <br>
- [Agentic Debugging Heuristics](references/agentic-heuristics.md) <br>
- [ARM64 Crash Parameters](references/arm64-crash-params.md) <br>
- [ARM64 Lock Analysis](references/arm64-lock-analysis.md) <br>
- [Debugging Case Studies](references/case-studies.md) <br>
- [Kernel Debug Tools Guide](references/debug-tools-guide.md) <br>
- [Kdump Setup Guide](references/kdump-setup-guide.md) <br>
- [Reference Sources Index](references/sources.md) <br>
- [vmcore File Format](references/vmcore-format.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and crash utility command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include privileged diagnostic commands; wrapper examples limit interactive sessions and large output.] <br>

## Skill Version(s): <br>
1.3.3 (source: server release metadata; artifact frontmatter reports 1.3.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
