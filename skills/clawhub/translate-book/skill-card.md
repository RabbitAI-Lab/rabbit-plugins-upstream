## Description:

Translate PDF, DOCX, EPUB, or Markdown books into another language using parallel subagents, then compile the result as HTML, DOCX, EPUB, or PDF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deusyu](https://clawhub.ai/user/deusyu)

### License/Terms of Use:

MIT

## Use Case:

Readers use this skill to translate book files between languages and create a complete translated book in a format such as HTML, DOCX, EPUB, or PDF.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security guidance reports that a crafted book could cause unrelated local files to be included in translation outputs.

Mitigation: Run translations in a dedicated working directory and review generated files before sharing them.

Risk: Installation and publishing examples use packages without fixed versions.

Mitigation: Review those commands and pin package versions before running them.

Risk: The security scan was partial, with some text checks degraded, two images out of scope, and some references unresolved.

Mitigation: Treat the scan as incomplete and review the skill and its dependencies before use.

## Reference(s):

- [Project homepage](https://github.com/deusyu/translate-book)
- [ClawHub skill release](https://clawhub.ai/deusyu/skills/translate-book)

## Skill Output:

**Output Type(s):** [Markdown, Files]

**Output Format:** [Translated Markdown chunks and compiled HTML, DOCX, EPUB, or PDF files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chunked, resumable translation; final format depends on the user's chosen output.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
