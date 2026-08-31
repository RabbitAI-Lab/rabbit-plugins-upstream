## Description:

Connects an agent to Xiaoshi/Shizixi public financial data through user-confirmed email authentication for market data, historical data, PIT macro data, news events, financials, factors, backtests, and quantitative research, without trade execution or investment orders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pilot1799](https://clawhub.ai/user/pilot1799)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users, developers, and financial researchers use this skill to authenticate with Xiaoshi/Shizixi and query public financial datasets for market research, reports, point-in-time analysis, factors, and backtesting. It is intended for data and research workflows, not trading, order placement, or investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email addresses, authentication responses, and financial-data query details may be exposed to Xiaoshi/Shizixi as part of normal use.

Mitigation: Confirm the user trusts Xiaoshi/Shizixi before installation or authentication, and send only the fields required for the current task.

Risk: API keys, verification codes, or session tokens could be exposed if stored in ordinary files, logs, screenshots, reports, or long-term chat memory.

Mitigation: Use the host's protected secret storage for cross-session use; otherwise keep credentials only for the current session and never echo them in user-facing output.

Risk: Financial research output may be mistaken for investment advice or trade execution.

Mitigation: Keep outputs limited to data and research, do not place or suggest orders, and state when results are observations rather than advice.

Risk: Market, PIT, or historical results can be misleading if dates, coverage, revisions, or adjustment modes are not checked.

Mitigation: Report relevant version, date range, market, currency, unit, time zone, adjustment mode, as_of timestamp, missing coverage, and revision evidence for substantive research.

## Reference(s):

- [Xiaoshi homepage](https://www.shizixi.com/)
- [Xiaoshi API bootstrap](https://api.shizixi.com/api/v3/agent/bootstrap)
- [Capabilities](references/capabilities.md)
- [Data, PIT, Download, and Error Contracts](references/data-and-safety-contracts.md)
- [Host Compatibility](references/host-compatibility.md)
- [Registration and Login](references/registration-and-login.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional JSON, code, shell command, and API request snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should distinguish verified platform data, publisher evidence, model inference, missing coverage, dates, row counts, currencies, units, time zones, adjustment modes, as_of timestamps, and revision times when relevant.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
