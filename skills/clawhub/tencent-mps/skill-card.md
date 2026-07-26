## Description: <br>
Tencent MPS helps agents choose and generate Python commands for Tencent Cloud Media Processing, COS file operations, task queries, usage checks, and media comparison workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ollielin](https://clawhub.ai/user/ollielin) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and media operators use this skill to prepare Tencent Cloud MPS and COS command-line workflows for video transcoding, enhancement, subtitles, audio processing, image generation and editing, content understanding, quality checks, usage reporting, and task follow-up. It is intended for users who already have Tencent Cloud credentials and appropriate rights to process the media they submit. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run Tencent Cloud MPS and COS commands with user credentials and upload local media to cloud storage. <br>
Mitigation: Use least-privilege Tencent Cloud credentials, private buckets, explicit local paths and output directories, and avoid passing secrets on the command line. <br>
Risk: Pre-signed URLs and COS result links may grant temporary access to processed media. <br>
Mitigation: Treat generated links as temporary access tokens and share them only with intended recipients. <br>
Risk: Dedupe, face-swap, voice-clone, and watermark-removal workflows can affect consent, rights, or impersonation-sensitive use cases. <br>
Mitigation: Use those workflows only when the operator has clear rights and consent for the input media and requested transformation. <br>
Risk: Cloud media-processing tasks may create costs or repeated processing side effects. <br>
Mitigation: Use dry-run previews, review the proposed command before execution, and avoid retrying failed tasks until task status and billing impact are understood. <br>


## Reference(s): <br>
- [Tencent MPS Skill Page](https://clawhub.ai/ollielin/skills/tencent-mps) <br>
- [MPS best-practice scenarios](references/best_practices.md) <br>
- [Tencent Cloud MPS pricing](https://cloud.tencent.com/document/product/862/36180) <br>
- [Tencent Cloud MPS request regions](https://cloud.tencent.com/document/product/862/37572) <br>
- [Transcoding parameters and examples](references/mps_transcode.md) <br>
- [Video enhancement parameters and examples](references/mps_enhance.md) <br>
- [Subtitle and speech-recognition parameters and examples](references/mps_subtitle.md) <br>
- [Image processing parameters and examples](references/mps_imageprocess.md) <br>
- [AIGC image generation parameters and examples](references/mps_aigc_image.md) <br>
- [AIGC video generation parameters and examples](references/mps_aigc_video.md) <br>
- [COS file operation parameters and examples](references/mps_cos_ops.md) <br>
- [Task query parameters and examples](references/mps_query_task.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Markdown, Guidance] <br>
**Output Format:** [Markdown containing Python command lines, confirmation prompts, task IDs, and result links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target scripts in the skill's scripts/ directory and may produce Tencent Cloud task IDs, COS URLs, pre-signed download links, or local comparison files.] <br>

## Skill Version(s): <br>
1.2.8 (source: ClawHub release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
