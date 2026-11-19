## Description:

Remove silences, dead air, pauses, and filler words (um, uh) on word boundaries, clean audio noise, generate AI voiceovers and TTS, add background music and sound effects (SFX), and auto-duck music under speech (-18 LUFS).

This skill is ready for commercial/non-commercial use.

## Publisher:

[brajendrak00068](https://clawhub.ai/user/brajendrak00068)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and editors use this skill to tighten spoken audio or video by removing silence and filler words, balancing dialogue, and adding or ducking background music.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Edit prompts, media URLs, and referenced recordings may be shared with Levea for processing.

Mitigation: Before sending a request, confirm that the prompt and media are appropriate to share with Levea.

Risk: Reference coverage is incomplete, so a local path-like reference may not have been assessed.

Mitigation: Check that each referenced media item is expected and accessible before running the edit.

## Reference(s):

- [Levea editing service](https://livecore.ai)
- [Levea API endpoint](https://api.livecore.ai)

## Skill Output:

**Output Type(s):** [API Calls, Media file links, Text]

**Output Format:** [Structured tool responses with project status and an exported MP4 URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exported media is provided by URL after processing.]

## Skill Version(s):

1.0.7 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
