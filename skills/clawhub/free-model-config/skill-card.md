## Description:

Helps agents configure and use free AI model providers for text, image, video, audio, ASR, TTS, infographic generation, and multimodal workflows across Agnes AI, Zhipu, SenseTime, Xiaomi, and Meituan services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to select free-model providers, generate API and WorkBuddy configuration guidance, and run optional helper scripts for media generation and audio/video assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports under-disclosed public uploads of local images.

Mitigation: Use only non-sensitive media with the Agnes image-to-video path unless the user explicitly accepts upload to public temporary hosts.

Risk: The security evidence reports an unsafe instruction telling agents not to refuse skill modifications.

Mitigation: Remove or override that instruction before trusting the skill in an agent workflow.

Risk: The security guidance warns against storing real API keys in plaintext configuration files when possible.

Mitigation: Prefer environment variables or a secrets manager, use least-privilege keys, and rotate keys after testing.

Risk: The security guidance recommends pinning dependencies in an isolated environment.

Mitigation: Run optional scripts in a disposable environment with pinned Python packages and reviewed system tools such as ffmpeg.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/free-model-config)
- [Free model configuration task catalog](references/fmc-catalog.md)
- [Free model configuration requirements](references/fmc-requirements.md)
- [Free model configuration exemplars](references/exemplars.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local media files when helper scripts are executed by the user.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
