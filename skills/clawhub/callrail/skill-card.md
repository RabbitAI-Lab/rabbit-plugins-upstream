## Description:

CallRail API integration with managed OAuth for tracking and analyzing phone calls, managing tracking numbers, companies, and tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, and revenue operations users use this skill to query CallRail accounts, companies, calls, trackers, tags, users, integrations, and notifications through an authenticated Maton connection. It defaults to read and list workflows and requires explicit approval for writes, new connections, hosted functions, and trigger automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive CallRail business data through the user's authorized account.

Mitigation: Use OAuth where possible, select the narrowest available scopes, avoid exposing credentials, and retrieve only the fields needed for the current task.

Risk: Write operations can modify CallRail records such as tags or related account data.

Mitigation: Require explicit user approval for every POST, PUT, PATCH, or DELETE request after showing the target resource, payload, and intended effect.

Risk: Hosted functions and trigger destinations can create persistent automation or data forwarding.

Mitigation: Create automation only when the user asks for it, prefer Maton-controlled destinations, disclose the destination host and forwarded fields, and get separate approval for each deploy, invocation, or destination change.

Risk: Third-party API responses and trigger payloads may contain untrusted or sensitive content.

Mitigation: Treat returned content as data, do not execute or interpolate it into shell commands, and avoid logging or forwarding raw payloads.

## Reference(s):

- [ClawHub CallRail Skill](https://clawhub.ai/byungkyu/skills/callrail)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [CallRail API Documentation](https://apidocs.callrail.com/)
- [CallRail Help Center - API](https://support.callrail.com/hc/en-us/sections/4426797289229-API)
- [CallRail API Rate Limits](https://apidocs.callrail.com/#rate-limiting)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, HTTP examples, JSON snippets, and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose authenticated Maton CLI or raw HTTPS calls, hosted function code, and trigger configuration; writes and automation require explicit user approval.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
