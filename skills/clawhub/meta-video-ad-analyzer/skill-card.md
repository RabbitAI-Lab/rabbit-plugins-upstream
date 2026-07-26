## Description: <br>
Extract and analyze content from video ads using Gemini Vision AI, including frame extraction, OCR text detection, audio transcription, and scene-by-scene analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fortytwode](https://clawhub.ai/user/fortytwode) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and marketing analysts use this skill to extract timelines, text overlays, transcripts, thumbnails, and scene descriptions from video ads or static creative assets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ad videos, images, audio, and extracted content may be processed by Google cloud AI services. <br>
Mitigation: Use only approved media, configure a dedicated least-privilege Google service account, and avoid confidential or regulated content unless organizational policy permits cloud processing. <br>
Risk: Generated thumbnails may be written under static/thumbnails and could expose sensitive creative assets if served publicly or retained too long. <br>
Mitigation: Restrict access to generated thumbnail directories and apply retention or cleanup controls appropriate for the analyzed media. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fortytwode/skills/meta-video-ad-analyzer) <br>
- [Publisher profile](https://clawhub.ai/user/fortytwode) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python examples and structured extraction objects] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces extracted scene timelines, text timelines, transcript text, thumbnail paths, and setup guidance for Google cloud AI services.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
