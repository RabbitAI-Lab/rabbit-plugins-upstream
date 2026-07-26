## Description: <br>
Parses PDF, Word, and CNKI documents, then helps an agent write an evidence-tracked literature review, adapt to journal style, audit citations, and generate a Word document. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liqiang12689](https://clawhub.ai/user/liqiang12689) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, students, and writing assistants use this skill to turn supplied literature files into a traceable narrative, scoping, critical, methodological, or background review. It supports document ingestion, evidence extraction, synthesis, journal-style profiling, citation auditing, and editable Word output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Directory inputs may recursively process more local documents than intended. <br>
Mitigation: Use a dedicated literature folder and review the generated manifest before relying on extracted content. <br>
Risk: OCR, legacy document conversion, or CNKI export parsing can produce incomplete or inaccurate text. <br>
Mitigation: Treat warning, failed, OCR-derived, and metadata-only records as limited evidence and verify key claims against the original documents. <br>
Risk: A generated review may contain unsupported claims, incorrect citation mapping, or overgeneralized journal-style conclusions. <br>
Mitigation: Run the citation and quality audit, separate evidence documents from style samples, and keep source-backed limitations in the final output. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/liqiang12689/skills/write-literature-review) <br>
- [Document Ingestion](artifact/references/document-ingestion.md) <br>
- [Evidence Extraction](artifact/references/evidence-extraction.md) <br>
- [Synthesis and Structure](artifact/references/synthesis-and-structure.md) <br>
- [Journal Style Profile](artifact/references/journal-style-profile.md) <br>
- [Citation and Quality Audit](artifact/references/citation-and-quality-audit.md) <br>
- [Word Output](artifact/references/word-output.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown reports and editable DOCX files, with supporting JSON manifests and shell commands when document extraction is needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce literature inventories, evidence matrices, style profiles, citation audits, Markdown source, extracted text files, manifest JSON, and Word documents.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter says 1.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
