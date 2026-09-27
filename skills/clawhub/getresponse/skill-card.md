## Description:

GetResponse API integration with managed OAuth for managing email marketing campaigns, contacts, newsletters, autoresponders, segments, workflows, ecommerce, SMS, landing pages, webinars, transactional emails, forms, and account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing operators, developers, and automation builders use this skill to manage GetResponse accounts, campaigns, contacts, messaging, ecommerce, and approved automations through a Maton-authenticated connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GetResponse write actions can send messages, alter workflows, create or update records, delete resources, or change business automations.

Mitigation: Require explicit user approval for each write operation after confirming the target account, audience or resource, payload, timing, and intended effect.

Risk: Newsletters, SMS, and transactional emails are delivered to real contacts and can affect recipients, cost, and sender reputation.

Mitigation: Confirm the audience, message content, and send schedule before execution, and default to read/list calls until the user approves a send.

Risk: Hosted functions, triggers, and destinations can create unattended or persistent automation.

Mitigation: Approve each hosted function, trigger, and destination separately, keep network access and destinations narrowly scoped, and review whether the automation should remain enabled.

Risk: API keys and OAuth-backed credentials can expose connected GetResponse account data if mishandled.

Mitigation: Prefer OAuth and OS credential storage, avoid exporting long-lived API keys to child processes, and use raw HTTP with MATON_API_KEY only where the CLI cannot be installed.

## Reference(s):

- [GetResponse Skill Page](https://clawhub.ai/byungkyu/skills/getresponse)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [GetResponse API Documentation](https://apidocs.getresponse.com/v3)
- [GetResponse OpenAPI Spec](https://apireference.getresponse.com/open-api.json)
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

**Output Type(s):** [guidance, shell commands, configuration, code, text]

**Output Format:** [Markdown with inline shell, JSON, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent guidance defaults to read/list calls and requires explicit user approval before write operations, new connections, hosted functions, triggers, or persistent destinations.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
