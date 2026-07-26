## Description: <br>
Parses scanned PDFs, images, OFD files, receipts, contracts, court documents, and other files into text or Markdown, using native parsing first and Delilegal OCR only as a fallback or when explicitly requested. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolalam](https://clawhub.ai/user/coolalam) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, legal operators, and other document-processing users use this skill to turn files that an agent cannot directly read into usable Markdown or text. It is suited for scanned legal documents, receipts, images, OFD files, and PDFs where native parsing is unavailable, empty, garbled, or incomplete. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive documents may be sent to Delilegal OCR when native parsing is insufficient. <br>
Mitigation: Use native parsing first, call OCR only after user approval or clear need, and treat the CLI API key in ~/.deli/cli/config.json as sensitive. <br>
Risk: OCR output can misread high-impact fields such as amounts, dates, names, case numbers, invoice numbers, bank accounts, seals, signatures, or handwriting. <br>
Mitigation: Flag uncertain fields and require human review before relying on OCR results for legal, financial, or evidentiary decisions. <br>
Risk: The external CLI may be unavailable, unauthenticated, or return no usable command for the requested file type. <br>
Mitigation: Run the documented CLI check and command discovery steps, preserve original files, and report command or format limitations instead of attempting unsupported fallback calls. <br>


## Reference(s): <br>
- [deli-cli 通用前置](references/cli-common.md) <br>
- [OCR 文件解析 CLI 场景指南](references/ocr-cli-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown or plain text files with concise Markdown status guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports the source filename, output path, raw-response retention status, parsing completeness, and fields that need human review.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact metadata lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
