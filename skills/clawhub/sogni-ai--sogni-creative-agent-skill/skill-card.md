## Description:

A CLI and agent skill for creating and editing images, videos, and music with Sogni AI, including personal LoRAs and multi-step creative workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sogni-ai](https://clawhub.ai/user/sogni-ai)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use the skill through an AI agent or CLI to create, edit, upscale, and analyze visual or audio media, and to coordinate durable creative workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, audio, or other media may be sent to remote services for processing, and the privacy disclosures are reported as unclear.

Mitigation: Review the service's current privacy terms and avoid sending sensitive or personal media unless its handling is acceptable.

Risk: Model-routing guidance may bypass safeguards.

Mitigation: Review the selected model and filtering behavior before generation, and keep safeguards enabled unless a change is deliberate and permitted.

Risk: Some installer references may use mutable versions.

Mitigation: Install a verified, pinned release and confirm the package source and version.

## Reference(s):

- [Image prompting guide](references/image-prompting.md)
- [Video prompting guide](references/video-prompting.md)
- [Model reference](references/models.md)
- [Hosted API modes](references/hosted-api.md)
- [Video editing guide](references/video-editing.md)
- [Sogni hosted MCP documentation](https://docs.sogni.ai/agents/mcp/)

## Skill Output:

**Output Type(s):** [Image, video, and audio files, Text, JSON]

**Output Format:** [Generated media files or result URLs, with optional machine-readable JSON status and text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media can be saved locally or returned as result URLs; JSON mode provides structured status and result details.]

## Skill Version(s):

3.72.1 (source: frontmatter, changelog released 2026-11-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
