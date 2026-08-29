## Description:

Turn one kitchen photo the listing already uses into one short clip for the listing page.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External real estate agents, hosts, and listing teams use this skill to plan and generate one short kitchen video clip from one existing kitchen photo while preserving visible room details. It supports photo inspection, model compatibility checks, user approval before paid generation, task polling, and delivery review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra Device Token with broad Beatra scopes.

Mitigation: Install only in trusted agent environments, keep the token out of prompts, logs, command arguments, and environment variables, and use the bundled uninstall flow or Beatra Console revocation when access is no longer needed.

Risk: The workflow uploads local kitchen photos to Beatra for image-to-video generation.

Mitigation: Upload only user-approved photos, inspect the file before upload, and avoid including sensitive or unauthorized listing media.

Risk: Silent automatic updates are enabled by default.

Mitigation: Use the documented update controls to disable automatic checks when local change control or review is required.

Risk: Paid video generation can create charges or duplicate work if requests are resubmitted incorrectly.

Mitigation: Require explicit approval before each billable generation, use one opaque client_request_id per approved payload, and recover uncertain responses with the same unchanged request rather than minting a replacement.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/apartment-kitchen-tour)
- [Beatra Skill Homepage](https://beatra.ai/skills/apartment-kitchen-tour)
- [Kitchen tour workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides one Beatra image-to-video task per approved photo; final media artifacts, usage, and billing details are returned by Beatra task results.]

## Skill Version(s):

0.1.1 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
