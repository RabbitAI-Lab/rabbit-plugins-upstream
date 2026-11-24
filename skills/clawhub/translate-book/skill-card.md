## Description:

Translate books (PDF/DOCX/EPUB) into any language using parallel sub-agents. Converts input -> Markdown chunks -> translated chunks -> HTML/DOCX/EPUB/PDF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deusyu](https://clawhub.ai/user/deusyu)

### License/Terms of Use:

MIT

## Use Case:

Readers and translators use this skill to translate complete PDF, DOCX, EPUB, or Markdown books into another language and export the result in a readable document format.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags possible copying of unrelated local files and automatic dependency installation; its analysis coverage is incomplete.

Mitigation: Review setup instructions before installing, limit file access to the intended book and outputs, and use only dependency installers and versions you trust.

## Reference(s):

- [Project homepage](https://github.com/deusyu/translate-book)
- [ClawHub skill release](https://clawhub.ai/deusyu/skills/translate-book)

## Skill Output:

**Output Type(s):** [Files, Markdown, Guidance]

**Output Format:** [Translated HTML, DOCX, EPUB, or PDF files, with Markdown chunks and run summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The available formats depend on installed conversion tools; translation requires an agent runtime that can launch sub-agents.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
