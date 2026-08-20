## Description:

This skill helps agents extract MP3 or WAV audio from local video files or direct video URLs with ffmpeg, and resolve supported social sharing links through qhkit before extraction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, operators, and content-production agents use this skill to pull background music, voice tracks, or other audio from video media for editing workflows. It is most useful when a user provides a local video, a direct video URL, or a supported platform sharing link that must be resolved before ffmpeg extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Link-based extraction depends on the third-party qhkit service and may require a qhkit API token.

Mitigation: Confirm the service and token requirements before use, and avoid sending media links that should not be processed by a third-party service.

Risk: Extracted audio may include copyrighted background music or other protected content.

Mitigation: Use only media the user is allowed to process and check music rights before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-audio-extract)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix workspace](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Files]

**Output Format:** [Markdown with inline bash code blocks and local file path guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces or points to extracted MP3 or WAV audio files when the agent environment can access the source media and required tools.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
