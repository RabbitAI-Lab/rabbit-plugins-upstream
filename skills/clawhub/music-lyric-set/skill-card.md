## Description:

Turn user-supplied song lyrics into a four-to-eight still music lyric card set, with each named lyric section laid out as its own still for lyric card packs, lyric flashcards, and matching lyric graphics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn approved lyric sections into a matching pack of still lyric cards. It guides confirmation, Beatra image generation, task recovery, billing reporting, and review of visible printed text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests a persistent shared Beatra account token with broad media, task, artifact, and wallet authority.

Mitigation: Install only after reviewing the requested access and keep the token private in the documented credential file.

Risk: The bundled client can silently update package code.

Mitigation: Use `python3 scripts/mcp_client.py update --auto off` when automatic updates are not acceptable, and rely on the documented verified update controls.

Risk: Uploading local files sends them to Beatra.

Mitigation: Upload only files intended for Beatra processing and treat scans or photos as visual references, not sources for missing lyric lines.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/music-lyric-set)
- [Beatra Skill Homepage](https://beatra.ai/skills/music-lyric-set)
- [Music lyric card pack workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with JSON MCP payloads, shell command snippets, task metadata, billing details, and generated image artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one image generation task per named lyric section; default pack size is four to eight stills, capped at eight.]

## Skill Version(s):

0.1.2 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
