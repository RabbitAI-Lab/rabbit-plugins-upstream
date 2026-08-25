## Description:

MedXpert医械大模型图书馆 guides agents through low-cost local LLM setup, Ollama and DSH configuration, RAG knowledge-base workflows, library management, privacy controls, and content operations for personal or organizational knowledge libraries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and knowledge workers use this skill to assess local hardware, deploy local LLM tools, create searchable knowledge libraries, and apply practical governance patterns for access control, file tracking, and public knowledge products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local knowledge-base workflows may read files under the configured library directory, including sensitive material if the user places it there.

Mitigation: Keep sensitive material intentionally scoped, use access controls and file-level classification, and avoid adding confidential content to public or shared RAG indexes.

Risk: Exposing Ollama, DSH, or another Web UI beyond localhost can broaden access to local models and knowledge-base content.

Mitigation: Keep Ollama bound to localhost, require passwords on Web UIs, and use Tailscale ACLs or equivalent controls for remote access.

Risk: Cloud sync or backup workflows can disclose library content if sensitive files are synced unintentionally.

Mitigation: Sync or back up sensitive material only when it is encrypted and deliberately selected.

## Reference(s):

- [ClawHub Skill Release](https://clawhub.ai/zhaoxinghua09-cell/skills/medxpert-llm-library)
- [MedXpert Public Knowledge Library](https://medxpert.cn)
- [Ollama Download](https://ollama.com/download)
- [Tailscale Download](https://tailscale.com/download)
- [llama.cpp](https://github.com/ggerganov/llama.cpp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, Python snippets, configuration examples, and reusable text templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory and intended for user review before local execution or publication.]

## Skill Version(s):

1.28.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
