## Description:

PDF Analysis helps agents extract text from text-layer PDFs, submit page-aware content to an AI Skills API, and produce summaries, key points, document-grounded Q&A, multi-document comparisons, and Markdown or JSON exports with page evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze non-scanned PDFs with retained filename, page, and quote evidence. It supports summaries, key points, document-grounded questions, comparison of two to three PDFs, and private export of successful analysis results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key and extracted PDF text can be sent to an endpoint selected through AI_SKILLS_API_URL.

Mitigation: Use only a trusted HTTPS API endpoint, verify that AI_SKILLS_API_URL is unset or points to the intended service, and keep the API key revocable.

Risk: Extracted text from contracts, financial records, personal data, or other confidential PDFs may be sent to the configured platform.

Mitigation: Confirm user authorization before processing sensitive documents and delete temporary extraction JSON after analysis.

Risk: The local extraction path depends on PyMuPDF behavior in the runtime environment.

Mitigation: Install PyMuPDF in an isolated environment and pin the dependency version in controlled deployments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/pdf-analysis)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key Configuration](https://ai-skills.open-idea.net/skill-docs/pdf-analysis/API-KEY.md)
- [Local PDF Text Extraction](https://ai-skills.open-idea.net/skill-docs/pdf-analysis/LOCAL-EXTRACTION.md)
- [HTTP Requests and Task Polling](https://ai-skills.open-idea.net/skill-docs/pdf-analysis/HTTP-REQUESTS.md)
- [Operations and Data Structures](https://ai-skills.open-idea.net/skill-docs/pdf-analysis/OPERATIONS.md)
- [Evidence and Safety Rules](https://ai-skills.open-idea.net/skill-docs/pdf-analysis/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and JSON analysis results with page-level evidence; local extraction emits JSON document payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PDF_ANALYSIS_API_KEY. Supports text-layer PDFs only, with no OCR. Single-document extraction is limited to 10 MB, 50 pages, and 120000 characters; comparison accepts 2 to 3 documents up to 180000 total characters.]

## Skill Version(s):

1.1.1 (source: server release evidence and package metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
