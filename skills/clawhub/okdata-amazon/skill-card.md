## Description:

Access public Amazon product, review, and Best Sellers data across 22 stores through okdata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to search Amazon products, retrieve product details and reviews, and browse category Best Sellers lists through okdata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial, could not resolve several local path-like references, and flagged the external service address; its benign verdict does not establish that the artifact is risk-free.

Mitigation: Use the service only if you trust it and want to use it; keep the API key in OKDATA_API_KEY or the client's configuration, and never expose it in output or URLs.

Risk: Paid data calls cost $0.006 each, and fetching another page requires another paid call.

Mitigation: State the planned call count and maximum cost before the first paid call, use max_price to cap a call, and fetch further pages only when needed.

## Reference(s):

- [okdata Amazon API reference](https://okdata.online/apis/amazon/?src=skill-okdata-amazon)
- [okdata agent setup guide](https://okdata.online/agents.md)
- [ClawHub skill page](https://clawhub.ai/conn-ho/skills/okdata-amazon)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text responses containing Amazon product, review, or Best Sellers data with source attribution.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One page per call; source and fetch time are included. Paid endpoint calls cost $0.006 each.]

## Skill Version(s):

0.2.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
