## Description: <br>
Reviews medical-claims case text to assess the relationship between other diagnoses and the primary diagnosis, then returns a reimbursement recommendation in the requested format. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Claims reviewers and insurance operations teams use this skill as an assistive review step for medical-claims materials or OCR text after personal identifiers have been redacted. It does not replace policy terms, legal review, or final human claim decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends user-provided medical or claims text to the configured model service. <br>
Mitigation: Use it only in workflows approved for that service and redact names, identifiers, account numbers, and other personal data before submitting a case. <br>
Risk: Normal JSON output includes the question text, and optional file output can store sensitive case material. <br>
Mitigation: Treat stdout and result files as sensitive, and use --output only in locations approved for medical or claims data. <br>
Risk: The generated review is an assistive claims assessment and may be incomplete or incorrect. <br>
Mitigation: Have qualified reviewers check the answer against policy terms, source materials, and applicable review procedures before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-pre-existing-review) <br>
- [Configured model API endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, files] <br>
**Output Format:** [JSON object by default; plain text with --text-only; NDJSON for batch output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes question text and metadata in JSON output; writes UTF-8 result files only when --output is provided.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
