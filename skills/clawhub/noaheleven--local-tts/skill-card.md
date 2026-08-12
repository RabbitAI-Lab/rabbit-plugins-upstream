## Description:

Local TTS converts text into local MP3 or WAV speech files using edge-tts by default, with a pyttsx3 offline fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[noaheleven](https://clawhub.ai/user/noaheleven)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to turn provided text into speech files for summaries, narration, voice announcements, and local playback workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default online TTS engine may send supplied text to a Microsoft-based service.

Mitigation: Use --offline for secrets, private documents, regulated data, or proprietary text.

Risk: Audio files may be saved under the skill directory when no output path is supplied.

Mitigation: Pass an explicit output path and clean up generated audio according to the caller's retention needs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/noaheleven/skills/local-tts)
- [Publisher profile](https://clawhub.ai/user/noaheleven)
- [README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [MP3 or WAV audio files, with an absolute output path printed as text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The default online engine can fall back to offline pyttsx3; optional playback is Windows-only.]

## Skill Version(s):

1.0.0 (source: frontmatter, changelog, release evidence; released 2026-08-10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
