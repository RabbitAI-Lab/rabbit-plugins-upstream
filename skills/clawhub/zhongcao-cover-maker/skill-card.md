## Description:

Turn a photo or a topic idea into a scroll-stopping vertical 3:4 Xiaohongshu cover with clean backgrounds, bold focal composition, and text-safe areas for beauty, food, fashion, and lifestyle notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to plan and generate REDnote/Xiaohongshu cover or post images from a source photo, a topic idea, or an accepted draft. The skill can also run optional paid Xiaohongshu lookups before cover planning when platform-specific evidence is needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary says the skill requests a broad shared Beatra token with spending and multi-media permissions.

Mitigation: Install only when that shared authorization is acceptable, keep the token private, and use the documented uninstall or Beatra Console revocation path when access should end.

Risk: The server security summary notes silent self-updates, and the artifact documents automatic update checks before ordinary Beatra commands.

Mitigation: Use the documented auto-update controls to disable silent checks when change control is required, and rely on the documented checksum and rollback checks for accepted updates.

Risk: The skill can upload selected local files and run paid image generation or Xiaohongshu lookup tasks.

Mitigation: Confirm each paid operation, quote lookup pricing when applicable, upload only the user-selected files needed for the cover, and preserve one client_request_id per billable request to avoid duplicate charges.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/beatra-ai/skills/zhongcao-cover-maker)
- [Beatra skill page](https://beatra.ai/skills/zhongcao-cover-maker)
- [Cover routing](references/cover-routing.md)
- [Cover craft](references/cover-craft.md)
- [Workflow](references/workflow.md)
- [Reading Xiaohongshu](references/note-lookup.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Review and recovery](references/review-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Files, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples; final delivery includes generated image artifact links, observed dimensions, task ID, and billing credits.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default output count is one 3:4 cover image; optional Xiaohongshu lookups and image generation are paid operations that require confirmation.]

## Skill Version(s):

0.1.5 (source: manifest.json and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
