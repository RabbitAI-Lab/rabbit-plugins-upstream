## Description:

AndonQ helps agents query Tencent Cloud support tickets, organization tickets, story requests, and SmartQA customer-service answers from Tencent Cloud.

This skill is ready for commercial/non-commercial use.

## Publisher:

[llm-pm](https://clawhub.ai/user/llm-pm)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Tencent Cloud support tickets, organization-level tickets and story requests, and to ask Tencent Cloud product questions through SmartQA.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read Tencent Cloud support-ticket data available to the configured AK/SK.

Mitigation: Use a least-privilege subaccount key, prefer temporary session-level environment variables, avoid storing long-lived secrets in shell profiles, and rotate credentials regularly.

Risk: SmartQA sends user questions and multi-turn context to Tencent Cloud services for processing.

Mitigation: Tell the user before the first SmartQA call and avoid sending secrets, customer data, internal hostnames, or other sensitive content.

Risk: Organization-wide ticket modes can expose broader ticket titles, UINs, descriptions, and related support data.

Mitigation: Use organization-wide queries only after the user explicitly asks for that scope and state that the returned data range has expanded.

Risk: Verbose and dry-run modes can reveal request payloads or signed-request metadata in shared logs.

Mitigation: Avoid verbose or dry-run output in shared terminals, recordings, or retained logs.

## Reference(s):

- [AndonQ ClawHub skill page](https://clawhub.ai/llm-pm/skills/tencent-andon)
- [Tencent Cloud API key console](https://console.cloud.tencent.com/cam/capi)
- [Tencent Cloud online service](https://cloud.tencent.com/online-service?from=claw&redirectType=0)
- [GetMCTicketList](references/GetMCTicketList.md)
- [GetMCTicketById](references/GetMCTicketById.md)
- [SmartQA](references/SmartQA.md)
- [DescribeOrganizationTickets](references/DescribeOrganizationTickets.md)
- [DescribeTicket](references/DescribeTicket.md)
- [DescribeTicketOperation](references/DescribeTicketOperation.md)
- [DescribeOrganizationStories](references/DescribeOrganizationStories.md)
- [DescribeOrganizationStory](references/DescribeOrganizationStory.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Tencent Cloud support-ticket data, SmartQA answers, session identifiers, and request IDs.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
