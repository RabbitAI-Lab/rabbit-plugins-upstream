## Description: <br>
Smart memory search with automatic vector fallback. Uses semantic embeddings when available, falls back to built-in search otherwise. Zero configuration - works immediately after ClawHub install. No setup required - just install and memory_search works immediately, gets better after optional sync. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluepointdigital](https://clawhub.ai/user/bluepointdigital) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to add memory_search, memory_get, memory_sync, and memory_status tools that search local memory files with vector embeddings when an index is available and keyword fallback otherwise. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can install npm dependencies, download and cache an embedding model, create a persistent local memory index, and run sync or search commands. <br>
Mitigation: Install from reviewed source, perform manual installation where possible, and review generated indexes and dependency changes before deployment. <br>
Risk: The memory_get path handling and shell command construction are identified by the security guidance as needing fixes before exposure to untrusted prompts or users. <br>
Mitigation: Restrict use to trusted users and prompts until path validation and command construction are remediated and re-scanned. <br>
Risk: The release is described as zero configuration, but the security summary says it can read more files and run more install/search-time code than that description makes clear. <br>
Mitigation: Document runtime file access and command behavior for operators, and review the tool commands before enabling automatic memory access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bluepointdigital/skills/vector-memory) <br>
- [Integration Guide](artifact/vector-memory/references/integration.md) <br>
- [pgvector Scale Guide](artifact/vector-memory/references/pgvector.md) <br>
- [Transformers.js](https://github.com/xenova/transformers.js) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [JSON results from tools plus Markdown and shell command guidance in documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results include path, line range, score, and snippet when available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata; artifact package.json also reports 1.0.0, while artifact changelog and skill manifest mention 2.1.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
