## Description:

Generates 9:16 vertical short videos from Markdown scripts with automatic storyboarding, optional prepared images, configurable TTS commands, subtitle controls, and MP4 output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, developers, and automation teams use this skill to turn Markdown video scripts into vertical short-form videos with generated scenes, narration, subtitles, and configurable media-processing options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted script paths, image folders, or TTS command templates may cause the agent to read unexpected files, write unwanted outputs, or run unintended local media commands.

Mitigation: Use trusted input paths and TTS command templates, keep outputs in an expected working directory, and review proposed commands before execution.

Risk: Configured API keys or TTS credentials may be exposed through command text, logs, or generated files.

Mitigation: Pass credentials through environment variables or a secret manager, avoid committing them to version control, and review logs before sharing.

Risk: Generated videos may include copyrighted or otherwise restricted source content.

Mitigation: Use only media and scripts the user has rights to process, and review generated outputs for legal and policy compliance before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/lh-video-gen)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with bash command examples, configuration values, and generated MP4 file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read Markdown scripts and image folders, invoke configured local media or TTS commands, and write video outputs.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
