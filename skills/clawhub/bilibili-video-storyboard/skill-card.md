## Description:

Create a Bilibili video storyboard from a topic, title, outline, or script. This AI Bilibili storyboard maker turns a long-form video idea into a chapter-led shot list, Bilibili video script, camera direction, narration and B-roll cues, and one to four storyboard key frames for explainers, reviews, tutorials, vlogs, gameplay, animation, and creative videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, editors, directors, and AI-video artists use this skill to turn a Bilibili topic, title, outline, or script into a chapter-led shot list and selected storyboard key frames for video production planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Beatra device credential and paid media-generation authority.

Mitigation: Install only when that access is acceptable, review paid key-frame requests before approval, and revoke the Beatra device in the Beatra Console when the installation is no longer trusted.

Risk: Selected local reference files may be uploaded for key-frame generation.

Mitigation: Upload only references that are appropriate to share with Beatra and label each reference role before generation.

Risk: Automatic package updates are enabled by default.

Mitigation: Disable silent update checks with `python3 scripts/mcp_client.py update --auto off` if automatic replacement is not acceptable.

Risk: Paid generation retries can duplicate work or charges if request identity changes after transport uncertainty.

Mitigation: Recover uncertain paid requests with the same `client_request_id` and unchanged arguments, and poll existing task IDs before submitting again.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/bilibili-video-storyboard)
- [Bilibili storyboard planning and key frames](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [MCP connection](references/mcp-connection.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with shot lists, key-frame plans, approval summaries, artifact references, and inline shell commands when setup or recovery is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include returned task identities, model names, dimensions, formats, and billing facts for approved paid key-frame generations.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
