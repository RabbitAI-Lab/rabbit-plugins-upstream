## Description:

Audit the whole repo for over-engineering. A ranked list of what to delete, simplify, or replace with stdlib or native features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dietrichgebert](https://clawhub.ai/user/dietrichgebert)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to identify and rank unnecessary complexity across a repository, including dead code, redundant abstractions, and opportunities to use standard-library or native features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A complexity-only audit may miss security, correctness, or performance problems.

Mitigation: Run separate security, correctness, and performance reviews when those concerns matter.

## Reference(s):

- [Project homepage](https://github.com/DietrichGebert/ponytail)
- [ClawHub skill listing](https://clawhub.ai/dietrichgebert/skills/ponytail-audit)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ranked one-line findings with paths and suggested simplifications, ending with estimated line and dependency reductions; no files are changed.]

## Skill Version(s):

4.10.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
