## Description:

Turn existing lyrics, rough drafts, loose lines, or a hook into a structured Suno song request with lyrics, title, sections, style direction, and generation recovery steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to convert their own lyric material into a Suno-ready production card, then submit and recover one paid Beatra music generation task after approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra device token can spend credits and access multiple Beatra media and task capabilities, not only Suno music generation.

Mitigation: Install only if the publisher is trusted, keep the token private, and reconnect the account only when that broader Beatra access is intended.

Risk: Paid generation can create charges or duplicates if a request is submitted more than once during uncertainty.

Mitigation: Require approval of a complete production card, submit once, and reuse the same request identity and task ID for recovery of unchanged work.

Risk: Silent automatic updates may replace package-owned files.

Mitigation: Use the documented update --auto off command when silent updates are not acceptable, and rely on the package's fixed-source and checksum verification when updates stay enabled.

Risk: Upload and uninstall commands can affect local files or shared Beatra connection state.

Mitigation: Invoke upload or uninstall flows only when needed, and use the bundled uninstall decision script instead of manually deleting shared Beatra files.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/beatra-ai/skills/suno-lyrics-to-song)
- [Beatra skill homepage](https://beatra.ai/skills/suno-lyrics-to-song)
- [Lyrics intake and modes](references/lyrics-intake-and-modes.md)
- [Song direction and request](references/song-direction-and-request.md)
- [Workflow](references/workflow.md)
- [Review and recovery](references/review-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown production cards with inline JSON and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit one approved paid Beatra/Suno music generation and return task, clip, usage, and billing details.]

## Skill Version(s):

0.1.7 (source: evidence.release.version and artifact manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
