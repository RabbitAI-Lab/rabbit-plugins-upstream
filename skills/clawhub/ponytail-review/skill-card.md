## Description:

Reviews code diffs for unnecessary complexity and suggests concise ways to remove it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dietrichgebert](https://clawhub.ai/user/dietrichgebert)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to identify code, dependencies, and abstractions they can remove from a diff without applying changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A complexity-only review can miss correctness, security, and performance issues.

Mitigation: Run a separate general code review for those issues before accepting changes.

## Reference(s):

- [Project homepage](https://github.com/DietrichGebert/ponytail)
- [ClawHub skill listing](https://clawhub.ai/dietrichgebert/skills/ponytail-review)

## Skill Output:

**Output Type(s):** [Text, Code review guidance]

**Output Format:** [Plain text, one line per finding]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings identify a location and a simpler replacement, followed by an estimated net line reduction; if nothing needs cutting, reports that the diff is already lean.]

## Skill Version(s):

4.10.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
