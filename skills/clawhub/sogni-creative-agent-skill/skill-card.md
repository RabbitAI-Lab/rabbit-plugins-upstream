## Description:

Sogni Creative Agent Skill lets agents generate and edit images, videos, and music through the Sogni AI CLI and hosted workflows, with support for personas, memories, model selection, loop reels, and multi-step creative workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[krunkosaurus](https://clawhub.ai/user/krunkosaurus)

### License/Terms of Use:

MIT

## Use Case:

Developers, creators, and agent operators use this skill to add Sogni-powered media generation to agent workflows, including prompt-to-image, image and video editing, music generation, persona-based creation, and durable multi-step creative jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Sogni API key and hosted or vendor modes may upload referenced media to Sogni-hosted services.

Mitigation: Protect the API key, avoid hosted modes for private media, and use direct CLI mode when local media must not leave the machine.

Risk: The skill can reuse persistent personas, memories, and personality settings stored locally.

Mitigation: Review, disable, or clear saved personas and memories before use on shared machines or sensitive workflows.

Risk: The skill exposes global install and self-update flows that can modify the CLI installation.

Mitigation: Treat self-update, sudo, and administrator prompts as manual maintenance decisions rather than part of a normal creative task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/krunkosaurus/skills/sogni-creative-agent-skill)
- [Sogni homepage](https://sogni.ai)
- [Hosted Sogni Intelligence API Modes](references/hosted-api.md)
- [Model Catalog & Sizing Rules](references/models.md)
- [Loop Maker: Image Folder to Seamless Music-Backed Video](references/loop-maker.md)
- [Personas, Memory & Personality](references/personas-memory.md)
- [Video Prompting Guide](references/video-prompting.md)
- [Video Editing & Stitching](references/video-editing.md)
- [OpenClaw Plugin Configuration](references/openclaw-config.md)
- [Sogni Skills per-skill index](skills/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON-capable CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local image, video, and audio files through the Sogni CLI; hosted modes may return URLs and JSON status.]

## Skill Version(s):

3.26.1 (source: server release metadata, SKILL.md metadata, and CHANGELOG, released 2026-08-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
