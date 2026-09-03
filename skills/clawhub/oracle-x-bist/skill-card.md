## Description:

Read and analyze Borsa Istanbul equities, TEFAS funds, KAP disclosures, VIOP futures, and Turkish macro data with inflation-adjusted returns and delayed prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yigtwxx](https://clawhub.ai/user/yigtwxx)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and external users use this skill to answer Turkish-market questions with BIST, TEFAS, KAP, VIOP, ownership, restrictions, calendar, and macro context. It guides agents to use built-in market rules offline and call a trusted Oracle-X instance when current or historical endpoint data is needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: BIST quotes from endpoint-backed data are delayed and can be mistaken for live prices.

Mitigation: Report the delay and avoid presenting endpoint-backed quotes as live trading data.

Risk: Endpoint-backed queries and radar scans are sent to ORACLE_X_URL.

Mitigation: Set ORACLE_X_URL only to a trusted Oracle-X instance and report clearly when no instance is reachable.

Risk: VIOP scan ranges can be mistaken for margin-call prices.

Mitigation: State that public data supports the price scan range only and do not compute a margin-call trigger from it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yigtwxx/skills/oracle-x-bist)
- [Oracle-X Borsa Istanbul endpoint reference](references/endpoints.md)
- [Reading Takasbank's price scan range](references/viop-margins.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with endpoint paths and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ORACLE_X_URL only for endpoint-backed data; rules guidance works without a server.]

## Skill Version(s):

1.0.0 (source: server release metadata; SKILL.md frontmatter states 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
