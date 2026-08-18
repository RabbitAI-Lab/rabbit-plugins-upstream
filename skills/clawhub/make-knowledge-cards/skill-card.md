## Description:

Convert pasted articles, local Markdown/TXT files, or PDF documents into 5-8 concise knowledge cards, each with a title, core knowledge summary, brief explanation, and an example or self-test question.

This skill is ready for commercial/non-commercial use.

## Publisher:

[slyum123](https://clawhub.ai/user/slyum123)

### License/Terms of Use:

MIT-0

## Use Case:

External users, students, and knowledge workers use this skill to turn pasted text or local Markdown, TXT, and PDF documents into concise study cards for review and self-testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDF parsing can expose the agent runtime to malformed or untrusted local files.

Mitigation: Use caution with PDFs from untrusted sources, keep pypdf updated, and confirm any local file path before allowing the agent to read it.

Risk: Generated cards may omit secondary points or over-compress long documents.

Mitigation: Review the Markdown cards against the source text, especially for long articles where the skill intentionally limits output to the most central points.

Risk: Unsupported inputs such as URLs, scanned PDFs, encrypted PDFs, and non-Markdown/TXT/PDF formats may fail or produce no cards.

Mitigation: Provide pasted text or supported local files; run OCR for scanned PDFs and decrypt encrypted PDFs before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/slyum123/skills/make-knowledge-cards)
- [Publisher profile](https://clawhub.ai/user/slyum123)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown knowledge cards with optional shell command guidance for PDF extraction]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces 5-8 cards by default, fewer when the source lacks enough distinct points, and a brief generated-from summary line.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, manifest.yaml, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
