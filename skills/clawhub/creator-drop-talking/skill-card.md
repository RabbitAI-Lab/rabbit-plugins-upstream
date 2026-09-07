## Description:

Turn a confirmed new-drop script and authorized stills into one drop talking clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, sellers, and listing teams use this skill to turn authorized still images and confirmed product-drop facts into short talking launch teasers. It helps an agent plan slots, confirm paid Beatra speech/video steps, and deliver one clip per still without inventing drop claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra Device Token stored on the user's machine.

Mitigation: Keep the token only in the documented private credential file, never expose it in chat, command arguments, environment variables, logs, or package directories, and use the bundled uninstall workflow when disconnecting.

Risk: Paid clone, speech, and video operations can spend Beatra credits.

Mitigation: Show the user a separate confirmation card with live pricing and a fresh client_request_id for each paid stage, submit each approved request once, and rely on Beatra task billing fields for final charges.

Risk: The package can silently update itself before ordinary Beatra commands.

Mitigation: Review the package before installation, use the documented update controls to disable automatic checks when needed, and rely on the updater's package, manifest, archive, and file checksum verification.

Risk: Talking clips may involve likeness or voice rights.

Mitigation: Require explicit likeness and voice authorization before using faces or cloned voices, and treat file access as insufficient consent.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/creator-drop-talking)
- [Beatra Skill Homepage](https://beatra.ai/skills/creator-drop-talking)
- [Drop talking-clip workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides Beatra model, upload, speech, video, wallet, task, update, and uninstall operations through bundled scripts; generated media artifacts are returned by Beatra tasks.]

## Skill Version(s):

0.1.3 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
