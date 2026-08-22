## Description:

Music Generation Studio helps an agent turn themes, lyrics, scenes, or reference audio into production briefs, lyrics, generation requests, and reviewable AI-generated music outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, teams, and agent users use this skill to plan, generate, recover, and review songs, instrumentals, background music, jingles, soundtracks, multilingual tracks, and reference-led arrangements through Beatra music tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses broad shared Beatra account authority for multiple media tools.

Mitigation: Install only in accounts where that authority is acceptable, keep tokens private, and reconnect or expand authorization only after explicit user approval.

Risk: The package can silently apply verified updates by default.

Mitigation: Use `python3 scripts/mcp_client.py update --auto off` when explicit update review is required, and rely on the documented verified update flow before re-enabling automatic updates.

Risk: Music generation is billable and duplicate submissions can create unintended charges.

Mitigation: Show the final production card before generation, submit once with a stable request identity, and retry only unchanged requests when recovery is needed.

Risk: Generated vocals, pronunciation, duration, loop points, melody carryover, and mastering are not guaranteed.

Mitigation: Review returned clips against the brief after generation and use a focused new request only when the user approves a revision.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/music-generation-studio)
- [Beatra skill homepage](https://beatra.ai/skills/music-generation-studio)
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
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command snippets and JSON-like generation payload details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report task status, clip metadata, artifact IDs, audio URLs, duration, MIME type, size, returned lyrics, and net charged credits after generation.]

## Skill Version(s):

0.1.5 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
