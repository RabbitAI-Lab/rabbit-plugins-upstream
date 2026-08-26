## Description:

AI Music Creator helps agents turn a theme, lyric, scene, or reference audio into reviewable songs, instrumentals, background music, and soundtracks with a clear creative direction and focused revisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative teams use this skill to plan lyrics, musical direction, model choice, reference-audio handling, generation requests, and review cycles for AI-created music. It is suited for songs, instrumentals, background music, jingles, video soundtracks, podcast themes, game music, multilingual tracks, and reference-led arrangements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared, persistent Beatra device credential with broad media and wallet-related scopes.

Mitigation: Install only when those scopes are acceptable, keep the credential private, and revoke the connected device from the Beatra Console or use the bundled uninstall workflow when access is no longer needed.

Risk: Selected local reference audio files may be uploaded to Beatra for reference-led generation.

Mitigation: Upload only files the user intentionally selects and is comfortable sending to Beatra; use the bundled upload command so the file and grant checks are applied.

Risk: Automatic updates are enabled by default and may replace package-owned files silently.

Mitigation: Use the documented update controls to disable automatic updates or check manually, and rely on the package's verification and rollback behavior before continuing work.

Risk: Music generation is billable and retries can create duplicate work if request identity is mishandled.

Mitigation: Confirm the final generation payload once, reuse the same request identity only for identical uncertain retries, and recover existing tasks before submitting replacement work.

## Reference(s):

- [AI Music Creator on ClawHub](https://clawhub.ai/beatra-ai/skills/beatra-ai-music-creator)
- [beatra-ai publisher profile](https://clawhub.ai/user/beatra-ai)
- [AI Music Creator homepage](https://beatra.ai/skills/beatra-ai-music-creator)
- [Intent and routing](references/intent-and-routing.md)
- [Creative brief and style](references/creative-brief-and-style.md)
- [Lyrics craft](references/lyrics-craft.md)
- [Vocal, language, and tags](references/vocal-language-and-tags.md)
- [Model routing](references/model-routing.md)
- [Music recipes](references/music-recipes.md)
- [Review and iteration](references/review-and-iteration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Beatra MCP endpoint](https://mcp.beatra.ai/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured generation details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Beatra task IDs, clip metadata, artifact IDs, audio URLs, billing facts, and review notes after a generation task completes.]

## Skill Version(s):

1.3.3 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
