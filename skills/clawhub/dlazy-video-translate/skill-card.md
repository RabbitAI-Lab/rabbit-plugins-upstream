## Description:

Transcribes video with word-level timings, translates the subtitles, burns them into the video, and optionally creates a timing-fitted dub track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content creators use this skill to translate a video's speech, produce translated SRT subtitles and a subtitled MP4, and optionally add a dubbed audio track.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The reported security concern includes overwriting existing files without warning.

Mitigation: Run the workflow in a dedicated working directory, check output names, and back up files before processing.

Risk: Authentication stores an API key in the local CLI configuration, and media is sent to dLazy services for processing.

Mitigation: Protect the local configuration, review media before processing, and rotate or revoke the API key if it may be exposed.

Risk: The security summary flags fixed translation instructions, and scanner coverage was partial.

Mitigation: Review the requested target language and generated subtitles, and inspect unresolved references before relying on the result.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [CLI package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [CLI homepage (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [MP4 video files, SRT subtitle files]

**Output Format:** [MP4 video and SRT subtitle files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Subtitled video is the default; dubbed audio is optional.]

## Skill Version(s):

1.0.32 (source: server-resolved release metadata; artifact frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
