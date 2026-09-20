## Description:

Checks restaurant dish cost and yield tables by recalculating row arithmetic, totals, duplicate rows, blanks, and negative quantities or amounts, with source-backed findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Restaurant finance and operations staff use this skill during month-end close, reconciliation, or inventory review to check dish cost and yield tables for arithmetic, total, duplicate, blank, and negative-value issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The output is arithmetic and table validation, not financial, tax, inventory, or operational advice.

Mitigation: Review findings against source records and qualified business judgment before acting on them.

Risk: Incomplete or malformed input can prevent the checker from reaching a conclusion.

Mitigation: Provide the full table with headers and use the missing-material messages to correct inputs before relying on results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/restaurant-food-cost-check-free)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Human-readable text or JSON results from a local Node.js command; agent responses may summarize those results in Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows; insufficient input reports missing material instead of producing a conclusion.]

## Skill Version(s):

1.0.43 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
