## Description:

Create a Bilibili video storyboard from a topic, title, outline, or script. This AI Bilibili storyboard maker turns a long-form video idea into a chapter-led shot list, Bilibili video script, camera direction, narration and B-roll cues, and one to four storyboard key frames for explainers, reviews, tutorials, vlogs, gameplay, animation, and creative videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Bilibili creators, editors, directors, and AI-video artists use this skill to turn a topic, outline, title, or script into a reviewable chapter-led shot list and a small set of approved storyboard key frames before production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary states that the skill uses broad persistent account access that can spend credits and access broader generation tools than the storyboard workflow needs.

Mitigation: Install only if the user trusts Beatra, protect the persistent Device Token, and revoke the device from the Beatra Console or bundled uninstall flow when the skill is no longer needed.

Risk: The security summary states that silent automatic updates are enabled by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when reviewed-code stability is required, and use manual update checks before accepting a newer release.

Risk: The skill can submit paid generation tasks, and uncertain transport recovery can create duplicate work if request identity is not preserved.

Mitigation: Freeze the approved request, use one opaque `client_request_id`, save returned task IDs, poll existing tasks, and retry only byte-equivalent requests with the same request identity.

## Reference(s):

- [Bilibili storyboard planning and key frames](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/bilibili-video-storyboard)
- [Beatra skill homepage](https://beatra.ai/skills/bilibili-video-storyboard)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured shot lists, image prompts, command examples, and returned task or artifact details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include one to four approved key-frame requests; reports task IDs, dimensions, formats, resolved model, and charge facts when available.]

## Skill Version(s):

0.1.4 (source: manifest.json and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
