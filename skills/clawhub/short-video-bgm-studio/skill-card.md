## Description:

Describe the footage and get an original instrumental track written for it, yours to keep and use commercially. This AI background music generator turns a scene, mood, and tempo feel into royalty-free BGM for short videos, vlogs, product clips, tutorials, livestream and store loops, podcast intros, and slideshow recaps, with an energy arc you choose: a calm or immediate opening, a lift at the moment that matters, a clean ending, room left for narration, and a result you can listen to before you publish.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, educators, and agents use this skill to turn a video or brand moment description into an original instrumental background track for short-form video, livestream, podcast, store loop, or slideshow use. It guides prompt planning, paid Beatra music generation, task recovery, and delivery of returned audio artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra device authorization covers more than the music-only purpose of this skill.

Mitigation: Review the authorization before installing, protect the credential stored under ~/.beatra, and revoke or reconnect access only when the user explicitly chooses to do so.

Risk: Silent package-owned code updates are enabled by default.

Mitigation: Disable automatic checks with python3 scripts/mcp_client.py update --auto off when silent updates are not acceptable; use the documented check/update commands for controlled updates.

Risk: Chosen reference audio and limited installation or platform metadata may be sent to Beatra.

Mitigation: Upload only reference audio the user is authorized to share, avoid sensitive media, and explain the upload before using reference-guided generation.

Risk: Paid generation can create duplicate work or charges if a request is replayed with changed arguments.

Mitigation: Confirm the frozen prompt, model, options, and maximum charge before submission; preserve the client_request_id and task_id, and recover the existing task before considering any new paid call.

## Reference(s):

- [BGM workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub listing](https://clawhub.ai/beatra-ai/skills/short-video-bgm-studio)
- [Beatra skill homepage](https://beatra.ai/skills/short-video-bgm-studio)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Files, Guidance]

**Output Format:** [Markdown guidance with JSON payload examples, shell commands, and returned audio artifact links or IDs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Beatra device authorization; billable generation requires explicit confirmation and uses asynchronous task polling.]

## Skill Version(s):

0.1.3 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
