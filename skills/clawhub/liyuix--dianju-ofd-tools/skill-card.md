## Description:

An OFD document processing tool that converts PDF/OFD files, converts OFD to images, and supports multiple document formats via the ofd365.com API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liyuix](https://clawhub.ai/user/liyuix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document-workflow operators use this skill to convert OFD, PDF, office documents, text, and image files through CLI, stdio MCP, or SSE server modes. It is suited for workflows that can send selected files to the ofd365.com conversion API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read local files chosen by path and can upload selected documents to the third-party ofd365.com conversion API.

Mitigation: Use only approved, non-sensitive files unless policy permits external processing, and avoid private, regulated, credential-bearing, or confidential documents.

Risk: SSE mode can expose conversion and file-reading behavior over HTTP/SSE if deployed beyond a trusted local environment.

Mitigation: Run SSE mode only in trusted environments with strong access controls and network exposure limited to intended clients.

Risk: Temporary download links may expose converted documents while they remain valid.

Mitigation: Retrieve outputs promptly, share links only with authorized users, and handle downloaded files according to the source document's sensitivity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liyuix/skills/dianju-ofd-tools)
- [ofd365 API endpoint](https://ofd365.com/admin-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON parameter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Conversion tools return temporary download links or extracted text; the local file-reading tool returns Base64-encoded file content.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
