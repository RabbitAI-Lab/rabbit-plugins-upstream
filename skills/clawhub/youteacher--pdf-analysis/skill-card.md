## Description:

Analyzes text-based PDFs for summaries, document questions, and comparisons with page-linked evidence, without local OCR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Users and their agents analyze, question, or compare text-based PDF documents and receive conclusions supported by file names, page numbers, and excerpts. Results can be exported as Markdown and JSON on request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Extracted PDF text is sent to the AI Skills platform, potentially exposing sensitive document contents.

Mitigation: Obtain authorization before processing contracts, financial records, or personal data; delete temporary extraction JSON after use.

Risk: API credentials may be exposed if copied into conversation or logs.

Mitigation: Configure the API key through the environment and never display or log the full key.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/youteacher/skills/pdf-analysis)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/pdf-analysis/API-KEY.md)
- [Local PDF text extraction](https://ai-skills.open-idea.net/skill-docs/pdf-analysis/LOCAL-EXTRACTION.md)
- [HTTP requests and task polling](https://ai-skills.open-idea.net/skill-docs/pdf-analysis/HTTP-REQUESTS.md)
- [Operations and response structure](https://ai-skills.open-idea.net/skill-docs/pdf-analysis/OPERATIONS.md)
- [Evidence and safety rules](https://ai-skills.open-idea.net/skill-docs/pdf-analysis/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Text responses with page-linked citations; optional Markdown and JSON exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local extraction requires a text layer; no local OCR or encrypted-PDF support. Single documents are limited to 10 MB, 50 pages, and 120,000 characters.]

## Skill Version(s):

1.3.0 (source: ClawHub release metadata and skill packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
