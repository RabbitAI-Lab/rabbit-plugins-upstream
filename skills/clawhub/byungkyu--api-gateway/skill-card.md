## Description:

Routes agent-requested calls to third-party apps through Maton's credential-injecting API gateway for apps the user has already connected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to read or update data in connected SaaS apps, manage connections, and configure event triggers through Maton. It is intended for tasks where the user has already connected the target app and explicitly approves writes, connections, triggers, destinations, and local handlers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad connected-app access can read, write, or delete data through services the user has connected.

Mitigation: Use least-privilege app scopes, default to read and list operations, and require explicit user confirmation before writes, deletions, new connections, triggers, destinations, or handlers.

Risk: Webhook destinations and local --exec handlers can forward event payloads or run local scripts with sensitive data.

Mitigation: Confirm the destination URL or handler script before setup, limit payload contents to the task, and remove triggers or handlers when they are no longer needed.

Risk: Secrets and personal data such as API keys, call records, form submissions, meeting notes, or mailbox content may be exposed during API use.

Mitigation: Do not print or persist credentials, send Maton credentials only to Maton endpoints, and avoid exposing personal data unless the user-approved task requires it.

## Reference(s):

- [API Gateway on ClawHub](https://clawhub.ai/byungkyu/skills/api-gateway)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and short guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run Maton CLI commands and raw HTTPS examples for connected apps; write operations and automation setup require explicit user confirmation.]

## Skill Version(s):

1.2.21 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
