## Description: <br>
Supports clinical-trial data statistics for pharmaceutical drug development by computing descriptive statistics and group comparisons, then generating a medical-model-assisted Markdown interpretation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and clinical data analysts use this skill to parse clinical-trial records from JSON or supported document and table formats, compute endpoint descriptive statistics by group, and produce an AI-assisted interpretation for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Clinical-trial statistics and study metadata are sent to the documented hivoice.cn medical model endpoint for interpretation. <br>
Mitigation: Use only when organizational policy permits that endpoint, and de-identify trial data before processing. <br>
Risk: Legacy documents, PDFs, and images may require conversion or OCR before parsing. <br>
Mitigation: Prefer JSON, CSV, or XLSX inputs when possible; run conversion of untrusted files in a sandbox. <br>
Risk: AI-assisted interpretations may be incomplete or unsuitable for formal clinical or regulatory decisions. <br>
Mitigation: Have qualified statisticians or clinical reviewers verify outputs before using them in study analysis, submissions, or decision-making. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-clinical-trial-statistics) <br>
- [Statistical Analysis reference skill](https://agent-skills.md/skills/Jst-Well-Dan/Skill-Box/statistical-analysis) <br>
- [Hivoice medical model API endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Markdown, Analysis] <br>
**Output Format:** [UTF-8 JSON containing structured clinical-trial statistics and Markdown interpretation text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an appkey for the documented hivoice.cn medical model API; optional prepared JSON can be saved for review.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
