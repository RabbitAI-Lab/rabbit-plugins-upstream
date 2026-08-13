## Description:

Generates Python commands for Tencent Cloud VOD uploads, media processing, media search, AIGC media generation, token and usage management, image processing, knowledge import, sub-application lookup, and task status queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencent-mpaas-skills](https://clawhub.ai/user/tencent-mpaas-skills)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use this skill to turn Tencent Cloud VOD tasks into concrete Python script commands for upload, processing, search, AIGC generation, media inspection, and task management workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can call billable Tencent Cloud VOD, media processing, and AIGC APIs.

Mitigation: Review generated commands before execution, use dry-run previews for uncertain or high-cost tasks, and configure billing alerts or spending limits.

Risk: The skill depends on Tencent Cloud credentials, AIGC tokens, and dotenv-based configuration.

Mitigation: Run in an isolated environment, keep dotenv files out of source control, and limit credential scope to the intended VOD account or sub-application.

Risk: Media URLs, prompts, and generated assets may be sent to cloud VOD and AIGC services.

Mitigation: Avoid submitting secrets, private URLs, personal data, or regulated media unless the use is approved for those cloud services.

Risk: The skill may install or rely on Python dependencies for Tencent Cloud API access.

Mitigation: Install dependencies in a virtual environment and review dependency installation output before running operational commands.

## Reference(s):

- [Tencent VOD skill page](https://clawhub.ai/tencent-mpaas-skills/skills/tencent-vod)
- [Tencent Cloud VOD pricing](https://cloud.tencent.com/document/product/266/2838)
- [Tencent Cloud VOD API reference](https://cloud.tencent.com/document/api/266/31767)
- [VOD upload reference](references/vod_upload.md)
- [VOD pull upload reference](references/vod_pull_upload.md)
- [VOD media processing reference](references/vod_process_media.md)
- [VOD media description reference](references/vod_describe_media.md)
- [VOD search reference](references/vod_search_media.md)
- [VOD AIGC image reference](references/vod_aigc_image.md)
- [VOD AIGC video reference](references/vod_aigc_video.md)
- [VOD AIGC audio reference](references/vod_aigc_audio.md)
- [VOD AIGC chat reference](references/vod_aigc_chat.md)
- [VOD task description reference](references/vod_describe_task.md)

## Skill Output:

**Output Type(s):** [Shell commands, Markdown, Guidance]

**Output Format:** [Plain text commands with Markdown links for returned URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands target python3 scripts in the skill package and may include dry-run flags or confirmation guidance for higher-cost processing.]

## Skill Version(s):

1.1.3 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
