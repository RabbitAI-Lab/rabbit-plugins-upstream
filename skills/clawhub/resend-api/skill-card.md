## Description:

Resend API integration with managed authentication for sending transactional email and managing domains, contacts, templates, broadcasts, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to perform approved Resend API work through Maton-managed authentication, including sending transactional email and managing domains, contacts, templates, broadcasts, webhooks, and API keys.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton CLI or SDK package distribution must be trusted before installation.

Mitigation: Install only from trusted Maton package channels and review release notes before upgrading pinned versions.

Risk: Long-lived API keys can leak through environment variables, logs, shell history, or copied output.

Mitigation: Prefer OAuth, never print or persist keys, pass secrets only through approved secret stores, and rotate any exposed key.

Risk: Email sends, deletes, webhook changes, API-key operations, functions, and triggers can create external side effects or account-security changes.

Mitigation: Require explicit user confirmation of the target, payload, destination, and intended effect before every write or automation action.

Risk: Persistent webhooks or trigger destinations can forward future email, recipient, or event data automatically.

Mitigation: Verify the destination URL is user-provided, identify who controls the host, minimize forwarded fields, and avoid request-bin, tunnel, pastebin, or inspection endpoints.

Risk: Third-party API responses and event payloads may contain sensitive data or adversarial instructions.

Mitigation: Treat returned content as untrusted data, avoid logging full payloads, and never let fetched content choose follow-up endpoints, recipients, commands, or destinations.

## Reference(s):

- [ClawHub Resend Skill](https://clawhub.ai/byungkyu/skills/resend-api)
- [Maton Homepage](https://maton.ai)
- [Resend API Documentation](https://resend.com/docs/api-reference/introduction)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent guidance for authenticated Resend API calls and user-approved automation setup; API responses may contain personal or business data.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
