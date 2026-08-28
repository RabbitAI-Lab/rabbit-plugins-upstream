## Description:

Pre-release code review skill that runs project checks, reviews diffs for cleanliness, design, efficiency, and side-effect-gating issues, validates findings, and fixes approved issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill before release, commit, or push to run validation, inspect changed code for actionable issues, and optionally apply approved fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run project checks and alter repository files during its fix phase.

Mitigation: Use it in a controlled workspace and approve fixes only after reviewing the reported findings and intended commands.

Risk: Security evidence says the written instructions exceed the narrow declared read-only git allowlist.

Mitigation: Review command and file-edit permissions before enabling the skill in a repository.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/code-polish)
- [Project homepage from ClawHub metadata](https://github.com/tenequm/skills/tree/main/skills/polish)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown review report with file references, recommendations, and optional code edits after approval]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs project validation before review; security evidence recommends confirming edit behavior and tool permissions before use.]

## Skill Version(s):

2.6.0 (source: evidence.release.version, SKILL.md metadata, CHANGELOG released 2026-08-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
