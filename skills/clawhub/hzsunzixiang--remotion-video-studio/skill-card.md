## Description:

Video by Remotion helps agents scaffold and run a Remotion-based pipeline that turns JSON narration scripts into animated explainer videos with TTS audio, subtitles, and optional custom scenes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hzsunzixiang](https://clawhub.ai/user/hzsunzixiang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and content creators use this skill to create educational or explainer videos, animated presentations, data visualization videos, and narrated programmatic videos from structured content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated project scripts can be abused through untrusted configuration or subtitle JSON to run shell commands or write outside the project folder.

Mitigation: Use only trusted configuration and subtitle content, review before installing, and run generated projects in an isolated directory or disposable environment.

Risk: The Edge TTS path sends slide narration text to the Microsoft Edge TTS service.

Mitigation: Avoid sensitive narration when using Edge TTS; use the local Qwen TTS path when offline processing is required.

Risk: The security evidence recommends stronger path containment, safer subprocess invocation, and locked dependencies.

Mitigation: Prefer a version that fixes those areas before production deployment, and review dependency and command behavior before use.

## Reference(s):

- [Configuration Reference](references/config-reference.md)
- [Animation Components Reference](references/animation-components.md)
- [Remotion Core Rules Reference](references/remotion-rules.md)
- [ClawHub skill page](https://clawhub.ai/hzsunzixiang/skills/remotion-video-studio)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with inline bash, JSON, Python, and TypeScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated project pipeline can produce MP4 video, TTS audio files, subtitle files, and Remotion render props.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
