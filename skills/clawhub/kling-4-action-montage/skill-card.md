## Description:

Guides an agent through planning a fast action montage from three or four key frames, generating it with Kling 4 through VARG, and selecting usable clips.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT

## Use Case:

Developers and creators use this skill to plan and generate short action sequences such as dance, sports tricks, chases, or parkour from reference frames, then identify and cut the usable moments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images or video may contain material the user does not want to share with VARG and its generation provider.

Mitigation: Use only reference media you are comfortable sharing and authorized to submit.

Risk: Video generation can incur service costs.

Mitigation: Estimate costs and review the selected duration and resolution before submitting a generation request.

Risk: The workflow uses a VARG service key for authenticated API requests.

Mitigation: Configure the service key securely and avoid placing it in prompts or shared output.

Risk: The artifact review does not cover companion skills or the live MCP service.

Mitigation: Review those connected services and their guidance separately before relying on them.

## Reference(s):

- [Skill release page](https://clawhub.ai/vargai/skills/kling-4-action-montage)
- [VARG documentation](https://varg.ai/how-to)
- [VARG MCP connection](https://mcp.varg.ai/mcp)
- [Kling 4 film example](https://www.youtube.com/watch?v=WzXKggH-0Io)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration]

**Output Format:** [Markdown guidance with video-generation prompts, API request examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides instructions and commands for an external video-generation service; the generated video is produced by that service.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
