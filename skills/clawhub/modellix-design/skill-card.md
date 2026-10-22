## Description:

Integrates Modellix's unified API into agent workflows for generating and editing images, video, and audio, including speech synthesis and transcription.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modellix](https://clawhub.ai/user/modellix)

### License/Terms of Use:

MIT

## Use Case:

Developers and other users can use the skill to request AI image, video, and audio generation or editing through Modellix. It also supports related speech and transcription workflows and returns task status and media resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Routine CLI checks may replace a shared CLI, and a failed update can require manual repair.

Mitigation: Set MODELLIX_CLI_AUTO_UPDATE=0 and install a reviewed CLI version separately, or use the connected MCP or direct REST path.

Risk: Generation is paid, and prompts and media are submitted to an external service.

Mitigation: Review model pricing before submission and avoid sending prompts or media that should remain private.

Risk: Profile-clearing examples can remove saved authentication settings.

Mitigation: Run profile-clearing commands only when you intend to remove that profile.

## Reference(s):

- [Modellix Design on ClawHub](https://clawhub.ai/modellix/skills/modellix-design)
- [Modellix Getting Started](https://docs.modellix.ai/get-started.md)
- [Modellix API Guide](https://docs.modellix.ai/ways-to-use/api.md)
- [Modellix MCP Documentation](https://docs.modellix.ai/mcp)
- [modellix-cli on npm](https://www.npmjs.com/package/modellix-cli)

## Skill Output:

**Output Type(s):** [Images, Video, Audio, Files, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Media resources and task-result JSON, with Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media outputs may be returned as resource URLs or downloaded files; available formats depend on the selected model.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
