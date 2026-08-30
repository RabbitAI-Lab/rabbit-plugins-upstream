## Description:

Suno Lyrics to Song helps an agent transform existing lyrics, rough drafts, loose lines, or a hook into structured custom lyrics, music direction, and a Beatra/Suno song-generation request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to turn supplied lyric material into a song-ready structure, style prompt, and one approved paid Beatra music generation task. Agents also use it to recover task status, report returned clips, and handle billing or connection errors without duplicate generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broad persistent Beatra Device Token is shared across Beatra skills and grants access beyond a single lyrics-to-song task.

Mitigation: Authorize only when needed, keep the token in the documented private credential file, never expose it in chat or logs, and revoke or uninstall the connection when it is no longer needed.

Risk: Paid music generation can consume Beatra credits after the final production card is approved.

Mitigation: Show the complete lyrics, title, model, options, and music direction before approval; submit once with a stable client_request_id; and recover uncertain delivery with the same request identity.

Risk: Silent package self-updates can change package files before ordinary Beatra commands.

Mitigation: Use the documented update controls to disable automatic checks with update --auto off or inspect availability with update --check.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/suno-lyrics-to-song)
- [Beatra skill homepage](https://beatra.ai/skills/suno-lyrics-to-song)
- [Lyrics intake and modes](references/lyrics-intake-and-modes.md)
- [Song direction and request](references/song-direction-and-request.md)
- [Workflow](references/workflow.md)
- [Review and recovery](references/review-and-recovery.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May lead to Beatra MCP API calls for paid music generation after user approval.]

## Skill Version(s):

0.1.9 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
