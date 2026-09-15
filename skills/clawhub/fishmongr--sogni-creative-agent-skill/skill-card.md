## Description:

Sogni Creative Agent Skill is an agent skill and CLI for image, video, music, speech, 3D reconstruction, media editing, hosted creative workflows, personas, and persistent creative memory using Sogni AI's decentralized GPU network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fishmongr](https://clawhub.ai/user/fishmongr)

### License/Terms of Use:

MIT

## Use Case:

Developers and external agent users use this skill to add Sogni-powered media generation, editing, upscaling, music, speech, 3D reconstruction, and workflow orchestration to agent runtimes. It supports direct CLI use, host launchers, OpenClaw metadata, and focused sub-skills for creative production tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Sogni API key and can send selected local media to Sogni or vendor-backed models.

Mitigation: Install only for users who accept that data flow, avoid hosted upload modes for private media, and review file references before generation.

Risk: The skill can store personas, voice clips, memories, preferences, and render metadata under the user's Sogni config directory.

Mitigation: Avoid storing sensitive persona or voice data unless needed, and review or purge the Sogni config directory during offboarding or uninstall.

Risk: The skill can steer agents toward self-update behavior and background update checks.

Mitigation: Use pinned package upgrades in automation-sensitive environments and review or disable self-update behavior before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/fishmongr/skills/sogni-creative-agent-skill)
- [Sogni AI Homepage](https://sogni.ai)
- [npm Package](https://www.npmjs.com/package/@sogni-ai/sogni-creative-agent-skill)
- [Hosted API Guide](references/hosted-api.md)
- [Model Catalog and Sizing Rules](references/models.md)
- [Video Prompting Guide](references/video-prompting.md)
- [Image Prompt Authoring Guide](references/image-prompting.md)
- [Personas, Memory and Personality](references/personas-memory.md)
- [Loop Maker Guide](references/loop-maker.md)
- [OpenClaw Configuration](references/openclaw-config.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and file-oriented output conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js, ffmpeg, and a Sogni API key for normal generation flows; generated media is directed to the user's working directory unless otherwise requested.]

## Skill Version(s):

3.50.0 (source: SKILL.md frontmatter, version.mjs, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
