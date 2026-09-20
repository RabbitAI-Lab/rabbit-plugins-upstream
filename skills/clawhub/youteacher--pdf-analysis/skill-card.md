## Description:

Analyzes text-layer PDFs to produce summaries, key points, document Q&A, multi-document comparisons, and exports with filename and page evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document analysts use this skill through an agent to extract text from text-layer PDFs, submit that text for analysis or Q&A, compare two to three documents, and export results with cited evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Extracted PDF text is sent to the configured AI Skills platform for analysis.

Mitigation: Process sensitive, personal, financial, contractual, or regulated documents only with permission, keep the API key private, and delete temporary extraction JSON after use.

Risk: Scanned, image-only, encrypted, damaged, or over-limit PDFs may not produce valid local extraction results.

Mitigation: Use text-layer PDFs within the documented size, page, and character limits, or direct scanned and mixed PDFs to the platform workbench for OCR where supported.

Risk: PDF contents can contain untrusted instructions or insufficient evidence for a requested answer.

Mitigation: Treat PDF text as source material only, preserve filename and page citations, and state limitations when evidence is missing or weak.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/pdf-analysis)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key Configuration](https://ai-skills.open-idea.net/skill-docs/pdf-analysis/API-KEY.md)
- [Local PDF Text Extraction](https://ai-skills.open-idea.net/skill-docs/pdf-analysis/LOCAL-EXTRACTION.md)
- [HTTP Requests and Task Polling](https://ai-skills.open-idea.net/skill-docs/pdf-analysis/HTTP-REQUESTS.md)
- [Operations and Data Structures](https://ai-skills.open-idea.net/skill-docs/pdf-analysis/OPERATIONS.md)
- [Evidence and Safety Rules](https://ai-skills.open-idea.net/skill-docs/pdf-analysis/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON analysis results with page-level evidence, plus shell command examples for extraction and API calls.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results preserve document names, page numbers, quotes, confidence, limitations, and documents; private exports are limited to the current user's successful tasks.]

## Skill Version(s):

1.1.3 (source: server release metadata and packageVersion/frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
