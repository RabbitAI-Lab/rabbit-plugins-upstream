## Description:

Create a short visual clip guided by a song's mood, rhythm, and visual concept.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative teams use this skill to turn a finished music excerpt and visual direction into a short music-driven promo clip, cover-art animation, lyric-led visual, or mood visual. The skill guides media inspection, route selection, Beatra task submission, polling, and result reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses broad Beatra account permissions through a shared device token.

Mitigation: Review the requested Beatra authorization before installation, keep the token only in the documented local credential file, and disconnect through the bundled uninstall workflow when access is no longer needed.

Risk: The skill can upload user-selected local media.

Mitigation: Inspect local files before upload, avoid sensitive or uncleared media, and preserve returned artifact references instead of exposing local paths.

Risk: Silent automatic updates are enabled by default.

Mitigation: Use the documented update control command to disable automatic checks when manual review of package updates is required.

Risk: Billable Beatra generation calls can spend credits.

Mitigation: Show the admission card before paid video submission, freeze one request identity per paid stage, and report terminal billing from the completed task response.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/ai-music-video-clip-maker)
- [Beatra skill homepage](https://beatra.ai/skills/ai-music-video-clip-maker)
- [Music video clip workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Text, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload local media, submit asynchronous Beatra generation tasks, poll task state, and return generated video artifacts or links with actual usage and billing details.]

## Skill Version(s):

0.1.4 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
