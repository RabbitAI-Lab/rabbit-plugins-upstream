## Description:

Audits a repository for bugs, security risks, load issues, missing tests, performance problems, and unnecessary code, prioritizing the most important findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dietrichgebert](https://clawhub.ai/user/dietrichgebert)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to audit a repository or selected area and receive prioritized, concrete findings with suggested fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A whole-repository audit may expose sensitive source code to the active agent context.

Mitigation: Use only on repositories the agent is authorized to read; limit the audit scope when sensitive files are not needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dietrichgebert/skills/ponytail-audit)
- [Project homepage](https://github.com/DietrichGebert/ponytail)

## Skill Output:

**Output Type(s):** [Analysis, Text]

**Output Format:** [Markdown audit report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prioritized findings with concrete cases and fixes; at most 20 findings. No code changes.]

## Skill Version(s):

5.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
