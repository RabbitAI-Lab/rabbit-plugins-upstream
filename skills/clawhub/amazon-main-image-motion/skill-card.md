## Description:

Turns one approved white-background Amazon main image into a short first-frame product motion clip for the listing main video slot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and listing operators use this skill to plan, price, submit, and review one Beatra image-to-video generation that turns an approved Amazon main image into a single short product motion clip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a shared broad Beatra Device Token for account access across Beatra skills.

Mitigation: Install only when Beatra account access and local credential storage are acceptable; review requested scopes and revoke the connected agent from the Beatra Console when access is no longer needed.

Risk: The workflow can submit billable image-to-video generation requests.

Mitigation: Require the documented production approval card before each paid animate call, use one opaque client_request_id per approved request, and report returned billing.net_charged_credits.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Use the documented update controls, including python3 scripts/mcp_client.py update --auto off, when a fixed local package version is required.

Risk: Selected local product images may be uploaded to Beatra for generation.

Mitigation: Inspect and upload only seller-approved files through the bundled client, and avoid using sensitive imagery where Beatra upload is not acceptable.

## Reference(s):

- [Main image motion workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/amazon-main-image-motion)
- [Beatra skill homepage](https://beatra.ai/skills/amazon-main-image-motion)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON payloads, shell commands, task status summaries, billing fields, and generated video artifact details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Beatra MCP calls, upload artifact references, production approval cards, terminal task results, and review notes for product or text drift.]

## Skill Version(s):

0.1.3 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
