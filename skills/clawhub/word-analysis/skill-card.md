## Description:

Word Analysis extracts text and tables from standard DOCX files locally, sends the parsed text to the analysis platform, and supports summaries, key points, evidence-based Q&A, comparison of two to three Word documents, and exportable results with paragraph evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze authorized DOCX documents, ask questions grounded in paragraph text, compare two to three Word documents, and export successful analysis results as Markdown or JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Extracted DOCX text, file name, and paragraph locations are sent to ai-skills.open-idea.net for analysis and billing.

Mitigation: Use only with authorization, and avoid confidential documents unless the platform's data handling terms are acceptable.

Risk: DOCX content may contain untrusted instructions or unsupported content.

Mitigation: Treat document text as evidence only, verify quotes against paragraph text, and clearly report unsupported DOC, encrypted files, or image OCR needs.

Risk: API key exposure could allow unauthorized use.

Mitigation: Store WORD_ANALYSIS_API_KEY in environment configuration and do not log or display it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/word-analysis)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key Configuration](https://ai-skills.open-idea.net/skill-docs/word-analysis/API-KEY.md)
- [Local Word Extraction](https://ai-skills.open-idea.net/skill-docs/word-analysis/LOCAL-EXTRACTION.md)
- [HTTP Requests](https://ai-skills.open-idea.net/skill-docs/word-analysis/HTTP-REQUESTS.md)
- [Operations](https://ai-skills.open-idea.net/skill-docs/word-analysis/OPERATIONS.md)
- [Behavior Rules](https://ai-skills.open-idea.net/skill-docs/word-analysis/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Text, Markdown, and JSON; setup guidance may include shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local extraction supports standard DOCX files up to 10 MB, 2000 non-empty paragraphs, and 120000 characters; image OCR, legacy DOC files, and encrypted documents are not supported by the local package.]

## Skill Version(s):

1.0.3 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
