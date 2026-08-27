## Description:

Turn seller-supplied new-year store mood notes into one retail playlist of 8 to 15 instrumentals. This new year music studio writes a retail playlist and seasonal store BGM set for doors-open, browse, and close. Use it for new year music, retail playlists, and seasonal store BGM.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and retail operators use this skill to turn already-written new-year store mood notes into a planned and generated pack of 8 to 15 original instrumental tracks for store playback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a broad shared Beatra device authorization rather than a narrow playlist-only grant.

Mitigation: Install only when that account-level authorization is acceptable, keep the token in the documented private Beatra state files, and use the disconnect flow when access is no longer needed.

Risk: Silent package-owned automatic updates are enabled by default.

Mitigation: Disable automatic updates with the documented update command when code changes must be reviewed before execution.

Risk: The bundled client manages shared ~/.beatra state used across Beatra packages.

Mitigation: Treat ~/.beatra as private account state, avoid copying credentials into chat or logs, and use the documented recovery and uninstall flows for cleanup.

Risk: The skill can initiate billable Beatra music generation tasks.

Mitigation: Require explicit confirmation after reading current model pricing, submit each slot once with a stable client_request_id, and recover uncertain responses without creating duplicate paid tasks.

## Reference(s):

- [New-year retail playlist workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/retail-new-year-pack)
- [Beatra package homepage](https://beatra.ai/skills/retail-new-year-pack)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with labeled track lists, inline JSON payloads, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide billable Beatra music generation after explicit confirmation and reports task, duration, and billing details returned by Beatra.]

## Skill Version(s):

0.1.1 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
