## Description:

Transforms supplied lyrics or lyric ideas into structured, Suno-ready song lyrics and a music-direction prompt, with options to preserve or refine the original words.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and songwriters use this skill to organize complete lyrics, rough drafts, loose lines, or hooks into a structured song. With user approval, it submits the lyrics and music direction for generation through Beatra.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra authorization grants media, voice, and credit permissions beyond song generation and may be reused by other Beatra skills; the song-generation approval does not enforce a song-only access boundary.

Mitigation: Review the requested permissions before authorizing, and revoke the device in Beatra's console when shared access should end.

Risk: Installation analytics run automatically.

Mitigation: Consider the automatic analytics when deciding whether to install; do not install if that collection is unacceptable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/suno-lyrics-to-song)
- [Beatra](https://beatra.ai/skills/suno-lyrics-to-song)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Audio]

**Output Format:** [Structured Markdown lyrics and music-direction prompt; generated song audio when requested and approved]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lyrics up to 5,000 characters; music-direction prompt 1–1,000 characters; title up to 80 characters; paid generation requires user approval.]

## Skill Version(s):

0.2.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
