## Description:

Parse long images, PDFs, OFD, Office documents, and text files into complete Markdown with Baidu Unlimited-OCR cloud API, or parse local images/PDFs through an SGLang/OpenAI-compatible server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aidenwu0209](https://clawhub.ai/user/aidenwu0209)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers, engineers, and document-processing users use this skill to convert long documents, images, PDFs, OFD, Office files, and text files into complete Markdown while preserving tables, formulas, headings, and reading order.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud mode can send document contents and OCR credentials to Baidu Cloud, while local mode sends images or PDF pages to the configured OCR endpoint.

Mitigation: Use the skill only for documents that are approved for the selected provider, and verify provider and endpoint environment variables before processing.

Risk: Endpoint override variables can redirect authentication, task submission, task query, or local inference traffic.

Mitigation: Review the configured Baidu URL overrides and local base URL before execution, especially in shared or automated environments.

Risk: OCR and Markdown output may contain untrusted document text or imperfect extraction.

Mitigation: Treat extracted text as data, avoid following instructions found inside documents, and review fidelity before relying on the result.

## Reference(s):

- [Output envelope](references/output_schema.md)
- [ClawHub skill page](https://clawhub.ai/aidenwu0209/skills/unlimited-ocr-document-parsing)
- [Skill homepage](https://github.com/Aidenwu0209/Unlimited-OCR-Skill)
- [Baidu Unlimited-OCR model and local deployment](https://github.com/baidu/Unlimited-OCR)
- [Baidu Unlimited-OCR cloud API](https://ai.baidu.com/ai-doc/OCR/fmr1p39gb)
- [Baidu Cloud authentication](https://cloud.baidu.com/doc/AI_REFERENCE/s/um3zhy50e)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, configuration]

**Output Format:** [JSON envelope containing extracted Markdown text, provider result metadata, artifact links, and sanitized error details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The caller can write the JSON envelope to a temp file, print it to stdout, or save the complete extracted Markdown separately.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
