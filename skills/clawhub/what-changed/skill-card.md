## Description:

Explain material semantic differences between versions or snapshots for policies, procedures, contracts, requirements, datasets, configurations, APIs, schemas, reports, and other evolving artifacts, focusing on impact rather than raw line diffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external reviewers, developers, and operators use this skill to compare versions of policies, contracts, datasets, schemas, APIs, configurations, or reports and identify material semantic changes, impact, and follow-up actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may provide sensitive contracts, policies, datasets, or other documents for comparison.

Mitigation: Provide only documents intended for agent analysis and handle outputs according to the confidentiality requirements of those documents.

Risk: Downstream impact analysis may be incomplete or inaccurate when organizational dependencies are unknown.

Mitigation: Review inferred impacts before acting and inspect downstream artifacts or processes when the user needs higher-confidence impact analysis.

## Reference(s):

- [Change Severity Heuristics](references/change-severity.md)
- [ClawHub Skill Page](https://clawhub.ai/raguets/skills/what-changed)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or structured text with change summaries, severity labels, evidence locations, and action lists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prioritizes semantic impact over raw line, row, or page volume and bounds uncertain downstream effects.]

## Skill Version(s):

1.0.0 (source: server release evidence; artifact frontmatter metadata version is 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
