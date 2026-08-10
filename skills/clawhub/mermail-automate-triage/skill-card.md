## Description:

Create, inspect, update, select, and delete Mermail task triagers and review recent triager runs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to configure and troubleshoot Mermail mailbox automation for task extraction, draft workflows, default triager selection, and triager-linked agent conversations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inbound mail could be mistaken for authority to send messages, delete data, use credentials, perform account actions, or make administrative changes.

Mitigation: Limit triagers to task extraction or reviewed drafts, prohibit high-impact effects from inbound content, and require fresh human approval for sends, deletions, credentials, account changes, and financial effects.

Risk: Sender addresses, display names, domains, or provider webhook checks may be treated as stronger identity proof than they provide.

Mitigation: Use provider-derived sender_authentication results where available, treat unknown or mismatched senders as untrusted, and require an independently configured policy or human decision before broadening scope or changing recipients, payees, addresses, prices, or destinations.

Risk: Unsafe, stale, ambiguous, or excessive message content may trigger unwanted automation or expose unrelated private content.

Mitigation: Require clean scan status before body interpretation, quarantine flagged content, keep unknown scan states metadata-only, sanitize active content, cap processed text and thread messages, and apply mailbox and sender rate budgets.

Risk: Changing the default triager or deleting a triager can alter active automation or remove evidence needed for troubleshooting.

Mitigation: Inspect current triagers and recent runs before editing, require explicit approval for active default changes, use idempotency for supported writes, and use prepare_destructive_action before a single approved deletion.

## Reference(s):

- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [Automate Mermail Triage on ClawHub](https://clawhub.ai/mermail/skills/mermail-automate-triage)
- [Triager security boundary](references/security.md)
- [Triage tool map](references/tools.md)

## Skill Output:

**Output Type(s):** [guidance, configuration, API calls]

**Output Format:** [Markdown guidance with structured tool calls and configuration recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MERMAIL_API_KEY and access to the Mermail MCP server.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
