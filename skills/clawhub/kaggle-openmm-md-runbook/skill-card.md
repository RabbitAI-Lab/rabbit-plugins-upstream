## Description:

Guides agents through planning, executing, debugging, calibrating, and handing off long OpenMM molecular dynamics runs on Kaggle free GPU sessions, with a fact registry, static preflight checker, and operational runbook.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and agent operators use this skill to run OpenMM molecular dynamics workflows on Kaggle, avoid known GPU/session traps, validate a positive-control calibration, and retrieve grounded rule, trap, error, and parameter facts by stable ID.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kaggle commands and supervisor workflows can consume GPU quota or mutate kernels and datasets.

Mitigation: Review Kaggle commands before use, replace example owner and slug values with the user's own resources, start remote mutations only on explicit instruction, and run only one supervisor loop.

Risk: Kaggle credentials may be mishandled if copied into project files or command output.

Mitigation: Keep credentials in the standard Kaggle config, avoid printing or relocating keys, and use the documented preflight secret checks before publishing kernel files.

Risk: Dependency drift can reduce reproducibility or break safety-critical OpenMM behavior.

Mitigation: Use the documented OpenMM pin, pinned Kaggle CLI, SHA256-verified micromamba bootstrap, and locked dependencies for reproducible or sensitive work.

Risk: The README's printed expected SKILL.md hash may be stale for this release.

Mitigation: Do not rely on that printed hash until the publisher updates it; compare against server-provided release file hashes or fetch a fresh copy.

## Reference(s):

- [README](README.md)
- [Runbook](RUNBOOK.md)
- [Operations Quick Reference](references/operations.md)
- [Traps and API Matrix](references/traps-and-api-matrix.md)
- [Calibration Registry](registry/calibration.json)
- [Rules Registry](registry/rules.json)
- [Traps Registry](registry/traps.json)
- [Errors Registry](registry/errors.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash and Python snippets, plus optional JSON diagnostics from bundled query and preflight scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill is documentation-first; local scripts can provide static preflight results, registry lookups, selftests, and append-only lesson-log records.]

## Skill Version(s):

1.2.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
