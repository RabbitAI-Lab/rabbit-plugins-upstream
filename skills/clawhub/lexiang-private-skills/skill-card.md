## Description: <br>
This skill helps an AI agent work with a private Tencent Lexiang knowledge base through authenticated search, reading, writing, block editing, file upload, and configuration workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lexiang](https://clawhub.ai/user/lexiang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and developers use this skill to connect an AI agent to a private Lexiang deployment for knowledge-base search, document creation, content editing, file operations, and operational setup guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill connects to a private Lexiang instance using a bearer token. <br>
Mitigation: Keep LEXIANG_TOKEN private, redact mcp.json in screenshots and logs, and install only when the publisher and target private instance are trusted. <br>
Risk: Write, delete, and bulk upload workflows can modify knowledge-base content. <br>
Mitigation: Confirm every write, delete, or bulk upload target before execution, and use dry-run or plan review before folder uploads. <br>
Risk: Folder upload or sync workflows can include more local files than intended. <br>
Mitigation: Avoid broad project or home directories, review upload plans and file counts, and batch large operations as the skill guidance describes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lexiang/skills/lexiang-private-skills) <br>
- [README](artifact/README.md) <br>
- [Skill routing and safety rules](artifact/SKILL.md) <br>
- [MCP configuration template](artifact/mcp.json) <br>
- [Lexiang setup guidance](artifact/references/setup.md) <br>
- [Lexiang base rules](artifact/references/base.md) <br>
- [Search and reading workflows](artifact/references/search.md) <br>
- [Document writing workflows](artifact/references/writer.md) <br>
- [File upload workflows](artifact/references/files.md) <br>
- [Block editing workflows](artifact/references/blocks.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with MCP tool names, JSON configuration snippets, and shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include dry-run plans, target-confirmation prompts, generated Lexiang links, and batching guidance for larger uploads.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
