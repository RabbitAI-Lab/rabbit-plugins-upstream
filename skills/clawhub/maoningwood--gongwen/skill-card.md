## Description:

Generates Chinese official-style DOCX documents such as notices, reports, requests, replies, letters, and meeting minutes using built-in layout conventions, font checks, and numeric format validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maoningwood](https://clawhub.ai/user/maoningwood)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to draft, format, and validate Chinese official-style DOCX documents for WPS or Microsoft Office workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on commercial Chinese fonts that are not included in the release.

Mitigation: Run the bundled font checker before generating documents and require users to install fonts from licensed sources.

Risk: Broad activation wording may cause ordinary notice or report drafting requests to use this specialized official-document format automatically.

Mitigation: Review activation behavior before deployment and narrow triggering if this format should only apply to explicit official-document requests.

Risk: Generated DOCX output can have formatting drift if fonts are missing or the document is edited in another office suite.

Mitigation: Run the bundled numeric DOCX validator after generation and reopen WPS or Office files before checking final layout.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/maoningwood/skills/gongwen)
- [ZCode skill convention](https://zcode.dev)
- [Fangzheng font source](https://www.foundertype.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python examples and shell commands for generating and validating DOCX files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated documents depend on user-installed commercial fonts and should be validated with the bundled DOCX format checker.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
