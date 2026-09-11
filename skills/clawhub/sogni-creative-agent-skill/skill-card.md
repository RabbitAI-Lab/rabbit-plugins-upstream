## Description:

Sogni Creative Agent Skill gives agents a CLI and hosted workflow surface for generating, editing, upscaling, and composing images, video, and music through Sogni AI's decentralized GPU network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[krunkosaurus](https://clawhub.ai/user/krunkosaurus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative operators, and agent users use this skill to route media-generation requests into Sogni image, video, music, upscaling, persona, and durable workflow commands. It is intended for agent-assisted creative production where the agent plans the prompt, model choice, file handling, and command invocation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install and update path can execute mutable npm package code.

Mitigation: Use pinned package versions, review updates before adoption, and avoid unversioned npx or @latest installs in controlled environments.

Risk: Hosted modes may upload selected local media to Sogni infrastructure.

Mitigation: Use direct local CLI modes for private media that must not leave the machine, and reserve hosted chat or durable workflows for media that may be uploaded.

Risk: The skill stores persistent Sogni credentials, app IDs, memories, personas, and render state under local configuration paths.

Mitigation: Protect the local Sogni configuration directory, use least-privilege API keys where available, and purge or back up local state deliberately during deprovisioning.

Risk: The server security verdict requires review before deployment.

Mitigation: Run organizational security review and scanner validation before enabling the skill in a shared or production agent environment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/krunkosaurus/skills/sogni-creative-agent-skill)
- [Sogni homepage](https://sogni.ai)
- [Sogni Creative Agent README](README.md)
- [Hosted API Modes](references/hosted-api.md)
- [Model Catalog and Sizing Rules](references/models.md)
- [OpenClaw Configuration](references/openclaw-config.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, CLI commands, JSON workflow plans, configuration snippets, and generated media file paths or result records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js, a Sogni API key, and ffmpeg for some local video and audio utilities; hosted modes may upload selected local media to Sogni infrastructure.]

## Skill Version(s):

3.42.0 (source: server release, SKILL.md metadata, version.mjs, CHANGELOG; server release created 2026-09-11T05:39:30Z)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
