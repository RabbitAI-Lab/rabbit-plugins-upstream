## Description: <br>
Memora Knowledge Base helps agents manage, search, query, upload, and create documents through a configured Memora knowledge-base API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zzlzzlzzl15](https://clawhub.ai/user/zzlzzlzzl15) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users use this skill to connect an agent to a Memora backend for document search, AI-assisted answers, document listing and details, file upload, and text-document creation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Documents, search queries, created notes, and generated prompts may leave the local machine or reach cloud AI providers depending on the configured backend. <br>
Mitigation: Use only a trusted KB_API_BASE endpoint and verify provider settings, privacy mode, backups, and deletion behavior before processing sensitive material. <br>
Risk: The artifact describes fully private local use, while security evidence flags remote API, external AI, and web access behavior. <br>
Mitigation: Treat privacy claims as deployment-dependent and review the actual Memora backend configuration before installation or production use. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/zzlzzlzzl15/skills/memora-knowledge-base) <br>
- [Memora documentation](https://github.com/zzlzzlzzl15/Memora/blob/main/personal_knowledge_base/README.md) <br>
- [Memora project](https://github.com/zzlzzlzzl15/Memora) <br>
- [RAG-Anything reference](https://github.com/RAG-Anything/RAG-Anything) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [JSON responses and Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires KB_API_BASE to point to a trusted Memora API endpoint.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
