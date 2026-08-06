## Description: <br>
RenderMark helps agents render, export, publish, share, validate, diff, and sync Markdown documents through the RenderMark MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jmsaavedra](https://clawhub.ai/user/jmsaavedra) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical writers, and other document authors use this skill when an agent needs to turn Markdown into styled previews, PDFs, DOCX files, HTML, images, hosted pages, Google Docs, visual diffs, or GitHub-synced documentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publishing, sharing, or GitHub sync actions can expose private or unintended document content. <br>
Mitigation: Review document content, share recipients, and publish settings before sharing links or enabling sync, especially for private repository material. <br>
Risk: The local RenderMark configuration can contain API keys or OAuth tokens. <br>
Mitigation: Protect ~/.rendermark/config.json and use environment or account controls appropriate for RenderMark and Google credentials. <br>
Risk: Rendered or exported documents may preserve mistakes, broken links, or misleading formatting from the source Markdown. <br>
Mitigation: Use validation and preview workflows for important documents before publishing, exporting, or sending them to others. <br>


## Reference(s): <br>
- [RenderMark Skill on ClawHub](https://clawhub.ai/jmsaavedra/skills/rendermark) <br>
- [RenderMark Homepage](https://rendermark.app) <br>
- [RenderMark MCP Server on npm](https://www.npmjs.com/package/@rendermark/mcp-server) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [Tools Reference](references/tools-reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with MCP tool calls that can return file paths, HTML, image data, document URLs, or document metadata] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may depend on RenderMark API access, local browser availability for PDF or image export, and optional Google OAuth configuration for Google Docs publishing.] <br>

## Skill Version(s): <br>
0.1.10 (source: server release metadata, target metadata, and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
