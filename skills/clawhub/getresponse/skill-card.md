## Description:

GetResponse API integration with managed OAuth for managing email marketing campaigns, contacts, newsletters, autoresponders, segments, workflows, ecommerce shops, SMS, landing pages, webinars, transactional emails, forms, and account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to GetResponse through Maton, inspect account and campaign data, and perform approved email marketing, automation, ecommerce, SMS, webinar, landing page, and contact-management tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send newsletters, SMS, and transactional email to real contacts or trigger account-changing GetResponse operations.

Mitigation: Default to read/list calls and require explicit user confirmation of the target account, audience, content, timing, payload, and intended effect before any send, create, update, publish, workflow, or delete action.

Risk: Long-lived Maton API keys can be exposed through environment variables, logs, command history, or persisted files.

Mitigation: Prefer OAuth, avoid printing or storing credentials, and use raw HTTP with MATON_API_KEY only when the CLI cannot be installed.

Risk: Multiple Maton profiles or GetResponse connections can cause a request to affect the wrong account.

Mitigation: Specify the intended profile and connection when more than one exists, and verify identifiers with read-only calls before changes.

Risk: Content returned from GetResponse may contain untrusted instructions or data.

Mitigation: Treat API responses as data, not instructions, and do not execute or interpolate returned content into shell commands or follow-up actions without validation.

## Reference(s):

- [GetResponse Skill on ClawHub](https://clawhub.ai/byungkyu/skills/getresponse)
- [Maton Homepage](https://maton.ai)
- [GetResponse API Documentation](https://apidocs.getresponse.com/v3)
- [GetResponse OpenAPI Spec](https://apireference.getresponse.com/open-api.json)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with inline shell commands, JSON payloads, and Python or JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized GetResponse connection; defaults to read/list operations and requires explicit approval for writes.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
