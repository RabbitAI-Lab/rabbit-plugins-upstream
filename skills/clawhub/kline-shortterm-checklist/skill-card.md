## Description:

This skill helps agents apply a disciplined A-share short-term stock screening checklist using the 96 principle, 2:30 eight-layer screening, bottom K-line patterns, trend checks, and risk-control rules, with optional market-data scripts and Wind MCP-assisted checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handm-735](https://clawhub.ai/user/handm-735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to screen A-share short-term candidates, review a specific ticker against checklist rules, and produce structured buy-before-or-hold review artifacts. The outputs are analytical aids and should not be treated as investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional localhost workbench can trigger file-writing analysis scripts through an unauthenticated local endpoint.

Mitigation: Run the workbench only in a trusted local environment, keep it bound to localhost, stop the server when finished, and review generated files before using them.

Risk: The skill fetches public market data and the security evidence notes disabled certificate checks for some data fetching.

Mitigation: Treat fetched data as untrusted analytical input, verify material results against trusted market-data sources, and avoid making trading decisions from generated output alone.

Risk: The skill produces stock-screening analysis that may be mistaken for investment advice.

Mitigation: Use the reports as checklist-based analysis only; require human review, independent validation, position sizing, and stop-loss discipline before any real trade.

## Reference(s):

- [K-line Short-Term Checklist Reference](references/checklist.md)
- [K-line Pattern Reference](references/kline_patterns.md)
- [ClawHub Skill Page](https://clawhub.ai/handm-735/skills/kline-shortterm-checklist)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell command sequences, JSON data files, and HTML dashboard reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write candidates, market-data, announcement-check, intraday-strength, and HTML report files in the working directory.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter lists 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
