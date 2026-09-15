## Description:

TextRazor (textrazor.com). Use this skill for ANY TextRazor request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate TextRazor through an OOMOL-connected account for content analysis, text classification, entity extraction, account quota lookup, and custom TextRazor resource management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup includes remote installer commands that should not be run blindly.

Mitigation: Manually review setup steps and prefer an official, versioned installation path with verification before installing the oo CLI.

Risk: TextRazor manager actions can change or delete custom classifiers or dictionaries.

Mitigation: Require explicit user confirmation of the exact operation, target, and payload before using custom_classifier_manager or dictionary_manager for upload, overwrite, deletion, or lifecycle changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-textrazor)
- [TextRazor Homepage](https://www.textrazor.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON connector responses when run with --json.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
