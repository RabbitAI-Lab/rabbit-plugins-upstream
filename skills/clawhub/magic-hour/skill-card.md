## Description:

Generate AI video and images with the Magic Hour API across text-to-video, image-to-video, and image generation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rhythmp28](https://clawhub.ai/user/rhythmp28)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to generate videos and images through Magic Hour, poll asynchronous jobs, and retrieve generated media URLs or downloaded files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation prompts, selected input images, and job parameters are sent to Magic Hour's hosted service.

Mitigation: Avoid sensitive inputs unless the user accepts that hosted processing, and follow the user's data handling requirements.

Risk: The MAGIC_HOUR_API_KEY credential is required for local script and MCP use.

Mitigation: Keep the API key in the environment, do not paste it into prompts or logs, and rotate it if exposure is suspected.

Risk: Generated media can be downloaded to local storage.

Mitigation: Use --download-dir only for an intended output directory and manage saved media according to the user's retention needs.

Risk: Paid or long-duration models may consume significant Magic Hour credits.

Mitigation: Check estimated credits before using paid models or longer generations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rhythmp28/skills/magic-hour)
- [Magic Hour raw HTTP reference](artifact/references/api.md)
- [Magic Hour model catalogue](artifact/references/models.md)
- [Magic Hour documentation](https://docs.magichour.ai)
- [Magic Hour hosted MCP](https://magichour.ai/mcp)
- [Magic Hour developer API key](https://magichour.ai/developer)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, files]

**Output Format:** [Markdown guidance with shell commands; helper scripts emit JSON containing project status, media URLs, credits charged, and optional downloaded file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MAGIC_HOUR_API_KEY and python3; generated media can be saved locally when a download directory is provided.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
