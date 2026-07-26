## Description: <br>
Search local documents, files, notes, and knowledge bases; index directories; search with BM25, vector, or hybrid retrieval; and get AI answers with citations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gmickel](https://clawhub.ai/user/gmickel) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and knowledge workers use this skill to let an agent operate the local GNO CLI for indexing local folders, searching documents and notes, retrieving cited content, managing local search collections, and setting up optional MCP or web UI access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can grant an agent broad access to run local GNO commands that index private files. <br>
Mitigation: Use narrow collections and avoid adding folders that contain secrets or sensitive material. <br>
Risk: GNO commands can change assistant configurations, start persistent services, export content, or delete local GNO data. <br>
Mitigation: Review proposed commands before execution, prefer dry-run or preview modes for configuration and publishing actions, and reserve destructive commands for explicit user-approved maintenance. <br>
Risk: MCP write tools and the web UI can expand the skill's local access surface. <br>
Mitigation: Enable MCP write tools only when needed and avoid exposing the web UI beyond the local machine unless the network impact is understood. <br>


## Reference(s): <br>
- [GNO Skill README](artifact/README.md) <br>
- [GNO Skill Instructions](artifact/SKILL.md) <br>
- [GNO CLI Reference](artifact/cli-reference.md) <br>
- [GNO MCP Reference](artifact/mcp-reference.md) <br>
- [GNO Usage Examples](artifact/examples.md) <br>
- [GNO MCP Documentation](https://www.gno.sh/docs/MCP) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include citations, document URIs, file paths, CLI status output, MCP setup steps, and web UI process guidance depending on the requested workflow.] <br>

## Skill Version(s): <br>
1.2.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
