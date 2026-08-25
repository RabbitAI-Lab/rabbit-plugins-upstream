## Description:

AI Photo Cleanup Studio helps agents remove selected objects or people from existing photos, filling the cleared area to match surrounding content while preserving the rest of the image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to clean up existing photos by removing named unwanted objects, people, reflections, clutter, or blemishes and returning the edited image after user-confirmed paid Beatra processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device token with broad account access.

Mitigation: Review the requested Beatra permissions before authorizing, keep the token only in the documented credential file, and reconnect with full authorization only when the user explicitly chooses to do so.

Risk: User photos are sent to Beatra for remote processing.

Mitigation: Avoid submitting confidential or sensitive images unless the user accepts that processing, and tell the user when removed areas are reconstructed rather than recovered detail.

Risk: Automatic updates are enabled by default and can replace package files silently.

Mitigation: Use the documented update controls to disable automatic updates or run a manual update check before use.

Risk: Image edits are paid Beatra operations and duplicate submissions can create duplicate charges.

Mitigation: Confirm the photo, target, regions, count, canvas, pass count, and maximum charge before each paid call, then reuse the same request identity only for unchanged recovery.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/beatra-ai/skills/ai-photo-cleanup-studio)
- [Beatra Package Homepage](https://beatra.ai/skills/ai-photo-cleanup-studio)
- [Cleanup Workflow](references/workflow.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Installation Registration](references/installation-registration.md)
- [MCP Connection](references/mcp-connection.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May result in Beatra task IDs, billing details, and edited image artifact references after user-confirmed paid calls.]

## Skill Version(s):

0.1.2 (source: manifest.json and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
