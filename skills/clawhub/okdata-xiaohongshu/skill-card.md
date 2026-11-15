## Description:

Reads public Xiaohongshu data through the okdata API for research on posts, creators, comments, trends, and products.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and marketers can use this skill to research public Xiaohongshu posts, comments, trends, products, and creators. It can support content planning, competitor research, audience feedback review, and creator discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests are sent to the external okdata service and use the configured API key.

Mitigation: Use the service only if you trust okdata. Keep OKDATA_API_KEY in the environment and never paste it into chat.

Risk: Successful API calls incur per-call charges.

Mitigation: Estimate the number and cost of calls before querying, and set max_price for paid calls.

Risk: The security scan had partial coverage because local references were unresolved.

Mitigation: Review the skill and its service references before installation; a benign verdict is not a guarantee of safety.

## Reference(s):

- [okdata Xiaohongshu API documentation](https://okdata.online/zh/apis/xiaohongshu/)
- [ClawHub skill page](https://clawhub.ai/conn-ho/skills/okdata-xiaohongshu)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Structured data]

**Output Format:** [Text or Markdown summaries and structured results based on retrieved public data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected API endpoint and may include post, creator, comment, trend, product, or video metadata.]

## Skill Version(s):

0.1.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
