## Description:

Talking Pet Video helps agents turn one clear pet photo and a short script or approved audio clip into a shareable talking-pet video, with review guidance for identity, mouth motion, speech clarity, and synchronization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content creators use this skill to make short pet greeting, reaction, story, and creator clips from a pet image plus approved speech. Agents use it to inspect media, prepare or upload speech, check current Beatra model constraints, obtain paid approvals, submit generation tasks, poll results, and review returned audio and video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill authorizes a shared Beatra device token with broad account capabilities.

Mitigation: Install only if the user trusts Beatra's service and shared-credential model; keep the device token in the local credential file and do not expose it in chat, command arguments, logs, or other files.

Risk: The skill uploads local media that the user directs it to upload.

Mitigation: Inspect or review local image and audio files before upload, pass only returned artifact references to remote tools, and avoid uploading sensitive media unless the user accepts Beatra processing.

Risk: The bundled client silently self-updates package files by default.

Mitigation: Use the documented update controls, including `python3 scripts/mcp_client.py update --auto off`, when silent update behavior is not acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/talking-pet-video)
- [Beatra Skill Page](https://beatra.ai/skills/talking-pet-video)
- [Talking-pet workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Beatra MCP endpoint](https://mcp.beatra.ai/mcp)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, text]

**Output Format:** [Markdown guidance with JSON examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Beatra task IDs, artifact references, audio or video links, usage details, billing fields, and review notes when available.]

## Skill Version(s):

0.1.6 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
