## Description: <br>
Extract data from construction images using AI Vision. Analyze site photos, scanned documents, drawings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Construction teams, developers, and engineers use this skill to extract structured data from site photos, scanned documents, sketches, and construction drawings, including OCR text, tables, detected objects, progress indicators, safety observations, confidence scores, and warnings for ambiguous areas. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Construction images and extracted text may contain client, worker, site, or proprietary plan details and may be sent to a configured external vision or OCR provider. <br>
Mitigation: Use scoped API keys, redact sensitive image content or extracted text when required, and install only when the selected provider is acceptable for the data being analyzed. <br>
Risk: Image analysis may produce low-confidence, ambiguous, or approximate results for OCR, progress, object detection, and safety observations. <br>
Mitigation: Review confidence scores, warnings, and annotated descriptions before using extracted data for operational or safety decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/datadrivenconstruction/skills/image-to-data) <br>
- [DataDrivenConstruction website](https://datadrivenconstruction.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Structured text, tables, JSON, confidence scores, annotated descriptions, warnings, and Python code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use filesystem image inputs and network calls to configured AI Vision or OCR providers; image size limits depend on the provider.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata, artifact/claw.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
