## Description:

Automates text-to-video generation with multi-provider TTS/ASR support, timestamp extraction, scene detection, and local Remotion rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhenstaff](https://clawhub.ai/user/zhenstaff)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content automation users use this skill to turn short scripts into vertical videos with generated speech, timed subtitles, scene styling, and optional background video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Script text and generated audio may be sent to configured cloud TTS or ASR providers.

Mitigation: Use the skill only for content that can be shared with the selected provider, and get explicit user confirmation before sending content to external APIs.

Risk: Troubleshooting instructions may expose local credentials by printing the .env file.

Mitigation: Do not display secrets in terminal output; verify configuration with redacted checks and keep credentials scoped and revocable.

Risk: Mutable source installs can change over time.

Mitigation: Prefer the pinned npm package or verify the source commit before cloning and running project commands.

Risk: The skill can ask an agent to install software and execute local shell commands.

Mitigation: Require user confirmation before installation or execution, and review commands before running them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhenstaff/skills/video-generator)
- [Project Homepage](https://github.com/ZhenRobotics/openclaw-video-generator#readme)
- [npm Package](https://www.npmjs.com/package/openclaw-video-generator)
- [GitHub Issues](https://github.com/ZhenRobotics/openclaw-video-generator/issues)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create audio files, timestamp JSON, scene configuration, and MP4 video files through the external generator.]

## Skill Version(s):

1.0.42 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
