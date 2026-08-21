## Description:

ApocData helps agents query China's A-share market data, including quotes, financials, fund flows, factors, announcements, macro indicators, sectors, convertible bonds, and comprehensive stock profiles through the ApocData public API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hanjialegit](https://clawhub.ai/user/hanjialegit)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let agents retrieve and summarize A-share market data for research workflows, market monitoring, and API-backed financial analysis. Outputs must remain research assistance and avoid investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled install path can fetch remote shell scripts or archives and persistently alter local agent skills without integrity checks.

Mitigation: Install only trusted releases, avoid curl-to-bash, inspect downloaded scripts or archives first, and verify file integrity before placing files in an agent skills directory.

Risk: Financial analysis may be misleading if delayed, sparse, failed, or contradictory market data is treated as current or definitive.

Mitigation: Check HTTP status and success fields, report data timestamps and freshness, stop deterministic conclusions on abnormal responses, cross-validate important figures, and label all analysis as research assistance rather than investment advice.

## Reference(s):

- [ApocData Skill on ClawHub](https://clawhub.ai/hanjialegit/skills/apoc-data-skill)
- [ApocData Platform](https://www.apocdata.com)
- [ApocData OpenAPI 3 Specification](https://www.apocdata.com/api/blade-dataplatform/open/data/openapi.json)
- [Interface Boundaries and Known Behavior](references/boundaries.md)
- [Financial Output Safety Rules](references/safety-rules.md)
- [Comprehensive Analysis Examples](references/examples.md)
- [Quotes and Valuation Endpoints](references/group-a-quote.md)
- [Financials and Fundamentals Endpoints](references/group-b-financial.md)
- [Capital Flow Endpoints](references/group-c-capital.md)
- [Limit-Up and Sentiment Endpoints](references/group-d-limitup.md)
- [Events and Information Endpoints](references/group-e-events.md)
- [Sectors and Concepts Endpoints](references/group-f-sector.md)
- [Convertible Bonds Endpoints](references/group-g-convertible.md)
- [Quant and Technical Endpoints](references/group-h-quant.md)
- [Macro Endpoints](references/group-i-macro.md)
- [Tool Endpoints](references/group-j-tools.md)
- [Agent Enhanced Endpoints](references/group-k-agent.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and API response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cited data timestamps, freshness details, source field labels, and research-only financial disclaimers.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
