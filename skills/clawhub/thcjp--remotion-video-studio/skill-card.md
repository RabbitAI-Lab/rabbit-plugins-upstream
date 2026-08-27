## Description:

Remotion视频工作室 helps agents turn video briefs into Remotion React project files, storyboards, subtitles, animation code, and local render commands for MP4 or WebM output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and marketing teams use this skill to turn product demos, social videos, education content, and data stories into Remotion scenes, subtitles, audio workflow steps, and renderable project files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create files under an output project directory and run local Remotion rendering commands.

Mitigation: Review generated files and commands before execution, and run rendering in a controlled workspace.

Risk: Optional cloud TTS, cloud Whisper, or callback URLs may send prompts, scripts, audio, or callback data to third-party services.

Mitigation: Confirm what content will be sent, use approved services, and keep API keys in environment variables.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/remotion-video-studio)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown instructions with React and TypeScript code blocks, shell commands, and generated project files under output/{project-name}/.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local Remotion project files and provide commands to render MP4 or WebM video outputs.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
