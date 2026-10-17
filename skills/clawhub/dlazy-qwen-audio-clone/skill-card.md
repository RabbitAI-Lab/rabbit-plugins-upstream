## Description:

Helps users clone a custom voice from a clean audio sample for later text-to-speech use through dLazy's hosted Qwen service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use the skill to submit an authorized voice sample and obtain a custom voice for subsequent text-to-speech requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples are uploaded to a hosted service and can contain sensitive biometric data.

Mitigation: Use only samples you have rights and consent to clone; review service data-handling terms before uploading.

Risk: The CLI stores or uses a dLazy API key.

Mitigation: Protect the key, avoid sharing it in prompts or logs, and rotate or revoke it if exposed.

Risk: The published examples contain image-output and --prompt documentation errors.

Mitigation: Check the installed CLI's help and actual response before relying on the examples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy CLI repository (listed in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for providing a voice sample and obtaining a custom voice for later TTS calls; CLI responses may include asynchronous task identifiers.]

## Skill Version(s):

1.3.29 (source: server-resolved ClawHub release; embedded frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
