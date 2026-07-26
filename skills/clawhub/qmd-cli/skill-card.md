## Description: <br>
Search and retrieve markdown documents from local knowledge bases using qmd, including BM25 keyword search, vector semantic search, and hybrid LLM-ranked query workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dpaluy](https://clawhub.ai/user/dpaluy) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to search, retrieve, and maintain locally indexed markdown knowledge bases such as notes, documentation, and meeting transcripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires installing and running the upstream qmd package. <br>
Mitigation: Install only when the qmd upstream package is trusted and prefer a pinned or released package when possible. <br>
Risk: Indexed QMD collections may expose local markdown content to agent search and retrieval workflows. <br>
Mitigation: Review directories before adding them as QMD collections and avoid indexing sensitive content that agents should not access. <br>
Risk: Running the qmd MCP server or daemon exposes the local index to MCP clients or agents. <br>
Mitigation: Run MCP server or daemon modes only when that access is intentional. <br>


## Reference(s): <br>
- [QMD upstream package repository](https://github.com/tobi/qmd) <br>
- [QMD CLI ClawHub release](https://clawhub.ai/dpaluy/skills/qmd-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON-oriented command usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires qmd CLI installation; commands should use --json for structured output.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
