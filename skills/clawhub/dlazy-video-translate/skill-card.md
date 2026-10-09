## Description:

Transcribes video, translates timed subtitles into Simplified Chinese, burns them into an MP4, and optionally adds a fitted dub track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and editors use this skill to make translated videos with timed Chinese subtitles and, when requested, dubbed audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video or audio and generated text are sent to dLazy services.

Mitigation: Confirm that the chosen media may be uploaded before running the skill.

Risk: CLI login stores a dLazy API key on the local machine.

Mitigation: Use DLAZY_API_KEY for one-off runs on shared machines if you do not want a saved key.

Risk: A broad translation request may result in Simplified Chinese subtitles or dubbing when another language was intended.

Mitigation: Confirm the target language and whether dubbing is wanted before processing.

## Reference(s):

- [dLazy CLI source (tool reference, not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Files, Shell commands]

**Output Format:** [MP4 video and SRT subtitles; optional dubbed MP4]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Subtitles default to Simplified Chinese; dubbing runs only when requested.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata; skill frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
