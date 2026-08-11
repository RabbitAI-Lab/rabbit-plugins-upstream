## Description:

Converts PDF or image files into editable Word documents through the Scnet asynchronous document conversion service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

Developers and document-processing users use this skill to submit local PDF or supported image files to Scnet, poll the conversion task, and receive a temporary download link for an editable Word document.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads user-selected local documents to the external Scnet API, which can expose document contents.

Mitigation: Use only with files approved for Scnet processing, and avoid confidential, regulated, or private PDFs unless that external service is approved.

Risk: Any existing file path provided to the script can be uploaded.

Mitigation: Confirm the exact local file path before execution and prefer test files when validating configuration.

Risk: Converted document links are temporary download URLs returned by the service.

Mitigation: Retrieve converted files promptly and handle returned links as sensitive access-bearing URLs.

## Reference(s):

- [Server-resolved source repository](https://github.com/SCNet-sugon/pdf_to_word)
- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/pdf-to-word)
- [Scnet service homepage](https://www.scnet.cn)
- [Scnet PDF to Word API docs](artifact/references/api-docs.md)
- [Document conversion field summary](artifact/assets/templates/fields-summary.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON printed to stdout with task metadata and a results array of temporary Word document download URLs; errors are text messages.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCNET_API_KEY, uploads the selected local file to Scnet, and polls until success, failure, or timeout.]

## Skill Version(s):

1.0.0 (source: frontmatter, skill.yaml, CHANGELOG, released 2026-08-11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
