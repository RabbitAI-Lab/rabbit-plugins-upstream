## Description:

Create a short visual clip guided by a song's mood, rhythm, and visual concept.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through planning, authorizing, submitting, polling, and reviewing short AI music-video clips from finished songs or excerpts. It supports promo teasers, cover-art animation, mood visuals, virtual performer scenes, and social music clips when the user has the necessary media rights.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Beatra account powers through a shared device credential.

Mitigation: Review the approval scope before authorizing, keep the credential private, and revoke the device from the Beatra Console when access is no longer needed.

Risk: Automatic package self-updates are enabled by default.

Mitigation: Disable silent updates with `python3 scripts/mcp_client.py update --auto off` when a fixed reviewed package version is required.

Risk: Billable media generation can consume Beatra credits and initial estimates may differ from terminal charges.

Mitigation: Require explicit user confirmation before paid video calls, submit each logical request once, and report only returned `billing.net_charged_credits`.

Risk: Installation and device telemetry may be sent for package registration and source attribution.

Mitigation: Tell users that package slug, version, platform, and source attribution can be recorded and that missing telemetry must not block creative work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/ai-music-video-clip-maker)
- [Beatra skill homepage](https://beatra.ai/skills/ai-music-video-clip-maker)
- [Music video clip workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [MCP connection](references/mcp-connection.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON MCP payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May lead the agent to submit Beatra generation tasks and return video artifacts or links; final usage and billing should be taken from Beatra task responses.]

## Skill Version(s):

0.1.5 (source: server release evidence, manifest.json, bundled script constants)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
