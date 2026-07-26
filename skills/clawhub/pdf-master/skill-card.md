## Description: <br>
PDF万能大师 helps agents inspect, convert, OCR, edit, secure, compress, extract, review, and batch-process PDF documents with scripted workflows plus quality and safety checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ford828](https://clawhub.ai/user/ford828) <br>

### License/Terms of Use: <br>
MIT No Attribution (MIT-0) <br>


## Use Case: <br>
Employees, external users, and developers use this skill to process uploaded PDFs into edited PDFs, Office files, spreadsheets, reports, summaries, redaction outputs, and batch-processing deliverables while preserving quality checks and confirmation gates for high-risk actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may handle confidential or sensitive PDF content. <br>
Mitigation: Use local-only handling for confidential files, avoid cloud routing when sensitivity is declared or detected, and clean temporary files after task completion. <br>
Risk: Direct edits, bulk replacement, signing, and permanent redaction can materially change documents. <br>
Mitigation: Require previews and explicit confirmation before high-risk actions, keep backups where appropriate, and provide verification reports for redaction workflows. <br>
Risk: Optional external services for Feishu, invoice verification, translation, or signing may be unavailable or may not provide legal effect. <br>
Mitigation: Disclose unavailable services and legal-effect boundaries, and do not fabricate verification, signing, or review results. <br>
Risk: PDF and OCR processing depends on local packages and optional system tools. <br>
Mitigation: Run the environment check before use, install required dependencies from the declared requirements files, and keep PDF/OCR dependencies updated. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ford828/skills/pdf-master) <br>
- [README](README.md) <br>
- [Security and Compliance Guardrails](references/security-compliance.md) <br>
- [Technical Implementation Specification](references/tech-spec.md) <br>
- [Command Guide](references/command-guide.md) <br>
- [Core Capabilities](references/capabilities-core.md) <br>
- [Value Capabilities](references/capabilities-value.md) <br>
- [Pro Capabilities](references/capabilities-pro.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands plus generated PDF, Office, spreadsheet, archive, image, or report files when the agent executes the workflows.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include quality-check notes, exception lists, previews, verification reports, and degradation notices for unavailable optional dependencies or external services.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
