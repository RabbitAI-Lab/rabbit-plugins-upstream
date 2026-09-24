## Description:

Resend API integration with managed authentication for sending transactional emails and managing domains, contacts, templates, broadcasts, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with Resend through Maton-managed authentication, including email sending, contact and template management, webhooks, and approved automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform sensitive Resend actions such as sending email, creating broadcasts, deleting resources, creating API keys, configuring webhooks, and running automation.

Mitigation: Confirm the target account, resource, payload, and intended effect with the user before any write, send, deletion, API-key, webhook, trigger, destination, or hosted-function action.

Risk: Persistent webhooks or trigger destinations can continue forwarding future email or event data after setup.

Mitigation: Use only user-named destinations, disclose what data will flow and how often, review existing destinations first, and remove destinations that are no longer needed.

Risk: Long-lived Maton API keys can leak through environment variables, command lines, logs, crash dumps, shell history, or pasted output.

Mitigation: Prefer OAuth, keep API keys out of logs and command arguments, do not persist them in profiles or scripts, and rotate any key that may have been exposed.

Risk: Hosted functions or local event handlers can run unattended against user-connected accounts.

Mitigation: Use user-authored or user-reviewed handlers, require separate approval for deploys and invocations, prefer least-privilege connections, and use DENY_ALL network policy unless the user approves named hosts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/resend-api)
- [Maton Homepage](https://maton.ai)
- [Resend API Documentation](https://resend.com/docs/api-reference/introduction)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)
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

**Output Type(s):** [guidance, shell commands, code, configuration, text]

**Output Format:** [Markdown with inline bash, JSON, and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces user-directed API workflows and approval prompts; responses may contain personal or business data and should be minimized to the task.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
