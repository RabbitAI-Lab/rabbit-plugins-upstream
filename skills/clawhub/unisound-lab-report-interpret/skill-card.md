## Description: <br>
Assists with interpreting basic lab and examination report text by identifying abnormal findings, explaining clinical significance, and producing follow-up suggestions as JSON plus a natural-language summary. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Community clinic and primary-care clinicians use this skill to turn blood test, chemistry, urinalysis, coagulation, thyroid, ECG, and similar report text into structured abnormality review, clinical significance notes, urgency flags, and follow-up suggestions. The output is assistive and does not replace clinician judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive medical report text may be sent to a remote LLM endpoint. <br>
Mitigation: Use the skill only with an endpoint approved for the applicable medical data and avoid including patient names or identifiers. <br>
Risk: The artifact states that reports are de-identified before sending, while the security guidance says not to rely on that promise unless implementation changes actually redact the report. <br>
Mitigation: Confirm or add real redaction before processing patient reports. <br>
Risk: Clinical interpretation output may be incomplete, incorrect, or unsuitable for an individual patient. <br>
Mitigation: Treat output as assistive review for licensed clinicians and keep final diagnosis and treatment decisions with qualified medical staff. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-lab-report-interpret) <br>
- [Default medical LLM API endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, JSON, Markdown, Files, Guidance] <br>
**Output Format:** [JSON followed by a natural-language summary, printed to stdout or written to an output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes abnormal item details, clinical significance, urgency, follow-up suggestions, and an urgent_attention_needed flag.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
