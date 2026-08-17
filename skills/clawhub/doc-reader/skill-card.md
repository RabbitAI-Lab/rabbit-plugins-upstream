## Description:

Extracts plain text and lightweight structure from local PDF, DOCX, TXT, and Markdown files for downstream summarization, retrieval, structured extraction, and knowledge ingestion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and knowledge workers use this skill to convert local documents into clean text or structured JSON before summarization, search indexing, field extraction, translation, or knowledge-base ingestion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled learning script can persist free-form usage data in learned_patterns.json without clear scoping or retention controls.

Mitigation: Use doc_extract.py for local document extraction and avoid running learner.py with sensitive notes or document-derived details unless retention in learned_patterns.json is acceptable.

Risk: Extracted document text and generated output files may contain confidential or personal information.

Mitigation: Process only owned or authorized documents, keep outputs local, and redact sensitive content before sharing results with downstream tools or third parties.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/doc-reader)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Guidance]

**Output Format:** [Plain text or structured JSON, with Markdown usage guidance and CLI shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local extraction can write output files and supports a max page or paragraph limit for previews.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
