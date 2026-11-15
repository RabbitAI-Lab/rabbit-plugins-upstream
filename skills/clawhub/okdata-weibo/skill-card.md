## Description:

Retrieves public Weibo posts, trends, account details, and comments through the okdata API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use the skill to look up Weibo trends, search public posts, inspect accounts, and read post comments for topic monitoring and content research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Query parameters are sent to the external okdata service, and API calls may incur charges.

Mitigation: Tell the user what will be queried and the expected cost before calling; set max_price and avoid sending unnecessary sensitive details.

Risk: The skill requires an OKDATA_API_KEY credential.

Mitigation: Keep the key in the designated environment variable and never ask the user to paste it into the conversation.

## Reference(s):

- [okdata Weibo API documentation](https://okdata.online/zh/apis/weibo/)
- [ClawHub skill release](https://clawhub.ai/conn-ho/skills/okdata-weibo)

## Skill Output:

**Output Type(s):** [API Calls, Analysis, Text]

**Output Format:** [Structured Weibo data with natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public-data lookups are paginated and billed per API call.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
