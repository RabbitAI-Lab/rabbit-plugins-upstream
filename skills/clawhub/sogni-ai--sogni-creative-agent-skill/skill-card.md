## Description:

An agent skill and CLI for generating, editing, analyzing, and upscaling images, video, and music through Sogni AI, with saved personas and multi-step creative workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sogni-ai](https://clawhub.ai/user/sogni-ai)

### License/Terms of Use:

MIT

## Use Case:

Creators and developers use it to direct an AI agent to make or edit images, videos, and music, analyze media, and assemble multi-step creative projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review cites model-routing guidance that may bypass safety refusals.

Mitigation: Keep the content filter enabled unless the user explicitly requests a change; do not retry a rejected request with filtering disabled as an automatic workaround.

Risk: Prompts and personal media may be sent to remote services for processing.

Mitigation: Explain what will be sent before hosted processing, and use direct CLI mode for media that must remain on the device.

Risk: Install or launch commands may use mutable package versions.

Mitigation: Review installation commands and prefer a reviewed, version-pinned release over a mutable latest tag.

Risk: The security review reports gaps in endpoint and replay-data safeguards, and some content was only partially analyzed.

Mitigation: Avoid sending sensitive media through hosted workflows until endpoint handling and replay-data retention are understood.

## Reference(s):

- [Image prompting guide](artifact/references/image-prompting.md)
- [Video prompting guide](artifact/references/video-prompting.md)
- [Model guide](artifact/references/models.md)
- [Hosted API guide](artifact/references/hosted-api.md)
- [Long jobs and queues guide](artifact/references/long-jobs-and-queues.md)
- [Persona and memory guide](artifact/references/personas-memory.md)

## Skill Output:

**Output Type(s):** [Files, Analysis, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Generated image, video, and audio files, with text, Markdown, JSON, and shell commands as needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated or edited media and multi-step workflow results.]

## Skill Version(s):

3.73.6 (source: CHANGELOG.md, server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
