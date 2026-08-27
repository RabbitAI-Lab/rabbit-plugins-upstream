## Description:

Extracts audio from local video files or direct video URLs into MP3 or WAV, and can use qhkit to resolve supported platform share links before extraction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, editors, and agents use this skill to extract BGM, voice tracks, or other audio from videos for editing and reuse. When a user provides a platform share link rather than a direct video URL, the skill guides qhkit resolution before ffmpeg extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: qhkit link parsing can consume account credits when creating a video-inspire task.

Mitigation: Tell the user which link will be parsed, explain that actual charges may apply, and wait for explicit approval before running the generate command.

Risk: Using qhkit requires installing a package and storing an API token locally.

Mitigation: Confirm the user is comfortable installing qhkit and keep the API token in the local qhkit configuration rather than exposing it in shared output.

Risk: Extracted music or voice tracks may carry copyright or platform-use restrictions, especially for commercial reuse.

Mitigation: Remind users to confirm they have rights to reuse extracted audio before commercial publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-audio-extract)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix workspace](https://www.iqinghu.com)
- [qhkit API key setup tutorial](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands, local file paths, and optional MP3 or WAV audio file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ffmpeg for local extraction; qhkit link parsing may require Node.js, an API token, and explicit user approval before credit-consuming task creation.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
