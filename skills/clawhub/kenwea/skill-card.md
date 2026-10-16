## Description:

Check an npm package or file in a no-network sandbox before installing it, and browse, sell or buy digital products on the Kenwea marketplace over MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenwea-protocol](https://clawhub.ai/user/kenwea-protocol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to review package or file install-time behavior before installation and to browse or transact on the Kenwea digital marketplace with operator approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Package and file checks, as well as marketplace actions, send information to external Kenwea services.

Mitigation: Configure and use Kenwea services only when the user accepts sending check requests or marketplace actions to them.

Risk: The suggested npx command runs an unpinned npm CLI.

Mitigation: For higher-assurance use, pin or pre-review the @kenwea/mcp version before running it.

Risk: Purchases, bids, wallet actions, and publication can have financial or public consequences.

Mitigation: Require explicit user approval for each such action before proceeding.

Risk: A clean sandbox result does not establish that a package or listing is safe for every use.

Mitigation: Describe the observed result and limitations without treating the verdict as a safety endorsement.

## Reference(s):

- [Kenwea skill release](https://clawhub.ai/kenwea-protocol/skills/kenwea)
- [Kenwea MCP documentation](https://www.kenwea.com/docs/mcp)
- [Kenwea record verification](https://www.kenwea.com/verify)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell commands and check-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Explains check outcomes and requests user approval before financial or public marketplace actions.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
