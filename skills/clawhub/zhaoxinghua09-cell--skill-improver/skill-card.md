## Description:

Skill Improver diagnoses review findings, applies safe metadata fixes, retests changes, and refuses to fabricate tests, demos, or capability claims.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers use Skill Improver to turn a skill package review's remediation list into real changes and re-evaluate the package. It refuses changes that would fabricate capabilities, tests, demos, or safety claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review rates the release suspicious because of reported documentation-editing behavior and incomplete inspection of some references.

Mitigation: Review the reported out-of-package write risk and broad documentation edits before installing, and do not treat unexamined references as safe.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/skill-improver)
- [Usage guide](references/usage.md)
- [Fixer details](references/fixers.md)
- [Limits and refusals](references/limits.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Files, Code, Shell commands]

**Output Format:** [Markdown findings, package file updates, and Python or shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Changes are limited to eligible metadata fixes; changes to existing documentation require explicit opt-in.]

## Skill Version(s):

1.0.0 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
