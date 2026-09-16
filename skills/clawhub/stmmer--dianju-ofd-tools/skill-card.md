## Description:

Dianju OFD Tools helps agents convert local PDF and OFD files between formats and extract text content from OFD files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stmmer](https://clawhub.ai/user/stmmer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document-processing agents use this skill to convert PDF and OFD documents, retrieve temporary download links for converted files, and extract OFD text as structured content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup uses an unpinned external package and sends credentials and documents to an HTTP API endpoint.

Mitigation: Use only a trusted pinned package version, require HTTPS endpoints, and approve the API service before processing sensitive documents.

Risk: APP_KEY values may be exposed through shared commands or logs.

Mitigation: Provide credentials through protected environment handling and avoid including real keys in shared commands, examples, or logs.

Risk: Converted files are delivered through temporary links that may expire or be unsuitable for uncontrolled sharing.

Mitigation: Download outputs promptly, verify generated file integrity, and avoid sharing temporary links outside approved workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/stmmer/skills/dianju-ofd-tools)
- [Publisher profile](https://clawhub.ai/user/stmmer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Conversion calls return temporary download links; OFD content extraction returns JSON arrays.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
