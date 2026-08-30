## Description:

Turns a theme, lyric, scene, or reference audio into reviewable songs, instrumentals, background music, and soundtracks with a clear creative direction and focused revisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to plan and generate original songs, lyrics-to-song tracks, instrumentals, background music, jingles, multilingual music, and reference-led arrangements while keeping model choice, billing, and revision boundaries visible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Beatra authorization grants a shared full-scope device token that can be used beyond music generation.

Mitigation: Install only if the user trusts Beatra's account, billing, telemetry, and service infrastructure; keep credentials private and use the bundled disconnect or uninstall flow when access should be removed.

Risk: Ordinary Beatra commands may silently update package files by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when manual review of code changes is required, and use the documented update check before accepting a new version.

Risk: Music generation consumes Beatra credits and can create duplicate paid work if a request is resubmitted incorrectly.

Mitigation: Make the final model, prompt, lyrics or instrumental status, reference, controls, and one-generation scope visible before submission; preserve the task ID and request identity during recovery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/beatra-ai-music-creator)
- [Beatra skill homepage](https://beatra.ai/skills/beatra-ai-music-creator)
- [Intent and routing](references/intent-and-routing.md)
- [Creative brief and style](references/creative-brief-and-style.md)
- [Lyrics craft](references/lyrics-craft.md)
- [Vocal, language, and tags](references/vocal-language-and-tags.md)
- [Model routing](references/model-routing.md)
- [Music recipes](references/music-recipes.md)
- [Review and iteration](references/review-and-iteration.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown and structured task or artifact summaries with inline shell commands and JSON request details when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include titles, lyrics, production cards, model choices, task IDs, clip URLs, artifact IDs, duration, MIME type, file size, and net charged Beatra credits returned by the service.]

## Skill Version(s):

1.3.5 (source: server release metadata and artifact/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
