## Description:

Guides agents in accessing Crown Town Compost customer portal information and account actions through authenticated shell requests without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Crown Town Compost customers and their agents use this skill to review pickups, invoices, and upcoming service, or to prepare authorized account and service requests without installing the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal credentials and session cookies can be exposed through shell environment or cookie files.

Mitigation: Use a temporary cookie jar with restrictive permissions, avoid leaving passwords exported, and clear session material after use.

Risk: Portal requests can change service or account details or send messages.

Mitigation: Require human confirmation before skips, account updates, missed-pickup reports, support messages, or cancellation requests; reread the account to verify any change.

Risk: Billing and account responses can contain sensitive customer information.

Mitigation: Avoid logging raw billing or account data and share only the minimum details needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/crowntowncompost-mcp)
- [Crown Town Compost customer portal](https://portal.crowntowncompost.com)
- [Portal endpoint reference](references/endpoints.md)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Markdown with shell commands and portal data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated responses may include personal account and billing information.]

## Skill Version(s):

1.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
