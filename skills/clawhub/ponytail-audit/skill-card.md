## Description:

Audits a whole repository for over-engineering and ranks opportunities to delete, simplify, or replace code with standard-library or native features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dietrichgebert](https://clawhub.ai/user/dietrichgebert)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to identify and prioritize repo-wide complexity reductions without modifying files. It produces a read-only list of possible deletions, replacements, and simplifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested deletions could remove code used through dynamic references or tests.

Mitigation: Review proposed deletions and check references across the repository before applying changes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dietrichgebert/skills/ponytail-audit)
- [Skill homepage](https://github.com/DietrichGebert/ponytail)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Numbered, ranked one-line findings with tags, suggested replacements, and file paths; a final estimate of lines and dependencies removable, or a no-findings message.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only recommendations; no files are changed.]

## Skill Version(s):

4.12.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
