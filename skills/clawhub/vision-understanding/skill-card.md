## Description: <br>
Turns images, video, audio, and documents into grounded text outputs such as captions, tags, transcripts, summaries, OCR, visual Q&A, and structured extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route media-to-text requests to appropriate multimodal models, specify the desired text shape, and validate that results are grounded in the supplied media. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Media inputs may be uploaded to external multimodal model providers, exposing confidential screenshots, receipts, documents, audio, or video. <br>
Mitigation: Avoid sensitive media unless provider use is approved, and redact sensitive details before submission when possible. <br>
Risk: Generated captions, OCR, transcripts, summaries, or visual answers may be incomplete or include unsupported details. <br>
Mitigation: Check that the output matches the requested shape and is grounded in visible or audible content before relying on it. <br>


## Reference(s): <br>
- [Vision Understanding on ClawHub](https://clawhub.ai/runware/skills/vision-understanding) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance, configuration] <br>
**Output Format:** [Markdown guidance with optional JSON output specifications] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can include modality, model choice, delivery mode, and requested output shape.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
