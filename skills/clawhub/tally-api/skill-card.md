## Description:

Tally API integration with managed OAuth for managing forms, submissions, workspaces, webhooks, organization users, and organization invites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent work with a connected Tally account through Maton OAuth, including reading forms and submissions and carrying out approved changes to workspaces, organization membership, invites, and webhooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write operations can change Tally account data, including forms, workspaces, organization membership, invites, submissions, and webhooks.

Mitigation: Default to read and list calls, then require explicit user approval with target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Organization user removal and invite management affect account membership.

Mitigation: Confirm the organization, target user or email, and intended access change before execution.

Risk: Webhooks can send form submission data, which may contain personal information, to external URLs.

Mitigation: Confirm the form, event types, and destination URL before creating or updating a webhook.

Risk: Maton credentials or provider-issued tokens could be exposed if printed, logged, persisted, or passed on the command line.

Mitigation: Use Maton OAuth and the CLI credential store where possible; never inspect stored credentials, never print tokens, and use the documented stdin-based raw HTTP fallback only when the CLI is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/tally-api)
- [Maton homepage](https://maton.ai)
- [Tally API introduction](https://developers.tally.so/api-reference/introduction)
- [Tally API reference](https://developers.tally.so/llms.txt)
- [Maton docs](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API request paths, command examples, confirmation prompts, and structured JSON payload examples.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
