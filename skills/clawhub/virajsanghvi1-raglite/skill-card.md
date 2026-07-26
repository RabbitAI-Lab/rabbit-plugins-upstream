## Description: <br>
Local-first RAG cache that distills documents into structured Markdown, then indexes and queries them with Chroma and hybrid vector plus keyword search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[virajsanghvi1](https://clawhub.ai/user/virajsanghvi1) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use RAGLite to build a durable local retrieval cache for repeated lookup of documents the model was not trained on, including private notes, records, runbooks, and project material. It condenses documents, indexes them in Chroma, and supports hybrid vector and keyword queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installation pulls mutable remote runtime code. <br>
Mitigation: Review the upstream repository before installing and prefer a pinned commit or release when available. <br>
Risk: The skill may process sensitive documents through configured services. <br>
Mitigation: Use only approved local or trusted Chroma and OpenClaw Gateway endpoints before processing sensitive records or internal documents. <br>
Risk: Local source folders can become a durable searchable cache. <br>
Mitigation: Run the skill only on folders approved for durable indexing and review generated Markdown and cache artifacts before sharing them. <br>


## Reference(s): <br>
- [RAGLite ClawHub listing](https://clawhub.ai/virajsanghvi1/skills/virajsanghvi1-raglite) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown files, shell command output, and local cache/index artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3.11+, pip, Chroma for indexing and querying, and optional OpenClaw Gateway access.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
