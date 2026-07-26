## Description: <br>
ClawAgent helps agents create marketing images and videos, manage AIGC production workflows, upload required assets, and publish approved image or video content to supported social platforms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiadouai](https://clawhub.ai/user/jiadouai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing operators, creators, and agents use ClawAgent to generate product visuals, short videos, lip-sync videos, posters, and social posts, then route approved content through authorized publishing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow can install global npm tooling and store a mcporter token in the user's home-scoped configuration. <br>
Mitigation: Use an isolated or low-privilege environment and a temporary or least-privilege token; confirm that home-scoped token storage is acceptable before installation. <br>
Risk: The upload flow can send local media to remote cloud storage. <br>
Mitigation: Do not upload sensitive, private, or rights-restricted files; confirm the file path, content, and user's permission before upload. <br>
Risk: Publishing tools can post image or video content to authorized social media accounts. <br>
Mitigation: Require explicit manual confirmation of the selected account, platform, title, media, and publish time before every publish action. <br>
Risk: The skill communicates with a third-party service and may report unsupported capability requests with user consent. <br>
Mitigation: Disclose the remote service interaction, send only the minimum necessary information, and obtain explicit user consent before unsupported-capability reporting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jiadouai/skills/clawagent) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/jiadouai) <br>
- [ClawAgent usage guide](artifact/SKILL.md) <br>
- [Authentication and authorization](artifact/references/auth.md) <br>
- [Common interfaces and workflows](artifact/references/workflows.md) <br>
- [Video publishing](artifact/references/video_publish.md) <br>
- [Image publishing](artifact/references/image_publish.md) <br>
- [Unsupported capability reporting](artifact/references/unsupported_feature_reporting.md) <br>
- [Product scene image generation](artifact/references/business_product_scene.md) <br>
- [Product poster generation](artifact/references/business_poster.md) <br>
- [Model try-on](artifact/references/model_try_clothes.md) <br>
- [Shoe try-on](artifact/references/shoes_dressing.md) <br>
- [Model generation](artifact/references/model_produce.md) <br>
- [Xiaohongshu note images](artifact/references/ice_design_image_xhs.md) <br>
- [Lip-sync video](artifact/references/ice_voice_video.md) <br>
- [Singing image video](artifact/references/image_song.md) <br>
- [Mixed-cut video](artifact/references/ai_mixed_script.md) <br>
- [Video clone](artifact/references/ai_clone_video.md) <br>
- [Video analysis](artifact/references/analyze_video.md) <br>
- [Douyin link parsing](artifact/references/get_raw_url.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON arguments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide authenticated MCP tool calls that return job IDs, media URLs, task status, account lists, or error messages.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release metadata; artifact frontmatter says 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
