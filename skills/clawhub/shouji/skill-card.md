## Description:

根据手机号查归属省市、运营商与卡类型。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jisuapi](https://clawhub.ai/user/jisuapi)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up a Chinese mobile phone number's province, city, carrier, and card type through JisuAPI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queried phone numbers are sent to JisuAPI for attribution lookup.

Mitigation: Query only numbers the user is permitted to process, mask numbers in user-facing summaries when practical, and avoid unnecessary retention.

Risk: The JISU_API_KEY may create quota, billing, or access exposure if reused broadly.

Mitigation: Use a dedicated key with limited quota or billing scope and avoid logging full command lines, request URLs, or raw key values.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jisuapi/skills/shouji)
- [JisuAPI Website](https://www.jisuapi.com/)
- [JisuAPI Mobile Phone Number Location API](https://www.jisuapi.com/api/shouji/)
- [JisuAPI Query Endpoint](https://api.jisuapi.com/shouji/query)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON from a Python CLI, with agent-facing guidance for summarizing the lookup result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and JISU_API_KEY; sends the queried phone number to JisuAPI.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
