## Description:

Beatra AI Image Studio guides agents through text-to-image generation, reference-guided composition, and focused image editing for product photos, ad creative, brand visuals, posters, social graphics, illustrations, concept art, and photo background changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creative teams, marketers, and developers use this skill to turn a written brief, ordered reference images, or an existing base image into reviewed image-generation or image-editing work. It helps choose the correct Beatra route, prepare sources, obtain paid approval, run the task, report billing facts, and inspect results for visual fit and drift.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary says this package grants and stores broad account authority, including media and spending authority.

Mitigation: Install only when that authority is acceptable; consider a dedicated Beatra account or low-balance setup, and revoke the device token from Beatra when the skill is no longer needed.

Risk: The server security guidance flags default silent package updates.

Mitigation: Disable silent updates for the installation with scripts/mcp_client.py update --auto off when automatic local package replacement is not desired.

Risk: Paid image tasks can create duplicate or unexpected charges if retried with changed inputs after uncertain transport results.

Mitigation: Use one stable client_request_id for each frozen paid payload, retry only the identical payload after uncertainty, and require new approval for changed prompts, sources, controls, count, model, or canvas.

Risk: The shared Beatra device token is sensitive local credential material.

Mitigation: Keep the token only in the private credential file, avoid exposing it in chat, logs, command arguments, environment variables, diffs, or backups, and use the bundled uninstall flow before removing shared connection state.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/beatra-ai/skills/beatra-ai-image-studio)
- [Beatra skill homepage](https://beatra.ai/skills/beatra-ai-image-studio)
- [Beatra MCP endpoint](https://mcp.beatra.ai/mcp)
- [Skill instructions](artifact/SKILL.md)
- [Intent and routing](artifact/references/intent-and-routing.md)
- [Visual direction and source preparation](artifact/references/visual-direction.md)
- [Image payloads and admission](artifact/references/image-recipes.md)
- [Review and iteration](artifact/references/review-and-iteration.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Beatra task IDs, image artifact URLs, dimensions, format, usage, and final charged credits when tasks run.]

## Skill Version(s):

1.1.3 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
