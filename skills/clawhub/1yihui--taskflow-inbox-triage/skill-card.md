## Description:

Example TaskFlow authoring pattern for inbox triage. Use when messages need different treatment based on intent, with some routes notifying immediately, some waiting on outside answers, and others rolling into a later summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[1yihui](https://clawhub.ai/user/1yihui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent authors use this skill as an example pattern for triaging inbox items in TaskFlow, routing business items to Slack wait states, personal items to immediate notification, and remaining items to an end-of-day summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Adapted inbox, Slack, or notification integrations could access unintended accounts, channels, or messages if authorization and scope are not explicit.

Mitigation: Before connecting real services, restrict integrations to approved accounts, channels, message scopes, and routing actions.

## Reference(s):

- [Taskflow Inbox Triage on ClawHub](https://clawhub.ai/1yihui/skills/taskflow-inbox-triage)
- [Related TaskFlow inbox triage example](skills/taskflow/examples/inbox-triage.lobster)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration]

**Output Format:** [Markdown with TypeScript and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes example TaskFlow stateJson and waitJson shapes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
