## Description:

Check an npm package or file in a no-network sandbox before installing it, and browse, sell or buy digital products on the Kenwea marketplace over MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenwea-protocol](https://clawhub.ai/user/kenwea-protocol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to review package install behavior before installation and to browse or transact on the Kenwea digital-products marketplace with operator authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the unpinned npm helper can install code that has changed since review.

Mitigation: Decide whether to trust the Kenwea package and service first; prefer a pinned version or the hosted MCP notary.

Risk: Persisted marketplace credentials could be exposed through insecure configuration or logs.

Mitigation: Review where the bearer token is stored and keep it out of chat logs and committed files.

Risk: Marketplace permissions may let the agent spend funds or publish listings.

Mitigation: Enable wallet, purchase, bid, or publish permissions only when intended; require explicit authorization for each purchase or bid.

## Reference(s):

- [Kenwea ClawHub release](https://clawhub.ai/kenwea-protocol/skills/kenwea)
- [Kenwea website](https://www.kenwea.com)
- [Kenwea MCP documentation](https://www.kenwea.com/docs/mcp)
- [Kenwea verification guide](https://www.kenwea.com/verify)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell snippets and plain-language verdict summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verdicts describe observed install-time behavior, not overall package safety.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
