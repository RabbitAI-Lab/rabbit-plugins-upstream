## Description: <br>
Generates Python shell commands for Tencent Cloud VOD upload, query, media processing, AIGC, search, image processing, task, and sub-application workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tencent-mpaas-skills](https://clawhub.ai/user/tencent-mpaas-skills) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to turn Tencent Cloud VOD requests into executable Python commands for uploads, media queries, transcoding, enhancement, AIGC generation, semantic search, and task management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill works with Tencent Cloud credentials and paid VOD or AIGC APIs. <br>
Mitigation: Review generated commands before execution, require confirmation for processing tasks, and prefer --dry-run for costly or uncertain operations. <br>
Risk: Running scripts may change the Python environment by upgrading packages. <br>
Mitigation: Run the skill in an isolated environment and review dependency changes before applying upgrades. <br>
Risk: Tokens, task metadata, prompts, URLs, or media-related context may be stored locally or sent to Tencent Cloud services. <br>
Mitigation: Avoid placing secrets or personal data in prompts, URLs, or session context, and review local plaintext files created by the scripts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tencent-mpaas-skills/skills/tencent-vod-intl) <br>
- [Tencent Cloud VOD Pricing](https://cloud.tencent.com/document/product/266/2838) <br>
- [Tencent Cloud Billing Budget Center](https://console.cloud.tencent.com/expense/budget) <br>
- [VOD Upload Documentation](https://cloud.tencent.com/document/api/266/31766) <br>
- [VOD Pull Upload Documentation](https://cloud.tencent.com/document/api/266/35575) <br>
- [DescribeMediaInfos Documentation](https://cloud.tencent.com/document/product/266/31763) <br>
- [ProcessMedia Documentation](https://cloud.tencent.com/document/product/266/33427) <br>
- [Create AIGC Image Task Documentation](https://cloud.tencent.com/document/api/266/126240) <br>
- [Create AIGC Video Task Documentation](https://cloud.tencent.com/document/api/266/126239) <br>
- [AIGC Token Management Documentation](https://cloud.tencent.com/document/api/266/128054) <br>
- [Semantic Search Documentation](https://cloud.tencent.com/document/product/266/126287) <br>
- [vod_upload.md](references/vod_upload.md) <br>
- [vod_process_media.md](references/vod_process_media.md) <br>
- [vod_aigc_image.md](references/vod_aigc_image.md) <br>
- [vod_aigc_video.md](references/vod_aigc_video.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Markdown, Configuration guidance] <br>
**Output Format:** [Plain text commands with Markdown hyperlinks for generated links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands use python3 scripts/<script-name>.py and may include dry-run or confirmation guidance before paid processing tasks.] <br>

## Skill Version(s): <br>
1.1.1 (source: frontmatter and ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
