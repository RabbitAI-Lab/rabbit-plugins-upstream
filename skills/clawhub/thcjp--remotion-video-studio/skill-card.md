## Description:

Remotion Video Studio helps agents plan scripts and generate React/Remotion video projects with scenes, subtitles, animation, rendering commands, and optional TTS or transcription steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content teams use this skill to turn video briefs into Remotion project structure, React scene components, subtitle timelines, script tables, and local render commands for product demos, social videos, educational clips, and data visualizations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may create project files and propose local Node/Remotion rendering commands.

Mitigation: Approve the output directory and each render command before execution, and run rendering in a scoped workspace or sandbox.

Risk: Optional TTS, Whisper, or callback URL use may send script, audio, or status data to external services.

Mitigation: Use only approved services and URLs, review the data being sent, and provide any API keys through environment variables.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/remotion-video-studio)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with React/TypeScript code blocks and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe files under output/{project-name}/src/, output/{project-name}/script.md, and Remotion render commands.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
