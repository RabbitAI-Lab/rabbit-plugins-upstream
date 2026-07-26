## Description: <br>
Query the DeepWiki MCP server for GitHub repository documentation, wiki structure, and AI-powered questions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arun-8687](https://clawhub.ai/user/arun-8687) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to query public GitHub repository documentation through DeepWiki, including wiki structure, topic contents, and question-answering grounded in repository documentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Repository names, wiki paths, and question text are sent to the DeepWiki service. <br>
Mitigation: Use only public repository context and avoid secrets, private repository details, or confidential project information in prompts. <br>


## Reference(s): <br>
- [DeepWiki MCP documentation](https://docs.devin.ai/work-with-devin/deepwiki-mcp) <br>
- [DeepWiki MCP server endpoint](https://mcp.deepwiki.com/mcp) <br>
- [ClawHub skill page](https://clawhub.ai/arun-8687/skills/deepwiki) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown or plain text returned from DeepWiki, with shell command examples for invocation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Queries are sent to DeepWiki for public GitHub repositories; no authentication is required.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
