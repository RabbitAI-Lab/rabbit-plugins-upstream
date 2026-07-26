## Description: <br>
Local search/indexing CLI (BM25 + vectors + rerank) with MCP mode. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[instant-picture](https://clawhub.ai/user/instant-picture) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to index selected local files, search them with keyword, vector, or hybrid retrieval, and expose qmd through MCP mode when needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Indexed files are stored in a local cache, which can include sensitive content if broad directories are indexed. <br>
Mitigation: Use narrow paths and masks, avoid secrets or sensitive personal directories, and clear ~/.cache/qmd when the index is no longer needed. <br>


## Reference(s): <br>
- [qmd package](https://github.com/tobi/qmd) <br>
- [Skill page](https://clawhub.ai/instant-picture/skills/qmd-1-0-0) <br>
- [Publisher profile](https://clawhub.ai/user/instant-picture) <br>
- [Homepage](https://tobi.lutke.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the qmd binary; embeddings and rerank use Ollama at OLLAMA_URL when configured.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
