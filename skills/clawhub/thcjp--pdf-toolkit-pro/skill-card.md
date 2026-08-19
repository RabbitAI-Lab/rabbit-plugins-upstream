## Description:

PDF工具包（专业版） helps agents guide PDF creation, editing, conversion, merging, splitting, compression, encryption, watermarking, OCR, table extraction, batch processing, and audit-report workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and document-processing teams use this skill to guide local PDF processing tasks such as transforming files, extracting content, adding protection, running batches, and producing audit records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local PDF operations can overwrite, alter, or expose important documents if paths or batches are chosen carelessly.

Mitigation: Use explicit input and output paths, keep backups of important PDFs, and review batch targets before running operations on sensitive folders.

Risk: Weak or example encryption passwords can leave protected PDFs vulnerable.

Mitigation: Use a unique strong password for encryption workflows and do not reuse the example default password shown in the artifact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/pdf-toolkit-pro)
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python, YAML, bash, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local output artifacts such as processed PDFs, converted documents, extracted text or tables, and audit JSON when executed by an agent.]

## Skill Version(s):

1.0.3 (source: server release metadata); artifact frontmatter lists 1.0.0

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
