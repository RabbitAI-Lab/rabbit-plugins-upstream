## Description:

Reviews code diffs for over-engineering and suggests deletions or simpler replacements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dietrichgebert](https://clawhub.ai/user/dietrichgebert)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to spot unnecessary complexity in code diffs and identify what to remove or simplify.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: This narrow review can miss correctness, security, and performance issues.

Mitigation: Run a separate review for correctness, security, and performance; do not rely on this skill as the sole review pass.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dietrichgebert/skills/ponytail-review)
- [Project homepage](https://github.com/DietrichGebert/ponytail)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Numbered, single-line findings with locations and a net-lines estimate, or a brief all-clear]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review only; does not apply fixes.]

## Skill Version(s):

4.13.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
