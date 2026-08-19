## Description:

Create YouTube thumbnails from a video topic, title, script, key frame, portrait, product photo, or channel reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, channel operators, and video teams use this skill to turn YouTube video concepts or source images into thumbnail directions, a selected 16:9 rendered image, title-matching advice, and a reusable channel consistency rule.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses broad shared Beatra account authorization for image, video, music, speech, upload, model, and task tools.

Mitigation: Install only if the user trusts Beatra with that authorization, review account scopes during approval, and use the bundled disconnect or uninstall flow when access is no longer needed.

Risk: Submitted media and prompts may include confidential, third-party, or rights-sensitive material.

Mitigation: Avoid uploading confidential or third-party content unless permitted, and keep title claims, names, credentials, and channel facts limited to information supplied by the user.

Risk: The bundled client silently checks for and installs newer releases by default.

Mitigation: Review the automatic update behavior and disable it after installation with `python3 scripts/mcp_client.py update --auto off` when a fixed local version is required.

Risk: Rendering and revisions consume Beatra credits, and duplicate or changed requests can create additional paid work.

Mitigation: Require a clear paid-work confirmation, preserve the original `client_request_id` for uncertain responses, and treat changed prompts, inputs, canvas, model, count, or embedded text as new paid work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/youtube-thumbnail-maker)
- [Beatra skill homepage](https://beatra.ai/skills/youtube-thumbnail-maker)
- [Thumbnail workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON payload examples and shell commands; completed runs may return image artifact links and task facts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces thumbnail directions, paid-work confirmations, Beatra task status, billing facts, title-matching notes, and channel consistency guidance.]

## Skill Version(s):

0.2.0 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
