## Description:

Turn Douyin video comments into one comment FAQ still per picked question.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers use this skill to turn pasted or looked-up Douyin comment questions and confirmed product facts into 4 to 8 FAQ still images for listings or comment replies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Beatra connection requests broad media and account permissions beyond the narrow FAQ-still workflow.

Mitigation: Install only when those permissions are acceptable, and revoke the Beatra device authorization when the skill is no longer needed.

Risk: Automatic updates can silently replace bundled executable files before ordinary Beatra commands.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when code review is required before changes run.

Risk: Comment lookup and image generation are paid operations, and incorrect retries can create duplicate work or charges.

Mitigation: Confirm lookup, generation, transform, and edit stages separately; reuse the same `client_request_id` only for byte-identical retries and poll existing tasks before resubmitting.

Risk: Generated FAQ stills may include small or inaccurate text if the source facts are incomplete or the rendered image is not reviewed.

Mitigation: Use only confirmed comment wording and product facts, then inspect each returned still and report only text that is actually visible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/douyin-video-comments-to-faq)
- [Beatra skill homepage](https://beatra.ai/skills/douyin-video-comments-to-faq)
- [Douyin comment FAQ workflow](references/workflow.md)
- [Douyin comment lookup](references/comment-lookup.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a free labeled slot list before paid operations, then reports returned artifacts, task status, dimensions, MIME type, size, and net charged credits when available.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
