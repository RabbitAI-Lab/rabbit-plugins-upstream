## Description:

Helps agents write, validate, and run quantum circuits using Quantinuum's Guppy language, the Selene emulator, TKET compile checks, and guarded Nexus workflow guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arunnadarasa](https://clawhub.ai/user/arunnadarasa)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to author Guppy v1 quantum kernels, run Selene emulator shots, manage parameter sweeps, and prepare validation evidence. It also gives guarded guidance for optional Quantinuum Nexus and TKET workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes billable Quantinuum Nexus and hardware-job guidance alongside local Selene emulator workflows.

Mitigation: Require explicit confirmation before login, cost probes, qnx.start_*_job calls, project changes, role changes, or any hardware/emulator submission; set max_cost and a total sweep budget before execution.

Risk: Nexus workflows may use credentials or persistent tokens.

Mitigation: Keep tokens out of shared workspaces and artifacts, use environment or session storage where possible, and clear local credentials after use.

Risk: Quantum execution evidence can be misleading if job status, shot count, seed, backend, or cost context is omitted.

Mitigation: Record execution metadata with results, distinguish emulator from hardware, report non-completed jobs plainly, and avoid making verification claims without supporting evidence.

## Reference(s):

- [Guppy language](references/guppy-language.md)
- [Guppy v1 migration](references/guppy-v1-migration.md)
- [Selene runtime](references/selene-runtime.md)
- [Driver pattern: parameterized kernels](references/driver-pattern.md)
- [Circuit patterns](references/circuit-patterns.md)
- [Parameter sweeps](references/sweep-runner.md)
- [pytket / TKET compile lane](references/pytket.md)
- [Quantinuum Nexus jobs](references/nexus-jobs.md)
- [Nexus accounts and quotas](references/nexus-admin.md)
- [Evidence integrity](references/evidence-integrity.md)
- [Cross-platform validation](references/cross-platform-validation.md)
- [selene_run schema](references/selene-run-schema.md)
- [Quantinuum docs corpus](references/quantinuum-docs-corpus.md)
- [Unified stack cheat sheet](references/stack-cheatsheet.md)
- [ClawHub skill page](https://clawhub.ai/arunnadarasa/skills/quantum)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code, shell commands, and occasional JSON schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include runnable Python snippets and result-schema guidance; Nexus or hardware actions require explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
