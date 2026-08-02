## Description: <br>
Generates precise Python shell commands for Tencent Cloud VOD operations, including uploads, media processing, media queries, AIGC image/video/chat tasks, token management, semantic search, knowledge import, image processing, sub-application lookup, and task status checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tencent-mpaas-skills](https://clawhub.ai/user/tencent-mpaas-skills) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to translate Tencent Cloud VOD requests into executable command lines for the bundled scripts. It supports upload, media processing, task lookup, AIGC, search, knowledge import, and configuration workflows for Tencent Cloud VOD accounts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can generate commands that run paid Tencent Cloud VOD processing, AIGC, storage, or upload operations. <br>
Mitigation: Use dry-run previews where available, verify each generated command, and require explicit user confirmation before costly processing actions. <br>
Risk: The scripts require Tencent Cloud credentials and may load or store tokens in local dotenv files. <br>
Mitigation: Install and run the skill only where Tencent Cloud credentials and local plaintext dotenv storage are acceptable; protect or remove dotenv files when they contain secrets. <br>
Risk: The bundled scripts can install or upgrade Python packages before executing VOD workflows. <br>
Mitigation: Run in a controlled Python environment and review package installation behavior before enabling the scripts in production. <br>
Risk: Media URLs, prompts, and task data can be sent to Tencent Cloud VOD or persisted locally. <br>
Mitigation: Avoid sending sensitive media, prompts, or internal URLs, and remove local task data such as mem/elements.json when it contains private information. <br>


## Reference(s): <br>
- [ClawHub Tencent VOD skill page](https://clawhub.ai/tencent-mpaas-skills/skills/tencent-vod) <br>
- [Tencent Cloud VOD pricing](https://cloud.tencent.com/document/product/266/2838) <br>
- [Tencent Cloud VOD ApplyUpload API](https://cloud.tencent.com/document/api/266/31767) <br>
- [Tencent Cloud VOD CommitUpload API](https://cloud.tencent.com/document/api/266/31766) <br>
- [Tencent Cloud VOD PullUpload API](https://cloud.tencent.com/document/product/266/35575) <br>
- [Tencent Cloud VOD ProcessMedia API](https://cloud.tencent.com/document/product/266/33427) <br>
- [Tencent Cloud VOD DescribeMediaInfos API](https://cloud.tencent.com/document/product/266/31763) <br>
- [Tencent Cloud VOD SearchMedia API](https://cloud.tencent.com/document/product/266/31813) <br>
- [Tencent Cloud VOD SearchMediaBySemantics API](https://cloud.tencent.com/document/product/266/126287) <br>
- [Tencent Cloud VOD DescribeTaskDetail API](https://cloud.tencent.com/document/product/266/33431) <br>
- [Tencent Cloud VOD AIGC LLM Chat](https://cloud.tencent.com/document/product/266/126561) <br>
- [Tencent Cloud VOD AIGC token management](https://cloud.tencent.com/document/api/266/128054) <br>
- [Tencent Cloud VOD CreateAIGCTask Image](https://cloud.tencent.com/document/product/266/126240) <br>
- [Tencent Cloud VOD CreateAIGCTask Video](https://cloud.tencent.com/document/product/266/126239) <br>
- [Tencent Cloud VOD ProcessImageAsync API](https://cloud.tencent.com/document/api/266/127858) <br>
- [Tencent Cloud VOD CreateSceneAIGCImageTask API](https://cloud.tencent.com/document/api/266/126968) <br>
- [Tencent Cloud VOD CreateSceneAIGCVideoTask API](https://cloud.tencent.com/document/api/266/127542) <br>
- [Tencent Cloud VOD ImportMediaKnowledge API](https://cloud.tencent.com/document/product/266/126286) <br>
- [Tencent Cloud VOD CreateAIGCCustomElement API](https://cloud.tencent.com/document/api/266/129121) <br>
- [vod_upload detailed parameters](artifact/references/vod_upload.md) <br>
- [vod_pull_upload detailed parameters](artifact/references/vod_pull_upload.md) <br>
- [vod_process_media detailed parameters](artifact/references/vod_process_media.md) <br>
- [vod_describe_media detailed parameters](artifact/references/vod_describe_media.md) <br>
- [vod_search_media detailed parameters](artifact/references/vod_search_media.md) <br>
- [vod_search_media_by_semantics detailed parameters](artifact/references/vod_search_media_by_semantics.md) <br>
- [vod_describe_task detailed parameters](artifact/references/vod_describe_task.md) <br>
- [vod_aigc_chat detailed parameters](artifact/references/vod_aigc_chat.md) <br>
- [vod_aigc_token detailed parameters](artifact/references/vod_aigc_token.md) <br>
- [vod_aigc_image detailed parameters](artifact/references/vod_aigc_image.md) <br>
- [vod_aigc_video detailed parameters](artifact/references/vod_aigc_video.md) <br>
- [vod_process_image detailed parameters](artifact/references/vod_process_image.md) <br>
- [vod_scene_aigc_image detailed parameters](artifact/references/vod_scene_aigc_image.md) <br>
- [vod_create_scene_aigc_video_task detailed parameters](artifact/references/vod_create_scene_aigc_video_task.md) <br>
- [vod_import_media_knowledge detailed parameters](artifact/references/vod_import_media_knowledge.md) <br>
- [vod_describe_sub_app_ids detailed parameters](artifact/references/vod_describe_sub_app_ids.md) <br>
- [vod_create_aigc_advanced_custom_element detailed parameters](artifact/references/vod_create_aigc_advanced_custom_element.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, markdown, configuration, guidance] <br>
**Output Format:** [Markdown containing executable Python shell commands and Markdown links for returned media URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target bundled scripts under scripts/ and may include dry-run flags or confirmation guidance for costly processing actions.] <br>

## Skill Version(s): <br>
1.1.2 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
