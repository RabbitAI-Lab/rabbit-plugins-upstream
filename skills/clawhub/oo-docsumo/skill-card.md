## Description:

Docsumo (docsumo.com) skill for reading, creating, and updating data through the OOMOL-connected Docsumo connector instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to operate Docsumo through the oo CLI, including account inspection, document metadata retrieval, extracted-data review, document listing, and URL-based document upload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Review the oo CLI installation path before installing, and prefer a pinned official release with a verified signature or checksum.

Risk: The upload_document_from_url action changes Docsumo state by uploading a public file URL for a selected document type.

Mitigation: Confirm the exact URL, document type, and intended effect with the user before running upload or any other state-changing action.

Risk: Connector access depends on an OOMOL-connected Docsumo account and may fail because of missing authentication, expired credentials, missing scopes, or billing limits.

Mitigation: Run actions only after schema inspection, and use the documented setup steps only when a command returns a matching auth, connection, or billing error.

## Reference(s):

- [Docsumo homepage](https://www.docsumo.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-docsumo)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return oo CLI JSON responses that include connector data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
