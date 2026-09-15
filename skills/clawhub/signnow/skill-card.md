## Description:

SignNow API integration with managed OAuth for sending, signing, and managing e-signature documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with SignNow through Maton's managed OAuth connection, including listing documents, uploading PDFs, sending signature invites, creating templates, and configuring approved automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act on SignNow business documents through a Maton-authenticated connection.

Mitigation: Use OAuth with the narrowest available SignNow scopes, confirm connection creation, and verify the target account or connection before writes.

Risk: Write operations and automations can send invites, modify documents, or create persistent downstream workflows.

Mitigation: Default to read/list calls, require explicit approval for every POST, PUT, PATCH, DELETE, function deployment, trigger, or destination, and describe the target resource and intended effect before execution.

Risk: API keys, event payloads, and document responses may expose sensitive data if printed, logged, or forwarded broadly.

Mitigation: Prefer CLI-managed OAuth, never print or persist credentials, forward only minimum required fields, avoid full-payload forwarding, and use platform destinations unless the user approves a specific third-party host.

## Reference(s):

- [SignNow API Reference](https://docs.signnow.com/docs/signnow/reference)
- [SignNow Developer Portal](https://www.signnow.com/developers)
- [SignNow Postman Collection](https://github.com/signnow/postman-collection)
- [SignNow SDKs](https://github.com/signnow)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with bash, JSON, and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include API paths, CLI commands, request payloads, hosted function snippets, and trigger configuration examples.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
