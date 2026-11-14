## Description:

Stock Screener helps agents run local multi-factor stock filtering, ranking, single-stock scoring, summary statistics, and factor correlation analysis from CSV inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cqdev-ai](https://clawhub.ai/user/cqdev-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to screen trusted CSV stock datasets by technical, fund-flow, and basic valuation factors, then prepare ranked candidate pools for downstream planning. Outputs are analysis aids and should not be treated as investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted CSV inputs or exported CSV files can produce misleading analysis or expose spreadsheet formula risks.

Mitigation: Use CSV files from trusted sources and sanitize or disable formulas before opening exported CSVs in spreadsheet software.

Risk: Stock screening results may be mistaken for investment advice.

Mitigation: Treat outputs as analytical signals for further review and require human decision-making before trading or portfolio actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cqdev-ai/skills/stock-screener)

## Skill Output:

**Output Type(s):** [text, shell commands, CSV files, guidance]

**Output Format:** [Markdown guidance with shell command examples, terminal analysis output, and optional CSV exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on user-provided CSV data with Python standard-library dependencies only.]

## Skill Version(s):

1.0.2 (source: server release evidence, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
