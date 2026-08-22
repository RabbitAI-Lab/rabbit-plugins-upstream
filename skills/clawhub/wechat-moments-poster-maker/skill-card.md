## Description:

Create WeChat Moments posters and campaign graphics from a product photo, event brief, promotion, recruitment message, seasonal greeting, brand assets, or accepted draft. Produce square or vertical social visuals with a clear focal point and headline-safe space for WeChat Moments, customer-community updates, launches, invitations, and marketing campaigns; refine the selected image while preserving the brand direction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, operators, and community managers use this skill to create or refine one WeChat Moments share graphic from a campaign brief, product photo, brand assets, or accepted draft.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra account authorization rather than a narrow media-only grant.

Mitigation: Install only if that shared authorization fits the deployment, and revoke the Beatra device authorization when the package is no longer used.

Risk: Generation, transform, and edit operations may spend Beatra credits.

Mitigation: Require confirmation before each paid request, keep one stable request identity for recovery, and report returned billing.net_charged_credits.

Risk: The package stores a local Beatra device token for subsequent requests.

Mitigation: Keep the token only in the user credential file, avoid exposing it in chat or logs, and use the documented disconnect flow to remove access.

Risk: Automatic package updates are enabled by default.

Mitigation: Disable auto-updates for environments that require change control, or run the documented update check before accepting a newer package.

## Reference(s):

- [WeChat Moments Poster Maker on ClawHub](https://clawhub.ai/beatra-ai/skills/wechat-moments-poster-maker)
- [Beatra Skill Homepage](https://beatra.ai/skills/wechat-moments-poster-maker)
- [Workflow](references/workflow.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Installation Registration](references/installation-registration.md)
- [MCP Connection](references/mcp-connection.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with command snippets, task details, billing details, and generated artifact links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one social poster workflow result per approved paid request, including task ID, resolved model, observed dimensions, net charged credits, and artifact links when available.]

## Skill Version(s):

0.1.1 (source: release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
