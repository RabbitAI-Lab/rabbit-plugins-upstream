## Description:

Helps an agent answer Turkish-market finance questions about BIST equities, TEFAS funds, KAP disclosures, VIOP futures, market positioning, delayed prices, and inflation-adjusted returns using documented rules and an optional Oracle-X instance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yigtwxx](https://clawhub.ai/user/yigtwxx)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide agents through Turkish-market research, including how to frame lira returns, choose Oracle-X BIST endpoints, handle unavailable data, and avoid unsupported VIOP margin-call calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticker lookups and scan requests may be visible to the operator of the configured Oracle-X instance.

Mitigation: Use only a trusted Oracle-X instance and avoid sending sensitive trading intent or personal account information.

Risk: BIST quote data exposed by the skill is delayed and may be unavailable when no Oracle-X instance or upstream data source responds.

Mitigation: State delay or unavailability clearly, and avoid presenting delayed or missing values as live market prices.

Risk: VIOP price scan ranges can be mistaken for margin-call levels.

Mitigation: Describe scan ranges as the move initial margin is sized for, and do not compute a margin-call price from public data.

## Reference(s):

- [Oracle-X BIST skill page](https://clawhub.ai/yigtwxx/skills/oracle-x-bist)
- [Oracle-X source repository](https://github.com/Yigtwxx/OracleX)
- [Oracle-X Borsa Istanbul endpoint reference](references/endpoints.md)
- [Reading Takasbank's price scan range](references/viop-margins.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown with inline code, shell commands, endpoint guidance, and concise market-analysis text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include curl commands and JSON endpoint interpretation when ORACLE_X_URL is configured; otherwise produces rules-based guidance without querying a server.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter declares 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
