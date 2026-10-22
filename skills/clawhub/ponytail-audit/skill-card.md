## Description:

Audits a repository for bugs, security risks, load issues, missing tests, performance problems, and unnecessary code, prioritizing the most important findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dietrichgebert](https://clawhub.ai/user/dietrichgebert)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review a repository for concrete defects, security and data-loss risks, load limits, missing tests, and code that can be simplified.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit reads broadly across a repository, including sensitive or business-critical code.

Mitigation: Grant access only to code intended for review and check the report before sharing it.

Risk: An incorrect finding could lead to an unnecessary or harmful change.

Mitigation: Require a concrete failing case for each finding and review proposed fixes before applying them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dietrichgebert/skills/ponytail-audit)
- [Project homepage (listed in skill metadata)](https://github.com/DietrichGebert/ponytail)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A read-only, prioritized audit report with up to 20 numbered findings, concrete cases, and suggested fixes.]

## Skill Version(s):

5.3.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
