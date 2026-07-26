## Description: <br>
Upload, edit, and export documents via Nudocs.ai for shareable collaborative editing links, rich document editing, and retrieving edited content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jdrhyne](https://clawhub.ai/user/jdrhyne) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, developers, and document authors use this skill to upload documents to Nudocs.ai, share editing links, list documents, pull edited versions back in selected formats, and manage cloud document records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can upload, share, download, list, and delete cloud documents through Nudocs.ai. <br>
Mitigation: Use it only for documents intended for Nudocs.ai, treat returned links and document identifiers as sensitive, and confirm document IDs before pull, link, or delete operations. <br>
Risk: The skill requires Nudocs credentials through NUDOCS_API_KEY or a local config file. <br>
Mitigation: Store credentials securely, avoid exposing API keys in shared logs or documents, and rotate keys if they may have been disclosed. <br>


## Reference(s): <br>
- [Nudocs](https://nudocs.ai) <br>
- [Nudocs CLI](https://github.com/PSPDFKit/nudocs-cli) <br>
- [Nudocs MCP Server](https://github.com/PSPDFKit/nudocs-mcp-server) <br>
- [Document Design Reference](references/document-design.md) <br>
- [Nudocs Format Reference](references/formats.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and document/file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or retrieve documents in formats including Markdown, DOCX, PDF, HTML, LaTeX, EPUB, plain text, and related document formats.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
