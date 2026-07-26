## Description: <br>
Memora Kb helps agents interact with a self-hosted personal knowledge base for document management, semantic search, AI-assisted Q&A, and knowledge graph exploration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zzlzzlzzl15](https://clawhub.ai/user/zzlzzlzzl15) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and knowledge workers use this skill to connect an agent to a Memora knowledge-base backend, search stored documents, retrieve AI-organized answers, list or inspect documents, and add new text or uploaded files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Private, regulated, or confidential knowledge-base content may be exposed through cloud LLM or embedding providers. <br>
Mitigation: Use localhost-only KB_API_BASE and local embedding or LLM settings when possible; add API keys only for trusted providers. <br>
Risk: External installation steps may run code outside the reviewed skill artifact. <br>
Mitigation: Inspect the external repository and install script before running manual installation commands. <br>
Risk: Web scraping can collect data from sources where collection is not permitted. <br>
Mitigation: Treat scraping as user-directed and scrape only sources the operator is allowed to collect. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zzlzzlzzl15/skills/memora-kb) <br>
- [Memora README](https://github.com/zzlzzlzzl15/Memora/blob/main/personal_knowledge_base/README.md) <br>
- [Memora repository](https://github.com/zzlzzlzzl15/Memora) <br>
- [Obsidian graph view](https://obsidian.md/) <br>
- [RAG-Anything reference](https://github.com/RAG-Anything/RAG-Anything) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Text, Files, Configuration] <br>
**Output Format:** [JSON responses from knowledge-base API commands, with text answers and source snippets when search_answer is used] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires KB_API_BASE for the target Memora backend; upload and create commands can add content to the connected knowledge base.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
