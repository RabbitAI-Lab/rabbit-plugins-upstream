## Description:

Creates a talking-avatar video from one portrait and either an approved speech track or a short script with a selected voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, training teams, product teams, and developers use this skill to prepare a single presenter-style clip for explainers, onboarding, lessons, announcements, and product messages from reviewed portrait and narration inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portraits, scripts, and speech inputs are sent to Beatra services for generation.

Mitigation: Use only inputs the user is comfortable sharing with Beatra, and require privacy-sensitive or enterprise users to review the data-sharing model before installation.

Risk: The package stores a shared full-scope Beatra device token locally.

Mitigation: Restrict local credential file access, avoid exposing tokens in commands or logs, and use the uninstall or revocation flow when access should be removed.

Risk: The bundled client silently checks for and installs verified package updates by default.

Mitigation: Disable automatic update checks with scripts/mcp_client.py update --auto off when change control or manual review is required.

Risk: Narration and video generation are paid stages that can create duplicate charges if retried with changed request data.

Mitigation: Freeze each approved payload with a stable request ID, recover uncertain submissions before retrying, and start changed work only after fresh approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/talking-avatar-video)
- [Beatra skill page](https://beatra.ai/skills/talking-avatar-video)
- [Narration-first presenter workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Beatra MCP endpoint](https://mcp.beatra.ai/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON MCP payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Beatra task status, billing facts, and generated audio or video artifact links when remote generation succeeds.]

## Skill Version(s):

0.1.6 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
