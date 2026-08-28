## Description:

Helps agents retrieve and analyze China A-share quotes, fundamentals, capital flows, technical factors, announcements, sectors, convertible bonds, macro data, and comprehensive stock profiles through the public ApocData API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hanjialegit](https://clawhub.ai/user/hanjialegit)

### License/Terms of Use:

Apache 2.0

## Use Case:

External users and developers use this skill to let an agent query ApocData's public A-share market endpoints and produce research-oriented market, company, sector, macro, and event analysis. The skill is intended for data retrieval and research summaries, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote shell or archive-based installation can alter local agent skill files without integrity checks.

Mitigation: Review the release contents before installation and prefer a downloaded archive or package whose checksum or signature is independently checked.

Risk: Financial market outputs may be stale, incomplete, or misread as investment advice.

Mitigation: Show trade_date, delayed_minutes, or freshness metadata; separate source data from inference; cross-check key data; and include research-only investment disclaimers.

Risk: Public no-auth API calls may return empty, truncated, rate-limited, or parameter-error responses.

Mitigation: Check HTTP status, response success flags, limit headers, freshness headers, and documented error codes before drawing conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hanjialegit/skills/apocdata-skill)
- [ApocData platform](https://www.apocdata.com)
- [ApocData OpenAPI specification](https://www.apocdata.com/api/blade-dataplatform/open/data/openapi.json)
- [Interface boundaries and known behavior](references/boundaries.md)
- [Financial output safety rules](references/safety-rules.md)
- [Comprehensive analysis examples](references/examples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and API response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state data freshness, distinguish source data from model inference, and avoid deterministic buy/sell instructions.]

## Skill Version(s):

2.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
