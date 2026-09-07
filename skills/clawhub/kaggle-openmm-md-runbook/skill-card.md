## Description:

Runbook, registry, and static checker for planning, executing, debugging, and handing off long OpenMM molecular dynamics runs on Kaggle's free P100 GPU tier.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and agents use this skill to run and troubleshoot OpenMM molecular dynamics workflows on Kaggle, including checkpoint/resume planning, known failure lookup, and pre-push static checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented supervisor can perform unattended Kaggle monitoring and relaunch work if a user starts it.

Mitigation: Start the supervisor only on explicit user request, run exactly one copy, and stop on completion or after repeated failures.

Risk: Runtime bootstrapping may rely on mutable micromamba endpoints or floating helper dependencies.

Mitigation: Prefer pinned, checksum-verified micromamba releases and dependency lock files outside short-lived Kaggle sessions.

Risk: Kaggle credentials or other secrets could be exposed when working with public kernels.

Mitigation: Do not read, print, copy, or embed credentials; run the static preflight secret gate and a real secret scanner before pushing a public kernel.

Risk: Incorrect molecular dynamics parameters or stale assumptions can waste GPU quota or produce invalid runs.

Mitigation: Fetch facts from the registry by stable IDs, run the preflight checker and selftest, and review commands before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/kaggle-openmm-md-runbook)
- [RUNBOOK.md](RUNBOOK.md)
- [Operations Quick Reference](references/operations.md)
- [Traps & API Matrix](references/traps-and-api-matrix.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, Python snippets, and JSON registry lookups]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a local registry query CLI and static preflight checks; live Kaggle operations require explicit user action.]

## Skill Version(s):

1.1.4 (source: server release metadata; packaged frontmatter and _meta.json report 1.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
