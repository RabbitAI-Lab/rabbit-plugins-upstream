## Description:

Helps agents use a connected Zoho Bigin account to find and manage CRM records and, when requested, set up related automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and operations teams use this skill to find, create, update, or delete Zoho Bigin contacts, companies, pipelines, and products through an authorized connection. They can also request hosted functions and triggers for approved CRM workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected CRM may expose modules beyond the headline contacts, companies, pipelines, and products.

Mitigation: Review the authorized scope before installation; require the agent to name the exact module, connection, record IDs, and payload before any write.

Risk: Hosted functions, triggers, and destinations can produce ongoing actions or forward event data.

Mitigation: Approve each function, trigger, and destination separately, including its target, schedule or event, and any data it sends.

Risk: Handling a Maton API key outside the CLI can expose account credentials.

Mitigation: Prefer the authenticated CLI; when direct HTTP is necessary, keep the key in a secret-managed environment and never print or persist it.

## Reference(s):

- [ClawHub release](https://clawhub.ai/byungkyu/skills/zoho-bigin)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Zoho Bigin API overview](https://www.bigin.com/developer/docs/apis/v2/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may contain customer and business data; share only fields needed for the task.]

## Skill Version(s):

1.2.5 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
