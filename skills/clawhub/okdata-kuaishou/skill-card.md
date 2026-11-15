## Description:

Retrieves public Kuaishou video, account, comment, and trending data through the okdata API for agent-assisted research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

AI agents use this skill to find public Kuaishou videos, inspect accounts and comments, and track trending topics for content research and competitor monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: This skill sends requests to an external paid API using an API key; the security assessment is benign with medium confidence and notes that some references were unresolved.

Mitigation: Review the service before connecting, keep the key in the OKDATA_API_KEY environment variable, estimate call costs, and set max_price for each call.

Risk: Returned public comments and account data can include IP regions.

Mitigation: Retrieve only the fields needed and avoid exposing personal details in shared summaries.

## Reference(s):

- [okdata Kuaishou API documentation](https://okdata.online/zh/apis/kuaishou/)
- [ClawHub release page](https://clawhub.ai/conn-ho/skills/okdata-kuaishou)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown]

**Output Format:** [Structured API results with concise text or Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public Kuaishou data; API calls are pay-per-call.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
