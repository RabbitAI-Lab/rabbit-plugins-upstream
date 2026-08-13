## Description:

Professional translation between Mandarin, English, and Spanish with cultural context, tone matching, and domain-specific formatting (business, legal, casual).

This skill is ready for commercial/non-commercial use.

## Publisher:

[aw207720-lgtm](https://clawhub.ai/user/aw207720-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use Translator Pro to translate documents, snippets, UI strings, and correspondence across Mandarin, English, and Spanish while preserving structure and receiving cultural notes for business, legal, or casual contexts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-stakes translations can be incorrect or ambiguous if the source language, target language, jurisdiction, region, or terminology are assumed.

Mitigation: Explicitly confirm those inputs and provide glossary terms before translating legal, business, or other high-stakes content.

Risk: Mandarin-Spanish translations may lose nuance when routed through English as a pivot.

Mitigation: Flag pivot-translated content with reduced confidence and add cultural notes for terms that may lose nuance.

Risk: Formatting-sensitive documents can be damaged if structure is not preserved.

Mitigation: Preserve Markdown, HTML, plain text, or JSON structure and report untranslated or ambiguous segments in warnings.

## Reference(s):

- [Glossary Format](references/glossary-format.md)
- [Mandarin-English Translation Notes](references/mandarin-english-notes.md)
- [Spanish-English Translation Notes](references/spanish-english-notes.md)
- [ClawHub Skill Page](https://clawhub.ai/aw207720-lgtm/skills/translator-pro)
- [Publisher Profile](https://clawhub.ai/user/aw207720-lgtm)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured translation result with translated text, language metadata, cultural notes, glossary matches, and warnings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves Markdown, HTML, plain text, and JSON structure when requested.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
