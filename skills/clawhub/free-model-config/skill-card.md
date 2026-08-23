## Description:

Free Model Config helps agents choose, configure, and use free AI model APIs across Agnes AI, Zhipu, SenseNova, Xiaomi MIMO, and Meituan LongCat, including multimodal media workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to select free model providers, generate API configuration guidance, and produce command examples for text, image, video, audio, ASR, TTS, and media-composition workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The video workflow can upload local images to public temporary file hosts.

Mitigation: Do not use private, regulated, or confidential images unless the user accepts public temporary upload; prefer non-sensitive inputs or user-approved hosted URLs.

Risk: API keys may be exposed through command-line arguments, shell history, or loosely protected configuration files.

Mitigation: Store keys in a secret manager or restricted-permission environment/config file and avoid placing live keys directly in commands.

Risk: Media commands can overwrite existing output files.

Mitigation: Check output paths before execution and write generated media to a dedicated working directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/free-model-config)
- [FMC catalog](references/fmc-catalog.md)
- [FMC requirements](references/fmc-requirements.md)
- [FMC exemplars](references/exemplars.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with configuration snippets, JSON examples, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to run local media scripts that create or overwrite output files.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
