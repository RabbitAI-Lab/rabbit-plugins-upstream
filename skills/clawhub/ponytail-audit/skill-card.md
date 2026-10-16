## Description:

Reviews a repository for bugs, security issues, scaling risks, missing tests, performance problems, and unnecessary code, prioritizing actionable findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dietrichgebert](https://clawhub.ai/user/dietrichgebert)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review a repository or selected code for concrete defects, security and scaling risks, missing tests, slow paths, and opportunities to simplify code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A whole-repository audit may summarize secrets or private material in its report.

Mitigation: Limit the audit scope to code you are comfortable sharing, and review the report before distributing it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dietrichgebert/skills/ponytail-audit)
- [Project homepage listed in skill metadata](https://github.com/DietrichGebert/ponytail)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown audit report with prioritized findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to 20 numbered findings, each with a concrete case, suggested fix, and consequence of inaction; reports assumed load and areas not checked. Does not modify code.]

## Skill Version(s):

5.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
