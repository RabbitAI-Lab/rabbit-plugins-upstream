## Description: <br>
将粘贴的中文文本或现有 .docx 文档，转换为符合党政机关公文格式规范的 Word 文档。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wing-art](https://clawhub.ai/user/wing-art) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, developers, and document operators use this skill to generate or reformat Chinese Party and government official documents as Word .docx files with prescribed layout, typography, headers, signatures, attachments, page numbers, and validation checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run local scripts that create or reformat official Word documents, so incorrect inputs or metadata can produce misleading operational documents. <br>
Mitigation: Review source text, recipient, issuer, document type, date, attachment, confidentiality, and signing fields before distribution; use placeholders only where values remain unknown. <br>
Risk: Missing official-document fonts can cause Word to substitute fonts and shift layout. <br>
Mitigation: Run the bundled font check and review generated documents on a system with the required fonts installed before printing or sending. <br>
Risk: The format-only workflow preserves paragraphs and tables but does not preserve images, comments, revision history, text boxes, or complex headers. <br>
Mitigation: Use format-only only when those elements are not required, and compare the generated document against the original when handling complex Word files. <br>
Risk: The security guidance notes operational helper workflows and service API scripts in the artifact set. <br>
Mitigation: Install only for intended operational use, review configured tokens and organization memory settings first, and use least-privilege service credentials. <br>


## Reference(s): <br>
- [Skill page](https://clawhub.ai/wing-art/skills/format-official-docx) <br>
- [公文文种选择速查](references/document-types.md) <br>
- [党政机关公文格式规则](references/format-rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [files, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Generated .docx files with Markdown guidance and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write generated Word documents to outputs/ and may emit format-check results or font warnings.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
