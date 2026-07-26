## Description: <br>
Tencent VOD helps agents generate python3 shell commands for Tencent Cloud VOD uploads, media processing, search, AIGC tasks, token management, and task queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tencent-mpaas-skills](https://clawhub.ai/user/tencent-mpaas-skills) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to generate commands for Tencent Cloud VOD workflows such as upload, pull upload, transcoding, media search, task lookup, image/video AIGC, token management, and knowledge import. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated commands can trigger billable Tencent Cloud VOD processing, AIGC, storage, or token operations. <br>
Mitigation: Require explicit user confirmation for processing and token deletion commands, prefer --dry-run for uncertain or high-cost operations, and use budget alerts. <br>
Risk: Runtime scripts use Tencent Cloud credentials and can persist cloud tokens or task metadata locally. <br>
Mitigation: Use least-privilege credentials, avoid sensitive media, internal URLs, secrets, and personal data, and inspect ~/.env, project .env, and mem/elements.json. <br>
Risk: The skill can change the local Python environment through dependency installation or runtime package updates. <br>
Mitigation: Use a dedicated Python environment, preinstall dependencies yourself, and avoid allowing runtime scripts to auto-upgrade packages. <br>


## Reference(s): <br>
- [Tencent VOD ClawHub listing](https://clawhub.ai/tencent-mpaas-skills/skills/tencent-vod) <br>
- [Tencent Cloud VOD pricing](https://cloud.tencent.com/document/product/266/2838) <br>
- [VOD upload reference](references/vod_upload.md) <br>
- [VOD media processing reference](references/vod_process_media.md) <br>
- [VOD media search reference](references/vod_search_media.md) <br>
- [VOD semantic search reference](references/vod_search_media_by_semantics.md) <br>
- [VOD AIGC image reference](references/vod_aigc_image.md) <br>
- [VOD AIGC video reference](references/vod_aigc_video.md) <br>
- [VOD AIGC token reference](references/vod_aigc_token.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, markdown, guidance] <br>
**Output Format:** [Plain text commands with Markdown links and short confirmation prompts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target python3 scripts and may include --dry-run for previews or explicit confirmation for billable operations.] <br>

## Skill Version(s): <br>
1.1.1 (source: artifact frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
