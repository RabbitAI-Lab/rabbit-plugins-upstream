## Description:

Public AliExpress data through okdata: products. 3 endpoints, $0.002 a call. Use when a task needs AliExpress data. 通过 okdata 取速卖通公开数据：products。3 个接口，每次 $0.002。

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill to search AliExpress products and read buyer reviews through okdata for product research and comparison.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes calls to an external data API, and paid calls incur a per-call charge.

Mitigation: Review the requested endpoint and maximum cost before the first paid call; use the documented price and max_price limit.

Risk: Scanner coverage was partial because several local references were unresolved.

Mitigation: Review the skill and its linked references before installation, especially any references the scan could not resolve.

## Reference(s):

- [AliExpress API documentation](https://okdata.online/apis/aliexpress/?src=skill-okdata-aliexpress)
- [okdata agent setup guide](https://okdata.online/agents.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text containing AliExpress product or buyer review data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paged results; each paid call returns one page, usually about 20 products or reviews.]

## Skill Version(s):

0.2.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
