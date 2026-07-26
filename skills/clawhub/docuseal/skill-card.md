## Description: <br>
Manage DocuSeal e-signature workflows from the terminal via the DocuSeal CLI, including creating templates from PDF, DOCX, and HTML, sending documents for signing, tracking submissions, and updating submitters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexbturchyn](https://clawhub.ai/user/alexbturchyn) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, automation engineers, and operations teams use this skill to prepare DocuSeal CLI commands for document templates, signing submissions, submitter updates, and CI/CD-friendly e-signature workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help an agent operate DocuSeal with an API key and affect real signing workflows, including sending emails or SMS, archiving records, updating templates or submitters, and marking submitters completed. <br>
Mitigation: Review commands before execution, especially commands that send notifications or change workflow state, and use credentials scoped to the intended DocuSeal workspace. <br>
Risk: The skill supports user-supplied local files, remote document URLs, and HTML content that are sent to the DocuSeal API for processing. <br>
Mitigation: Use trusted local files or approved HTTPS document URLs for signing materials and avoid submitting unreviewed sensitive content. <br>


## Reference(s): <br>
- [DocuSeal homepage](https://www.docuseal.com) <br>
- [DocuSeal API settings](https://console.docuseal.com/api) <br>
- [Templates reference](references/templates.md) <br>
- [Submissions reference](references/submissions.md) <br>
- [Submitters reference](references/submitters.md) <br>
- [DOCX dynamic content variables](references/docx-variables.md) <br>
- [PDF and DOCX field tags](references/field-tags.md) <br>
- [HTML field tags](references/html-fields.md) <br>
- [DocuSeal dynamic DOCX variables guide](https://www.docuseal.com/guides/use-dynamic-content-variables-in-docx-to-create-personalized-documents) <br>
- [DocuSeal embedded field tags guide](https://www.docuseal.com/guides/use-embedded-text-field-tags-in-the-pdf-to-create-a-fillable-form) <br>
- [DocuSeal HTML fillable form guide](https://www.docuseal.com/guides/create-pdf-document-fillable-form-with-html-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; DocuSeal CLI command output is JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the docuseal CLI, DOCUSEAL_API_KEY, and DOCUSEAL_SERVER.] <br>

## Skill Version(s): <br>
1.0.7 (source: artifact/SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
