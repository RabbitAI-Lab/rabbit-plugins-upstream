## Description:

Queries county-level bidding opportunities, award notices, winner contact details, notice details, and business registration information through the dcbmt.com county business data service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[498617](https://clawhub.ai/user/498617)

### License/Terms of Use:

MIT-0

## Use Case:

External users can search county-level procurement and bidding notices, inspect notice details, identify winning companies, and query company registration/contact information for local business research and sales prospecting.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The quota-exhaustion path directs users to an off-platform QQ contact for registration and API-key onboarding.

Mitigation: Review that flow before installation, use the manifest homepage as the primary trust anchor, and avoid sharing credentials through unofficial channels.

Risk: Bulk winner-phone retrieval can expose large volumes of business contact data.

Mitigation: Run bulk retrieval only when it is appropriate for the user’s purpose and applicable data-handling obligations.

Risk: The publisher trust tier in server evidence is low.

Mitigation: Confirm the publisher profile, service homepage, and security scan summary before enabling the skill in production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/498617/skills/county-business-query)
- [Publisher profile](https://clawhub.ai/user/498617)
- [Official county service homepage](https://dcbmt.com/county/)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses optional API-key configuration through command argument or environment variable; query results may include business names, phone numbers, notice metadata, and service error guidance.]

## Skill Version(s):

8.12.0 (source: SKILL.md frontmatter, clawhub.yaml, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
