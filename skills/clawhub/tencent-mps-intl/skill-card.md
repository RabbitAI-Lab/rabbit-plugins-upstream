## Description: <br>
Generates Python commands for Tencent Cloud MPS media processing, COS file operations, task queries, and AI image and video workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tencent-mpaas-skills](https://clawhub.ai/user/tencent-mpaas-skills) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and media operations teams use this skill to turn media-processing requests into Tencent Cloud MPS Python commands for transcoding, enhancement, subtitles, AI generation, task status queries, and COS transfer workflows. <br>

### Deployment Geography for Use: <br>
Global, subject to Tencent Cloud MPS endpoint and region availability. <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Tencent Cloud credentials and can upload, process, store, download, and share links to media through Tencent Cloud services. <br>
Mitigation: Use least-privilege temporary credentials, keep credentials in approved environment configuration, restrict COS permissions, and avoid sensitive media unless consent and retention controls are in place. <br>
Risk: Paid Tencent Cloud MPS operations can incur unintended costs or duplicate charges. <br>
Mitigation: Review the generated command before execution, prefer dry-run for uncertain or high-cost jobs, require explicit confirmation for processing tasks, and do not resubmit unfinished tasks without checking task status. <br>
Risk: The security evidence flags a deduplication or bypass-oriented feature as a misuse concern. <br>
Mitigation: Avoid deduplication or bypass workflows unless the use is legitimate, approved, and consistent with platform and customer requirements. <br>
Risk: Pre-signed links and COS URLs may expose processed media if shared too broadly. <br>
Mitigation: Limit link distribution, use short-lived links where possible, and remove or restrict objects after the intended workflow is complete. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tencent-mpaas-skills/skills/tencent-mps-intl) <br>
- [Tencent MPS best-practice scenarios](artifact/references/best_practices.md) <br>
- [Transcoding command reference](artifact/references/mps_transcode.md) <br>
- [Enhancement command reference](artifact/references/mps_enhance.md) <br>
- [Subtitle command reference](artifact/references/mps_subtitle.md) <br>
- [Image processing command reference](artifact/references/mps_imageprocess.md) <br>
- [AIGC image command reference](artifact/references/mps_aigc_image.md) <br>
- [AIGC video command reference](artifact/references/mps_aigc_video.md) <br>
- [COS operations command reference](artifact/references/mps_cos_ops.md) <br>
- [Task query command reference](artifact/references/mps_query_task.md) <br>
- [Tencent Cloud MPS pricing](https://cloud.tencent.com/document/product/862/36180) <br>
- [Tencent Cloud MPS request structure and regions](https://cloud.tencent.com/document/product/862/37572) <br>
- [Tencent Cloud ProcessMedia API](https://cloud.tencent.com/document/api/862/37578) <br>
- [Tencent Cloud ProcessImage API](https://cloud.tencent.com/document/api/862/112896) <br>
- [Tencent Cloud CreateAigcImageTask API](https://cloud.tencent.com/document/api/862/114562) <br>
- [Tencent Cloud CreateAigcVideoTask API](https://cloud.tencent.com/document/api/862/126965) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown text with python3 shell commands and Markdown links for returned result URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target scripts under scripts/ and may include dry-run, no-wait, task query, COS transfer, and environment-check options.] <br>

## Skill Version(s): <br>
1.2.6 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
