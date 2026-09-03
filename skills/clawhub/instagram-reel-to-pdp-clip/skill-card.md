## Description:

Instagram product video is one product detail video per product still after reading a competitor Reel. Use this Instagram PDP clip studio for a product page video and a Reel-to-PDP clip from the same still list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, commerce teams, and their agents use this skill to turn supplied product stills into silent product-detail clips. It guides Reel lookup, free shot-list planning, paid generation approval, upload, task polling, recovery, and delivery through Beatra.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra device authorization can spend credits and access broader Beatra media tools than this workflow needs.

Mitigation: Install only when that account access is acceptable, provide only product stills and public Instagram references intended for Beatra, and revoke or uninstall the connection when it is no longer needed.

Risk: Automatic package updates are enabled by default and can replace package code without a separate prompt.

Mitigation: Disable silent updates with `python3 scripts/mcp_client.py update --auto off` when review-before-update is required; the bundled updater is documented to verify fixed Beatra paths and package checksums.

Risk: Paid Reel lookup and video generation consume Beatra credits, and incorrect retries can create duplicate billable work.

Mitigation: Use live pricing, show the required approval card before paid work, and reuse a `client_request_id` only for byte-identical recovery of an uncertain request.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/instagram-reel-to-pdp-clip)
- [Beatra skill homepage](https://beatra.ai/skills/instagram-reel-to-pdp-clip)
- [Product-detail clip workflow](references/workflow.md)
- [Reel lookup](references/reel-lookup.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads; successful generation returns one video file per supplied still.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live pricing and explicit user approval before paid lookup or video generation.]

## Skill Version(s):

0.1.1 (source: manifest.json and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
