## Description:

Free Model Config helps agents standardize configuration and usage guidance for free AI model providers, including API key handling, model selection, text/image/video/audio generation workflows, ASR/TTS guidance, and audio/video helper commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, builders, and agent users use this skill to select free model providers, generate API and configuration guidance, and run optional helper workflows for image, video, audio, TTS, and audio/video merge tasks. It is especially relevant for users managing provider API keys and reusable model configuration files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner reports a safety-override instruction in the skill text.

Mitigation: Remove or disregard the non-refusal instruction before modifying or deploying the skill, and apply the host agent's normal safety and review policies.

Risk: Local image-to-video inputs may be uploaded automatically to public third-party file hosts.

Mitigation: Use only dummy or non-sensitive media for testing, prefer already public URLs when appropriate, and avoid local image inputs unless public upload is acceptable.

Risk: The skill works with API keys through command-line arguments, environment variables, and ~/.workbuddy/models.json.

Mitigation: Avoid passing real API keys on the command line, protect the models.json file, use placeholders in shared outputs, and rotate keys if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/free-model-config)
- [Free model configuration catalog](references/fmc-catalog.md)
- [Free model configuration requirements](references/fmc-requirements.md)
- [Free model configuration exemplars](references/exemplars.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON configuration snippets, shell commands, and optional local media files from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may reference API keys, provider endpoints, local configuration paths, and generated media files depending on the requested workflow.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
