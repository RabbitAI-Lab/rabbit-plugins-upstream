## Description:

An agent CLI skill for creating, editing, and upscaling images, videos, and music through Sogni AI, with support for personas and multi-step creative workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sogni-ai](https://clawhub.ai/user/sogni-ai)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use the skill to direct a compatible agent to create or edit images, videos, and music, manage personas, and run multi-step media workflows through Sogni.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hosted chat and workflow modes may upload local reference media to Sogni storage, including sensitive photos, recordings, or likenesses.

Mitigation: Use direct CLI mode for media that must stay local, and confirm sharing and consent before sending reference media.

Risk: Installation guidance and package dependencies can change between releases.

Mitigation: Review the install source and version before running setup commands.

Risk: Image, video, and music generation can consume paid credits, and priority options can change the cost.

Mitigation: Review the quoted estimate and billing options before starting a generation; use priority only after the user opts in.

## Reference(s):

- [Sogni AI](https://sogni.ai)
- [Sogni MCP connection guide](https://docs.sogni.ai/agents/mcp/)
- [Sogni pricing and Spark Packs](https://docs.sogni.ai/pricing/#spark-packs)
- [Hosted API guide](references/hosted-api.md)
- [Image prompting guide](references/image-prompting.md)
- [Video prompting guide](references/video-prompting.md)
- [Model guide](references/models.md)
- [Long jobs and queues guide](references/long-jobs-and-queues.md)

## Skill Output:

**Output Type(s):** [Image files, Video files, Audio files, 3D model files, Text guidance, Shell commands, Configuration]

**Output Format:** [Generated media files with Markdown guidance, command examples, and configuration instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated results depend on the selected model and service availability.]

## Skill Version(s):

3.70.0 (source: frontmatter, changelog, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
