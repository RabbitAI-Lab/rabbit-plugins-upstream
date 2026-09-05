## Description:

Transcribes source-video audio with word-level timing, translates subtitle cues, burns subtitles into video, and optionally assembles a fitted dubbed audio track using dLazy CLI tools with local ffmpeg.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operators use this skill to guide an agent through video translation, subtitle generation, subtitle burn-in, and optional dubbing for user-provided media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-selected videos, extracted audio, and related local files are uploaded to dLazy cloud services for processing.

Mitigation: Run the workflow only with media that may be sent to dLazy, and review dLazy service terms before processing sensitive content.

Risk: The dLazy API key may be stored locally in the user configuration directory.

Mitigation: Prefer per-session use of DLAZY_API_KEY on shared machines, or run dlazy logout after use.

Risk: Long videos and dubbing can incur dLazy credits because ASR, LLM translation, and TTS are billed operations.

Mitigation: Use --dry-run to inspect payloads and cost estimates before running long or dubbed videos.

Risk: The workflow installs or invokes a third-party CLI package.

Mitigation: Review the pinned @dlazy/cli package and source before installation or execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-translate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands, JSON snippets, SRT subtitle files, and MP4 media outputs when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided media, a dLazy API key, network access to dLazy services, and local ffmpeg/ffprobe.]

## Skill Version(s):

1.0.5 (source: server release evidence; artifact frontmatter is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
