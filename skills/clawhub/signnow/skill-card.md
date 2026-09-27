## Description:

SignNow API integration with managed OAuth for uploading documents, sending signature invites, creating templates, and managing e-signature workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to SignNow through Maton, perform approved document signing workflows, and optionally create user-approved automation around those workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or change SignNow resources through an authenticated Maton connection.

Mitigation: Default to read and list operations, and require explicit user approval before creating connections or running POST, PUT, PATCH, or DELETE actions.

Risk: Long-lived API keys or environment variables can broaden credential exposure.

Mitigation: Prefer Maton OAuth and the operating system credential store; use raw API keys only where the CLI cannot be installed.

Risk: Hosted functions and triggers can run approved SignNow actions persistently or in response to third-party events.

Mitigation: Use user-authored or user-reviewed handlers, deploy with least privilege and deny outbound network access unless approved, and remove unused connections, functions, and triggers when finished.

## Reference(s):

- [ClawHub SignNow skill page](https://clawhub.ai/byungkyu/skills/signnow)
- [Maton homepage](https://maton.ai)
- [SignNow API Reference](https://docs.signnow.com/docs/signnow/reference)
- [SignNow Developer Portal](https://www.signnow.com/developers)
- [SignNow Postman Collection](https://github.com/signnow/postman-collection)
- [SignNow SDKs](https://github.com/signnow)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly trigger reference](references/calendly/triggers.md)
- [GitHub trigger reference](references/github/triggers.md)
- [Google Mail trigger reference](references/google-mail/triggers.md)
- [HubSpot trigger reference](references/hubspot/triggers.md)
- [Linear trigger reference](references/linear/triggers.md)
- [Notion trigger reference](references/notion/triggers.md)
- [Slack trigger reference](references/slack/triggers.md)
- [Stripe trigger reference](references/stripe/triggers.md)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, markdown]

**Output Format:** [Markdown guidance with inline shell commands, code examples, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide authenticated SignNow API calls through Maton and require explicit user approval for writes, new connections, hosted functions, and triggers.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
