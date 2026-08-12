## Description:

Generates evidence-based Skill portfolio audits, privacy classifications, consolidation recommendations, roadmaps, and a dependency-linked execution queue without modifying audited Skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Skill maintainers use this skill to inventory Skill portfolios, identify duplicates and stale versions, classify public sharing risk, and prioritize merge, split, maintenance, or publishing work. It is intended for read-only audit recommendations plus a separate dependency-linked task ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit may inspect private project files, memories, logs, or conversation history while assessing portfolio frequency and sharing risk.

Mitigation: Set a clear scan scope before running the skill and review generated findings before sharing them outside the workspace.

Risk: The persistent execution queue writes to a separate task ledger outside the audited Skills.

Mitigation: Choose an explicit ledger location and review task-ledger changes before treating recommendations as accepted work.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown report with scorecard tables, sharing classifications, roadmap sections, risk notes, and task ledger guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces recommendations and a persistent execution queue; it does not modify, delete, publish, or execute audited Skills.]

## Skill Version(s):

1.1.2 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
