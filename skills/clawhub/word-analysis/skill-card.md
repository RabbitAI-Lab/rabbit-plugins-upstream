## Description:

Analyzes standard DOCX files for summaries, key points, question answering, multi-document comparison, and evidence-backed exports; it does not support legacy DOC, encrypted documents, or image OCR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to analyze standard DOCX documents, ask questions grounded in extracted text, compare two to three documents, and export results with paragraph-level evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Extracted DOCX text is sent to the provider service.

Mitigation: Process regulated or highly confidential documents only after confirming the provider's data handling terms and user authorization.

Risk: The WORD_ANALYSIS_API_KEY credential can authorize provider requests if exposed.

Mitigation: Store the API key only in the configured environment variable and avoid logging or pasting it into conversations.

Risk: An untrusted AI_SKILLS_API_URL override could redirect document text and credentials.

Mitigation: Use the default trusted service URL unless the replacement endpoint is explicitly trusted.

Risk: Crafted or untrusted DOCX files may stress the local extractor.

Mitigation: Treat untrusted DOCX files cautiously and rely on the documented size, paragraph, and character limits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/word-analysis)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/word-analysis/API-KEY.md)
- [Local Word extraction](https://ai-skills.open-idea.net/skill-docs/word-analysis/LOCAL-EXTRACTION.md)
- [HTTP requests](https://ai-skills.open-idea.net/skill-docs/word-analysis/HTTP-REQUESTS.md)
- [Operations](https://ai-skills.open-idea.net/skill-docs/word-analysis/OPERATIONS.md)
- [Evidence and safety rules](https://ai-skills.open-idea.net/skill-docs/word-analysis/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON responses with optional shell commands and evidence exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires WORD_ANALYSIS_API_KEY; local extraction supports standard DOCX files up to 10 MB, 2000 non-empty paragraphs, and 120000 characters.]

## Skill Version(s):

1.0.1 (source: release metadata and package metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
