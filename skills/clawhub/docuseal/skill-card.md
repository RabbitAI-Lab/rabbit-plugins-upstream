## Description:

Manage DocuSeal e-signature workflows from the terminal via the DocuSeal CLI: create templates from PDF, DOCX, or HTML, send documents for signing, track submissions, and update submitters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docuseal](https://clawhub.ai/user/docuseal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to prepare DocuSeal CLI commands for creating templates, sending signature requests, tracking signing status, and updating submitters in shells, scripts, or CI/CD pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents using this skill can operate a DocuSeal account through an API key.

Mitigation: Use a least-privilege API key and install only when agent access to DocuSeal workflows is intended.

Risk: Commands can send signature requests by email or SMS and can update templates, submissions, and submitters.

Mitigation: Confirm template, submission, and submitter IDs; review recipients before sending; use no-send-email options or test accounts for automation trials.

Risk: Commands may pass local files, remote document URLs, HTML content, or internal URLs to the DocuSeal API.

Mitigation: Share only intended document content and avoid passing sensitive internal URLs unless that disclosure is deliberate.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/docuseal/skills/docuseal)
- [DocuSeal Homepage](https://www.docuseal.com)
- [Templates](references/templates.md)
- [Submissions](references/submissions.md)
- [Submitters](references/submitters.md)
- [PDF / DOCX Field Tags](references/field-tags.md)
- [HTML Field Tags](references/html-fields.md)
- [DOCX Dynamic Content Variables](references/docx-variables.md)
- [DocuSeal DOCX Dynamic Content Variables Guide](https://www.docuseal.com/guides/use-dynamic-content-variables-in-docx-to-create-personalized-documents)
- [DocuSeal Embedded Field Tags Guide](https://www.docuseal.com/guides/use-embedded-text-field-tags-in-the-pdf-to-create-a-fillable-form)
- [DocuSeal HTML Field Tags Guide](https://www.docuseal.com/guides/create-pdf-document-fillable-form-with-html-api)
- [Example PDF with Field Tags](https://www.docuseal.com/examples/fieldtags.pdf)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON-oriented CLI parameter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [DocuSeal CLI command output is documented as JSON; commands require DOCUSEAL_API_KEY and may use DOCUSEAL_SERVER.]

## Skill Version(s):

1.0.8 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
