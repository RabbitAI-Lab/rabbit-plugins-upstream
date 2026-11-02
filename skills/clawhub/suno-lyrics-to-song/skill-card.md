## Description:

Turn existing lyrics or rough lyric ideas into a structured Suno song, with lyrics preserved or refined and music direction for style, mood, arrangement, and vocals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and songwriters can organize complete lyrics, drafts, loose lines, or a hook into labeled song sections, shape or preserve the wording, and prepare music direction for Suno song generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorization covers other media-generation tools, voice management, spending, and a credential shared with other Beatra skills.

Mitigation: Review the requested access before authorizing, and prefer a release with music-only permissions when available.

Risk: This release has an uninstall flaw, and revoking its shared device credential in Beatra Console also disconnects other skills using it.

Mitigation: Prefer a release with corrected uninstall handling; consider other installed Beatra skills before revoking the shared device.

Risk: Lyrics are sent to Beatra for generation, and installation analytics are automatic.

Mitigation: Avoid submitting lyrics you do not want sent to Beatra, and account for automatic installation analytics.

## Reference(s):

- [Beatra skill page](https://beatra.ai/skills/suno-lyrics-to-song)
- [Lyrics intake and modes](artifact/references/lyrics-intake-and-modes.md)
- [Song direction and request](artifact/references/song-direction-and-request.md)
- [Workflow](artifact/references/workflow.md)
- [Updates and security](artifact/references/updates-and-security.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Audio links]

**Output Format:** [Markdown with section-labeled lyrics, music direction, and returned track links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lyrics can be preserved or refined; generated track links are included when generation succeeds.]

## Skill Version(s):

0.3.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
