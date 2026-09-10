## Description:

What Changed helps agents explain material semantic differences between versions or snapshots and assess why those differences matter across policies, procedures, contracts, requirements, datasets, configurations, APIs, schemas, reports, and other evolving artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and analysts use this skill when they need an agent to compare evolving artifacts and explain meaningful changes, impact, severity, and affected downstream processes rather than produce a raw diff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Comparisons may involve sensitive contracts, policies, procedures, or business data.

Mitigation: Provide only the files and organizational context needed for the comparison, and review outputs before sharing them.

Risk: Impact may be uncertain when downstream dependencies or organizational context are missing.

Mitigation: Label uncertain downstream impact as potential and gather only the additional context needed to bound the impact.

## Reference(s):

- [Change Severity Heuristics](references/change-severity.md)
- [Overpowered suite](https://github.com/raguets/overpowered)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown change-impact report with evidence locations and a short action list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prioritizes semantic impact, severity, affected artifacts or processes, and bounded uncertainty over raw textual differences.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
