## Description:

Generate one short directed transition from an approved first frame to an approved last frame, turning two images into one clip that begins and ends on those images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and agents use this skill to turn two approved endpoint images into one short Beatra video transition for transformations, product reveals, before-and-after stories, day-to-night shifts, scene changes, and cinematic endpoints. It guides endpoint inspection, live model admission, paid submission, task polling, billing reporting, and post-result review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a persistent shared Beatra device token with permission to spend credits and access broader media and task capabilities.

Mitigation: Install only for trusted Beatra accounts, keep the credential file private, avoid sharing sensitive media, and revoke the device connection from Beatra or run the bundled uninstall flow when access is no longer needed.

Risk: Automatic package updates are enabled by default and can replace executable code before ordinary commands.

Mitigation: Review the package before installation and disable silent updates with `python3 scripts/mcp_client.py update --auto off` when change control is required.

Risk: Video generation is paid work and a duplicate submission can spend additional credits.

Mitigation: Require explicit approval after the admission card, freeze one `client_request_id` per paid stage, and recover uncertain submissions with the same frozen payload instead of creating replacements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/first-last-frame-video)
- [Beatra Skill Homepage](https://beatra.ai/skills/first-last-frame-video)
- [First-and-last-frame workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API Calls]

**Output Format:** [Markdown guidance with inline shell commands, JSON tool payloads, and returned video artifact links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one transition workflow at a time and reports returned task status, media artifacts, resolved generation details, usage, and net charged credits when available.]

## Skill Version(s):

0.1.5 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
