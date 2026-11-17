## Description:

Provides an agent skill and CLI for generating, editing, upscaling, and orchestrating image, video, and music workflows on Sogni AI's decentralized GPU network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[krunkosaurus](https://clawhub.ai/user/krunkosaurus)

### License/Terms of Use:

MIT

## Use Case:

Developers, agent operators, and creative users use this skill to give an agent concrete workflows for image generation and editing, video generation and editing, music generation, media upscaling, personas, saved preferences, and hosted Sogni creative workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent personas, memories, personality text, and voice clips may retain sensitive information and can be reused in later hosted chat or tool workflows.

Mitigation: Avoid storing secrets in saved state, review or clear personas and voice clips when they are no longer needed, and use direct CLI mode for media that must remain local.

Risk: Hosted workflows may send prompts, media, or references to Sogni services for generation and durable execution.

Mitigation: Install and use the skill only when the operator trusts Sogni AI with the submitted prompts and media, and avoid hosted modes for private local-only assets.

Risk: Self-update and @latest install flows can run newly published package code.

Mitigation: Approve updates only after deciding that the newly published package is acceptable for the environment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/krunkosaurus/skills/sogni-creative-agent-skill)
- [Sogni AI homepage](https://sogni.ai)
- [README](README.md)
- [Hosted API guide](references/hosted-api.md)
- [Model reference](references/models.md)
- [Image prompting guide](references/image-prompting.md)
- [Video prompting guide](references/video-prompting.md)
- [Personas and memory guide](references/personas-memory.md)
- [OpenClaw configuration guide](references/openclaw-config.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, configuration snippets, and generated media file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent to invoke Sogni CLI or hosted API workflows and to save generated media in the user's working directory unless the user requests another destination.]

## Skill Version(s):

3.42.0 (source: frontmatter metadata, release evidence, changelog, version.mjs)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
