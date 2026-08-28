## Description:

Turn an article title, topic, summary, or reference image into a WeChat Official Account cover, WeChat article cover, article hero image, post cover, headline image, or supporting article visual.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content teams use this skill to create, compose, refine, and review WeChat Official Account cover images from article context, reference assets, or an accepted draft. It helps prepare one confirmed image-generation request, track the Beatra task, and return publish-ready artifact details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Beatra device authorization grants this package account-level authority for its Beatra operations.

Mitigation: Install only when that authorization is acceptable, and reconnect or uninstall the package if the device authorization should no longer be trusted.

Risk: The skill stores a shared Beatra token under ~/.beatra.

Mitigation: Keep the credential files private to the local user and avoid copying tokens into prompts, logs, command arguments, diffs, or other files.

Risk: Selected local files may be uploaded to Beatra when composing from references or editing drafts.

Mitigation: Review chosen files before upload and provide only the images needed for the requested cover.

Risk: The package can silently auto-update its installed package files during normal use.

Mitigation: Disable automatic updates with python3 scripts/mcp_client.py update --auto off when silent replacement is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/wechat-cover-maker)
- [Beatra skill homepage](https://beatra.ai/skills/wechat-cover-maker)
- [Beatra MCP endpoint](https://mcp.beatra.ai/mcp)
- [Intent and routing](references/intent-and-routing.md)
- [Canvas and cover craft](references/canvas-and-cover-craft.md)
- [WeChat cover workflow](references/workflow.md)
- [MCP connection](references/mcp-connection.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Review and recovery](references/review-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Installation registration](references/installation-registration.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and returned artifact links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses one confirmed Beatra image request at a time and reports task, billing, and artifact details when available.]

## Skill Version(s):

0.2.1 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
