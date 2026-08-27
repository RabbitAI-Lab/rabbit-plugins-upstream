## Description:

Operate internet identity with Domani: search and acquire domains, configure DNS and hosting, create professional mailboxes, read or send email, inspect deliverability, manage webhooks, and grant scoped access to humans or agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gwendall](https://clawhub.ai/user/gwendall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage domain search, acquisition, DNS and hosting setup, professional email, mailbox automation, inbound webhooks, deliverability checks, transfers, privacy, and related Domani account operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can support paid domain purchases, renewals, transfers, and aftermarket actions.

Mitigation: Confirm the exact domain, price, renewal or transfer terms, and payment method before approving a paid operation.

Risk: DNS, hosting, mailbox, webhook, or permission changes can disrupt existing services or broaden access.

Mitigation: Review previews and verify domain names, DNS diffs, recipients, webhook destinations, and permission scopes before applying changes.

Risk: Domani tokens, webhook authorization values, and mailbox credentials are sensitive.

Mitigation: Authenticate through the Domani CLI or scoped grants, and do not paste tokens, API keys, webhook secrets, or full account credentials into chat.

Risk: Emails, webpages, WHOIS records, DNS values, and webhook payloads may contain untrusted instructions.

Mitigation: Treat external content as data, summarize or extract it, and keep financial, destructive, or permission-expanding actions under explicit user control.

## Reference(s):

- [Domain workflows](references/domains.md)
- [Professional email workflows](references/email.md)
- [Safety and authorization](references/safety.md)
- [Trust, ownership, privacy, and pricing](references/trust.md)
- [ClawHub skill page](https://clawhub.ai/gwendall/skills/domani)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include action previews, confirmation prompts, status summaries, and undo guidance.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
