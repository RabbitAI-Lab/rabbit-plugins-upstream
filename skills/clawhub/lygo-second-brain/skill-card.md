## Description: <br>
LYGO Second Brain helps agents manage a local Obsidian-style markdown vault with Ollama-backed ingest, indexing, semantic search, consensus checks, and wiki page generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to compound local notes into a searchable second brain, generate wiki pages from vault content, and run consensus checks before saving contentious claims. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and write the configured local vault and create local git commits there. <br>
Mitigation: Use a dedicated vault path, review generated notes and git diffs, and keep secrets out of vault content. <br>
Risk: Vault content may contain sensitive personal or project information. <br>
Mitigation: Treat LYGO_VAULT_ROOT as sensitive and summarize rather than copying vault contents into chat logs or public repositories. <br>
Risk: Inference settings can expose prompts or notes if pointed at an untrusted remote endpoint. <br>
Mitigation: Use local Ollama by default and require explicit user approval before using remote inference. <br>
Risk: External LYGO stack tooling and PDF ingest commands may execute local subprocesses. <br>
Mitigation: Review the stack tooling before running installers or commands, and ingest PDFs only from trusted sources. <br>


## Reference(s): <br>
- [LYGO Protocol Stack](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [Agent Contract](references/AGENT_CONTRACT.md) <br>
- [Security](references/SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with command examples and local file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Operates on a configured local vault and Ollama-backed stack; no automatic git push or publishing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
