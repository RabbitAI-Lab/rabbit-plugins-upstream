## Description:

code-polish performs pre-release code review by running validation checks, analyzing diffs through cleanliness, design, efficiency, and side-effect-gating lenses, validating findings, and preparing approved fixes before commit, push, or release.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill before committing, pushing, or releasing code to run project checks, inspect changed files, and receive a validated review report. When approved, it can make targeted cleanup and fix edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may edit a local repository during automated-check cleanup before the later approval point described for review findings.

Mitigation: Use it in a clean working tree or after backing up or stashing important work, and inspect the resulting diff before accepting changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/code-polish)
- [Homepage](https://github.com/tenequm/skills/tree/main/skills/polish)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown review report with file references, recommendations, and optional targeted code edits or shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify repository files during automated-check cleanup or after the user approves fixes]

## Skill Version(s):

2.4.2 (source: server evidence, frontmatter metadata, and changelog released 2026-08-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
