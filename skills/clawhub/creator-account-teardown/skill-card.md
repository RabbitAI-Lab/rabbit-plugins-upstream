## Description:

Creator Account Teardown helps users analyze a creator account from supplied evidence or supported platform lookups, then turn the account's positioning, audience, content matrix, hook patterns, and cadence into their own account plan and first produced post.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and social media operators use this skill to benchmark a creator account or diagnose their own account, then produce a positioning line, bio, content pillars, hook formula, opening plan, and first post.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra bearer token and wallet-spending authority.

Mitigation: Install only if that shared trust boundary is acceptable, keep the local credential private, and run paid lookups or media generation only after explicit user approval.

Risk: The bundled client can silently update the skill package.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when silent replacement is not acceptable, and review updates before use.

Risk: Account metrics, comments, generated covers, and narration can become stale, inaccurate, or incur charges.

Mitigation: Label account data by source and read time, avoid unsourced metrics, inspect generated media before delivery, and confirm every paid lookup or production call separately.

## Reference(s):

- [Reading the account from a handle](references/account-lookup.md)
- [Reading the account](references/account-read.md)
- [Building your own account](references/build-template.md)
- [Account teardown workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured analysis, tables, plans, scripts, captions, shell commands, and generated media task details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Beatra task identifiers, artifact links, billing details, generated cover details, and narration metadata when paid production is approved.]

## Skill Version(s):

0.1.4 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
