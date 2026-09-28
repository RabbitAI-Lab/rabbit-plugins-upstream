## Description:

Guides an agent through transcribing and translating video, burning in subtitles, and optionally adding a timing-matched dub.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and editors use this skill to translate video speech into timed subtitles and, when requested, produce a dubbed video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio and local media supplied to the workflow are uploaded to dLazy services.

Mitigation: Avoid confidential videos unless uploading them is acceptable; review dLazy service terms first.

Risk: The CLI may store an API key locally.

Mitigation: Use a per-invocation DLAZY_API_KEY if you do not want a stored key, and review the pinned CLI package before installation.

Risk: Transcription, translation, and optional dubbing can incur charges.

Mitigation: Confirm the target language and estimated cost before paid steps; use the documented dry-run option when appropriate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Executing the workflow produces an MP4 with burned-in subtitles and SRT files; a dubbed MP4 is optional.]

## Skill Version(s):

1.0.14 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
