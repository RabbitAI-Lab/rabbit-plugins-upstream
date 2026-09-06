## Description:

Southwest Florida real-estate and local-economy data for Lee and Collier County housing, ZIP-level reports, flood and insurance context, permits, CRE corridors, and local economic indicators, with each figure sourced and dated.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ethanrickyjrjr-wq](https://clawhub.ai/user/ethanrickyjrjr-wq)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and real-estate professionals use this skill to retrieve sourced, dated Southwest Florida housing and local-economy reports for Lee County, Collier County, and nearby city or ZIP-level market questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes public web requests to a third-party SWFL Data Gulf data service.

Mitigation: Use only the documented public endpoints unless the user explicitly approves optional MCP use, and do not provide credentials to the service.

Risk: A user may mistake dated market figures for current-day values.

Mitigation: Preserve each returned source name, as-of date, freshness date, and metric-specific caveat when presenting figures.

Risk: The skill includes a human upgrade path for paid plans.

Mitigation: Do not authorize purchases or sign up for paid services on the user's behalf.

## Reference(s):

- [SWFL Data Gulf homepage](https://www.swfldatagulf.com)
- [SWFL Data Gulf ClawHub skill page](https://clawhub.ai/ethanrickyjrjr-wq/skills/swfl-data-gulf)
- [Agent site map](https://www.swfldatagulf.com/llms.txt)
- [Master report speak endpoint](https://www.swfldatagulf.com/api/b/master?view=speak&tier=2&v=5)
- [Housing report speak endpoint](https://www.swfldatagulf.com/api/b/housing-swfl?view=speak&tier=2&v=5)
- [CRE report](https://www.swfldatagulf.com/r/cre-swfl)
- [MCP endpoint](https://www.swfldatagulf.com/api/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline curl commands and optional MCP configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should preserve source names, as-of dates, freshness dates, and attached caveats from the retrieved SWFL Data Gulf reports.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
