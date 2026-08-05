## Description:

Create, inspect, update, select, and delete Mermail task triagers and review recent triager runs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure Mermail mailbox triage automation, inspect existing triagers and recent runs, and safely manage default triager behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill manages persistent Mermail triage settings with a Mermail API key.

Mitigation: Install only where the agent should manage triage, and review mailbox scope, sender scope, scan policy, rate budget, allowed integrations, and default status before enabling automation.

Risk: Inbound mail content can contain untrusted instructions that try to trigger external or destructive effects.

Mitigation: Limit triagers to task extraction or drafts, keep inbound interpretation sandboxed, and require fresh human confirmation for sends, deletes, credentials, OTP or magic-link use, account changes, and financial effects.

Risk: Verification, passwordless sign-in, or recovery mailboxes can expose sensitive login material if automated.

Mitigation: Keep verification mailboxes isolated unless the user explicitly changes that isolation setting.

## Reference(s):

- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [Mermail MCP Server](https://console.mermail.app/mcp)
- [Triage tool map](references/tools.md)
- [Triager security boundary](references/security.md)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands]

**Output Format:** [Markdown with tool-call guidance and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MERMAIL_API_KEY and the Mermail MCP server.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
