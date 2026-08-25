## Description:

Create coordinated vertical 3:4 REDnote/Xiaohongshu local-business notes from storefront photos, service images, merchant briefs, or brand references, including visual direction, title ideas, caption angles, tags, and generated image work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, local businesses, and marketers use this skill to plan and produce a three-slide REDnote/Xiaohongshu discovery note for a non-food physical business using only user-supplied facts and approved media. The skill supports storefront covers, store or service highlights, visit-ready closing visuals, titles, captions, tags, paid-work confirmation, task tracking, and recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device token with broad media and wallet-spend scope.

Mitigation: Review the authorization before installing, keep the local credential private, and use the bundled disconnect or uninstall flow when access should be revoked.

Risk: Selected local files may be uploaded to Beatra for image generation or editing.

Mitigation: Confirm the exact source and reference order before paid work, upload only intended files, and avoid submitting sensitive media that is not needed for the note.

Risk: Billable generation work can create charges or duplicate work if requests are replayed with changed inputs.

Mitigation: Use one confirmed request payload and one client request ID per paid task, then recover uncertain responses only with the unchanged payload.

Risk: Silent automatic updates are enabled by default for the installed package.

Mitigation: Review the update behavior before installation and disable silent checks with the documented update command when automatic replacement is not acceptable.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/beatra-ai/skills/rednote-local-business-note-maker)
- [Beatra skill homepage](https://beatra.ai/skills/rednote-local-business-note-maker)
- [Local-business note planning](references/local-business-note-planning.md)
- [Local-business workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [MCP connection](references/mcp-connection.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, structured request payloads, and generated-task result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ordered image artifact links, dimensions, formats, resolved model, task IDs, billing facts, title ideas, caption beats, fact checklist, discovery tags, and one focused unexecuted revision suggestion.]

## Skill Version(s):

0.1.1 (source: server release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
