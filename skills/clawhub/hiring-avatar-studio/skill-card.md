## Description:

Turn one HR or founder portrait and a job brief into one talking-avatar hiring video per open role. This hiring avatar studio and recruitment avatar workflow can clone or pick a voice, then produce a hiring talking head clip that walks through the role, requirements, and next step. Use it for recruiting video, job posting video, job opening presenter clips, and a hiring video studio that keeps each new role on camera.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

HR teams, founders, recruiters, and their agents use this skill to turn an authorized portrait plus a role brief, script, or approved speech track into talking-head hiring videos. It guides consent checks, voice selection or cloning, narration, video generation, task polling, billing review, and delivery of role-labeled clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a broad Beatra Device Token locally and uses it for account, artifact, speech, voice, video, wallet, and task operations.

Mitigation: Install only when the user accepts Beatra as the credential authority, keep the token in the documented private credentials file, avoid exposing it in chat, logs, command arguments, environment variables, or other files, and use the bundled authorization and uninstall flows to reconnect or revoke access.

Risk: Voice cloning and portrait animation can create identity-sensitive hiring videos and require clear likeness and voice rights.

Mitigation: Confirm rights for the portrait and voice before generation, treat access to a media file as insufficient consent, and stop before clone or video submission if authorization is missing.

Risk: Generation calls can spend Beatra credits, and estimates may differ from final measured usage.

Mitigation: Show admission cards before paid clone, narration, and video calls; submit each paid stage once with a stable client_request_id; poll task results; and report authoritative billing.net_charged_credits after completion.

Risk: The bundled client silently checks for and installs verified package updates by default.

Mitigation: Review the automatic update posture before installing and disable silent update checks with the documented update command when the user wants manual update control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/hiring-avatar-studio)
- [Beatra skill homepage](https://beatra.ai/skills/hiring-avatar-studio)
- [Hiring avatar workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payload examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides Beatra MCP calls that can create speech, cloned voices, and hiring-avatar video task artifacts.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
