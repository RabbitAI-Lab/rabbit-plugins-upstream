## Description: <br>
Uses the poocr library with Tencent Cloud OCR to recognize VAT invoices and export extracted invoice data to Excel. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Finance, tax, audit, and operations users can use this skill to prepare agent workflows that process single invoices or reviewed folders of invoices and export key fields to Excel. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Invoices can contain tax, payment, address, and business information that may be sent to Tencent Cloud OCR. <br>
Mitigation: Confirm that the invoices are approved for Tencent Cloud processing before running the workflow. <br>
Risk: Tencent Cloud SecretId/SecretKey values and generated Excel files can expose sensitive access or invoice data if mishandled. <br>
Mitigation: Store credentials securely, avoid embedding real keys in shared code, and protect generated Excel files according to data-handling policy. <br>
Risk: Batch folder processing can submit unintended invoice files or files that have not been reviewed. <br>
Mitigation: Review the input folder contents before batch processing and limit runs to intended invoice files. <br>
Risk: OCR accuracy depends on invoice image or PDF quality, which can produce incorrect extracted fields. <br>
Mitigation: Review the exported Excel results before using them for reimbursement, tax, audit, or reporting decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/poocr-vatinvoice2excel) <br>
- [Tencent Cloud API key console](https://curl.qcloud.com/9ExTmaya) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with bash commands, Python examples, and parameter tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The example workflow writes Excel files to the configured output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
