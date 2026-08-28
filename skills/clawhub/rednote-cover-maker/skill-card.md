## Description:

Turn a photo, a topic idea, or an accepted draft into a scroll-stopping REDnote (Xiaohongshu) cover and post image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and agents use this skill to transform source photos, topic ideas, or accepted drafts into vertical 3:4 REDnote/Xiaohongshu covers and post images. It helps prepare a single confirmed cover brief, submit approved Beatra image-generation work, track the task, and review the result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra device token stored under ~/.beatra.

Mitigation: Review the Beatra authorization before installation, keep the token out of command arguments and logs, and revoke the device from the Beatra Console when the connection is no longer needed.

Risk: Approved generation calls can spend Beatra credits.

Mitigation: Confirm the prompt, references, canvas, model, count, controls, and client_request_id before submitting paid work, then avoid duplicate submissions during recovery.

Risk: The skill silently updates its installed package files by default.

Mitigation: Use python3 scripts/mcp_client.py update --auto off to disable automatic updates when a reviewed static installation is required.

Risk: Selected local images are uploaded to Beatra for transform or edit workflows.

Mitigation: Upload only user-approved images and avoid exposing private prompts, credentials, or sensitive input details in recovery messages.

## Reference(s):

- [Cover routing](references/cover-routing.md)
- [Cover craft](references/cover-craft.md)
- [Workflow](references/workflow.md)
- [Review and recovery](references/review-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/rednote-cover-maker)
- [Beatra skill homepage](https://beatra.ai/skills/rednote-cover-maker)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON MCP tool arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a single confirmed image-generation request path and reports task links, dimensions, task ID, and net charged credits after completion.]

## Skill Version(s):

0.1.2 (source: server evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
