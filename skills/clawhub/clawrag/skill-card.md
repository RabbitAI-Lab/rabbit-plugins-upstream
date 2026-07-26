## Description: <br>
Self-hosted RAG engine with hybrid semantic and keyword search, document ingestion, local privacy, and OpenClaw integration through Docker and MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[2dogsandanerd](https://clawhub.ai/user/2dogsandanerd) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to connect OpenClaw to a self-hosted ClawRAG instance for local document ingestion, retrieval, citations, and memory workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup runs third-party Docker images, compose configuration, and an npm MCP package. <br>
Mitigation: Install only after trusting the ClawRAG GitHub repository, npm package, and Docker images; review the compose file and .env before running. <br>
Risk: Document indexing or optional cloud API keys could expose documents or document-derived content beyond the intended local scope. <br>
Mitigation: Use a narrow DOCS_DIR containing only documents intended for indexing, and avoid cloud API keys unless sending document-derived content to that provider is acceptable. <br>


## Reference(s): <br>
- [ClawRAG Full Docs](https://github.com/2dogsandanerd/ClawRag#readme) <br>
- [ClawRAG Issues](https://github.com/2dogsandanerd/ClawRag/issues) <br>
- [@clawrag/mcp-server Package](https://www.npmjs.com/package/@clawrag/mcp-server) <br>
- [ClawHub Skill Page](https://clawhub.ai/2dogsandanerd/skills/clawrag) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and configuration steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance assumes Docker, Docker Compose, OpenClaw, and a reachable local ClawRAG service.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
