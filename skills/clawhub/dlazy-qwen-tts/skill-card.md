## Description:

Alibaba Bailian qwen3-tts text-to-speech lets agents choose curated system voices, including dialect voices, or design a custom voice from a natural-language description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to generate text-to-speech audio through the dLazy CLI and hosted Qwen TTS service, selecting a system voice or describing a custom voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill delegates execution to a third-party CLI and hosted cloud API.

Mitigation: Review the pinned @dlazy/cli package before installation and run it only in environments where third-party CLI execution is acceptable.

Risk: Prompts and selected inputs may be sent to dLazy cloud services, and local file paths passed to media fields may be uploaded.

Mitigation: Avoid passing private or regulated content unless cloud processing by dLazy is approved for the use case.

Risk: Authentication may store an API key in the local dLazy CLI configuration.

Mitigation: Use OS account protections for the config file and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown guidance with shell commands and JSON service responses; generated media can be saved as a local file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can return asynchronous task identifiers and hosted result URLs; saved files depend on the dLazy CLI invocation.]

## Skill Version(s):

1.3.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
