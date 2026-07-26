## Description: <br>
Provides MediaKit CLI guidance for video enhancement, video understanding, subtitle removal, scene segmentation, OCR, ASR subtitles, matting, metadata probing, and highlight generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[volcvnebot](https://clawhub.ai/user/volcvnebot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and media engineers use this skill to select and invoke MediaKit CLI video tools for workflows such as enhancement, storyline and highlight analysis, subtitle/OCR extraction, matting, scene segmentation, and metadata probing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted media and API credentials should be treated as exposed to the external MediaKit CLI and cloud service. <br>
Mitigation: Install and use this skill only when the operator trusts that CLI and service, and process confidential, regulated, internal-only, or personally sensitive audio/video only when authorized to send it there. <br>
Risk: Video URLs, callback_args, and client_token values can accidentally carry secrets or durable access to private media. <br>
Mitigation: Prefer time-limited URLs and avoid placing secrets in video URLs, callback_args, or client_token values. <br>
Risk: Video analysis, enhancement, subtitle removal, OCR, and generated highlight outputs may be inaccurate or unsuitable for downstream use without review. <br>
Mitigation: Review MediaKit results before publication, editing decisions, compliance use, or automated downstream processing. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/volcvnebot/skills/byted-mediakit-video) <br>
- [MediaKit shared rules](reference/shared.md) <br>
- [Analyze video highlights](reference/analyze-video-highlights.md) <br>
- [Analyze video storyline](reference/analyze-video-storyline.md) <br>
- [ASR subtitles](reference/asr-subtitles.md) <br>
- [Enhance video](reference/enhance-video.md) <br>
- [Enhance video generative](reference/enhance-video-generative.md) <br>
- [Erase video subtitle](reference/erase-video-subtitle.md) <br>
- [Erase video subtitle pro](reference/erase-video-subtitle-pro.md) <br>
- [Generate highlights microdrama](reference/generate-highlights-microdrama.md) <br>
- [Generate highlights minigame](reference/generate-highlights-minigame.md) <br>
- [Matte greenscreen video](reference/matte-greenscreen-video.md) <br>
- [Matte portrait video](reference/matte-portrait-video.md) <br>
- [Probe video metadata](reference/probe-video-metadata.md) <br>
- [Segment scenes](reference/segment-scenes.md) <br>
- [Video OCR](reference/video-ocr.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with MediaKit CLI command examples and JSON request/result shapes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires mediakit-cli; most video tools submit asynchronous jobs that return task_id and request_id for later query-task retrieval.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
