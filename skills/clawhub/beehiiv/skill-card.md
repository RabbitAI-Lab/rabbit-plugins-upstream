## Description:

beehiiv API integration with managed OAuth for managing newsletter publications, subscriptions, posts, custom fields, segments, tiers, and automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access beehiiv through Maton-managed authentication, list or update newsletter resources, and create user-approved automation around publications, subscriptions, posts, segments, tiers, custom fields, and automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write operations can modify newsletter data, subscriber records, content, segments, tiers, custom fields, automations, or downstream workflows.

Mitigation: Default to read and list calls, verify identifiers and current state first, and require explicit user approval for every POST, PUT, PATCH, or DELETE operation.

Risk: API keys and destination credentials can leak through environment variables, command lines, logs, shell history, or stored trigger templates.

Mitigation: Prefer OAuth through the Maton CLI, never print or persist MATON_API_KEY, send it only to api.maton.ai, and never store Maton or provider tokens in trigger destination headers or body templates.

Risk: Hosted functions run with the deploying Maton account's identity and can access that account's connected apps.

Mitigation: Deploy only user-authored or user-reviewed handlers, summarize accessible connections before deployment or invocation, prefer accounts with only needed connections, and use DENY_ALL network policy unless the user explicitly approves required hosts.

Risk: Trigger destinations create persistent automatic delivery of event data and can disclose personal, business, mailbox, repository, workspace, or payment data.

Mitigation: Use api.maton.ai or Maton-hosted function destinations by default, disclose the destination host and transmitted fields, forward only the minimum required payload fields, and delete destinations when no longer needed.

Risk: Local trigger event watch with --exec runs a local handler on untrusted event data and may continue acting unattended.

Mitigation: Use plain event listing or watch for inspection, run --exec only with a user-provided or user-reviewed handler, scope the automation narrowly, and obtain separate approval before starting it.

## Reference(s):

- [ClawHub beehiiv skill](https://clawhub.ai/byungkyu/skills/beehiiv)
- [Maton homepage](https://maton.ai)
- [beehiiv Developer Documentation](https://developers.beehiiv.com/)
- [beehiiv API Reference](https://developers.beehiiv.com/api-reference)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Code, Configuration instructions]

**Output Format:** [Markdown with inline bash, JSON, and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read/list operations are preferred by default; writes, new connections, hosted functions, trigger destinations, and local event handlers require explicit user approval.]

## Skill Version(s):

1.2.3 (source: server release metadata; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
