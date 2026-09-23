## Description:

Market retrieves validated raw market and quantitative data for A-share, Hong Kong, U.S., commodity, financial-statement, news, flow, limit-up, and technical-indicator workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fize](https://clawhub.ai/user/fize)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and developers use this skill to fetch date-checked market datasets, raw observations, and deterministic technical indicator values before producing their own analysis or reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plaintext HTTP fallback quote paths can expose symbol queries and allow market data to be tampered with in transit.

Mitigation: Use authenticated or TLS-protected market-data sources for trading-critical decisions and cross-check returned source, timestamp, and price fields before relying on results.

Risk: Raw market data, cache entries, local query history, and watchlist-derived data can persist in the skill data directory.

Mitigation: Run the skill in an isolated workspace for sensitive research and periodically clear local data and cache files.

Risk: Third-party provider outages, throttling, or stale data can affect completeness and freshness.

Mitigation: Treat nonzero exits or structured blocking reasons as data unavailability, not as empty market results, and verify important outputs against authoritative sources.

## Reference(s):

- [Market Data Scenarios](references/scenarios.md)
- [ClawHub market skill page](https://clawhub.ai/fize/skills/market)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [JSON market-data documents from shell commands, with human-readable diagnostics on stderr]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large datasets may be persisted locally and returned through compact views with raw file paths.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
