## Description:

Turn user-supplied song lyrics into a four-to-eight still music lyric card set. This lyric-to-card studio lays out each named lyric section as its own still. Use it for music lyric card packs, lyric flashcards, and matching lyric card graphics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative teams use this skill to plan, approve, generate, review, and deliver still lyric-card packs from lyrics they already supplied. It is designed for section-by-section music lyric card graphics, not audio rendering or public lyric lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device token with broad media-generation, artifact, task, and wallet-spending capabilities.

Mitigation: Review the requested Beatra authorization before installation, keep ~/.beatra private, and use the bundled authorization and uninstall flows rather than copying or deleting credential files manually.

Risk: Billable image generation can create charges or duplicate work if transport failures are handled incorrectly.

Mitigation: Use one opaque client_request_id per frozen request, poll existing tasks before retrying, and resubmit only unchanged requests with the original identity.

Risk: Silent automatic package updates may replace package-owned files without a separate prompt.

Mitigation: Review the documented update behavior and run `python3 scripts/mcp_client.py update --auto off` if silent replacement is not acceptable.

Risk: Generated lyric cards can contain incorrect or invented text if missing lyrics are filled from memory or external sources.

Mitigation: Use only user-supplied lyric sections and lines, keep missing facts as gaps, and review generated text against the confirmed pack list before delivery.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/beatra-ai/skills/music-lyric-set)
- [Music lyric card pack workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured generation payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a labeled pack plan, confirmation text, Beatra task details, billing details, and generated still image artifacts when approved.]

## Skill Version(s):

0.1.1 (source: release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
