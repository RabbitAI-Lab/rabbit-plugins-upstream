## Description:

Dlazy Audio音频生成 helps agents use the dlazy CLI to generate text-to-speech audio, music, sound effects, and voice clones through dLazy-hosted audio models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and automation teams use this skill to select dLazy audio models, construct dlazy CLI commands, configure API credentials, and process generated audio outputs for voiceover, music, sound effect, and voice-cloning workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local recordings, voice samples, images, or videos may be uploaded to dLazy-hosted services during media workflows.

Mitigation: Confirm the specific files, destination service, and user intent before executing commands that send local media to dLazy.

Risk: The skill can guide agents to execute broad dlazy CLI commands.

Mitigation: Show and confirm the exact dlazy command before execution, especially when commands reference private media paths or remote URLs.

Risk: API keys used for dLazy access could be exposed or over-scoped.

Mitigation: Use a revocable DLAZY_API_KEY with limited scope, avoid echoing secrets, and do not store keys in chat logs or generated files.

Risk: Voice cloning or media generation may involve protected voices, recordings, or copyrighted material.

Mitigation: Require user confirmation that they have the necessary rights and consent before processing voice samples or protected media.

## Reference(s):

- [ClawHub skill release: dlazy-audio-generate](https://clawhub.ai/thcjp/skills/dlazy-audio-generate)
- [ClawHub publisher profile: thcjp](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown]

**Output Format:** [Markdown guidance with inline bash commands and JSON result handling notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to run dlazy commands that call dLazy-hosted services and return generated media URLs or local output paths.]

## Skill Version(s):

1.0.2 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
