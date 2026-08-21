## Description:

This skill supports bidirectional Chinese/English translation for BWC technical and API documentation while preserving code, identifiers, placeholders, and approved terminology.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cyknowgen](https://clawhub.ai/user/cyknowgen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical writers, and localization reviewers use this skill to translate BWC product, API, SDK, release-note, and developer-facing content between Chinese and English. It also helps validate that BWC-specific terms follow the approved glossary and that code-like material is unchanged.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad routing triggers such as BWC, translate, and 翻译 may activate the skill for content that is not actually BWC-specific.

Mitigation: Confirm the source content is BWC-related before applying the skill; use a generic translation workflow when no BWC context is present.

Risk: The glossary contains template and TBD entries, so production, legal, or brand-sensitive translations may use incomplete terminology.

Mitigation: Populate and validate the glossary before production use, and review every [NEEDS-GLOSSARY] marker before accepting the translation.

## Reference(s):

- [BWC Glossary - Terminology Source of Truth](references/glossary.md)
- [BWC Technical Translation Style Guide](references/style-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text translation with preserved code, identifiers, placeholders, and review flags for unresolved glossary terms]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Flags missing terminology with [NEEDS-GLOSSARY] and may include a brief summary of unresolved terms for user review.]

## Skill Version(s):

1.0.0 (source: server release evidence and artifact/manifest.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
