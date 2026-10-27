## Description:

A read-only Weibo research assistant for reviewing trending topics, posts, comments, engagement, and creator profiles or post lists through SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Users and analysts use this skill to review Weibo trends, discover posts, inspect comments and engagement, and retrieve creator profiles or post lists through SocialDataX. It requires a SocialDataX API key and does not modify Weibo accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and links are sent to SocialDataX for data retrieval.

Mitigation: Use only queries and links you are comfortable sharing with the service.

Risk: The SocialDataX API key could expose account access if disclosed.

Mitigation: Keep SOCIALDATAX_API_KEY private and avoid exposing it in logs or outputs.

Risk: Large data collections may consume service credits.

Mitigation: Check credit costs and set appropriate collection limits before large queries.

Risk: The documented CLI examples install the latest package version, which can change over time.

Mitigation: Prefer a reviewed, fixed package version and limit its access to unrelated files and secrets.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, JSON, Research guidance]

**Output Format:** [Structured Weibo research results and concise summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; results depend on the query and SocialDataX API response.]

## Skill Version(s):

0.1.20 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
