## Description: <br>
Provides postoperative rehabilitation exercise guidance for patients, using CareKit's instruction task view as a reference for structured action guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and care teams use this skill to turn existing postoperative rehabilitation exercise entries into structured instructions, frequency and duration details, precautions, and Markdown guidance. It is informational and does not replace clinician assessment or patient-specific rehabilitation decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Rehabilitation exercise details are sent to a remote medical-model endpoint. <br>
Mitigation: Install only if this remote processing is acceptable, avoid patient-identifying data unless approved, and disclose the data flow to users. <br>
Risk: Generated exercise guidance could be mistaken for patient-specific clinical advice. <br>
Mitigation: Treat outputs as informational and require clinical review before applying them to individual rehabilitation decisions. <br>
Risk: Broad document conversion and OCR support may process unexpected or sensitive file contents. <br>
Mitigation: Limit inputs to intended rehabilitation exercise files and review extracted content before submitting it for inference. <br>


## Reference(s): <br>
- [CareKit](https://github.com/carekit-apple/CareKit) <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-exercise-guidance) <br>
- [Remote medical-model endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Markdown, Guidance] <br>
**Output Format:** [UTF-8 JSON containing structured fields and Markdown guidance text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an appkey and can preprocess JSON, text, tables, documents, PDFs, and images before generating guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact _meta.json reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
