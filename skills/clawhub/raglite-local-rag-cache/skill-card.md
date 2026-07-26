## Description: <br>
Local-first RAG cache: distill docs into structured Markdown, then index/query with Chroma + hybrid search (vector + keyword). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[virajsanghvi1](https://clawhub.ai/user/virajsanghvi1) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use RAGLite to condense local or private documents into structured Markdown, index them in Chroma, and query them with hybrid vector and keyword retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Setup installs RAGLite from a live GitHub main branch, so installed code can change between runs. <br>
Mitigation: Pin and audit the dependency before use, and review the install step before approving it. <br>
Risk: Indexing private documents can expose sensitive content to configured retrieval services or leave local cache artifacts. <br>
Mitigation: Confirm where the OpenClaw gateway and Chroma server run, use an explicit local or offline engine when needed, scope input folders narrowly, and protect generated output directories. <br>


## Reference(s): <br>
- [ClawHub RAGLite listing](https://clawhub.ai/virajsanghvi1/skills/raglite-local-rag-cache) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown artifacts, shell command output, and retrieval guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes structured Markdown summaries, optional node files, query results, and .raglite metadata in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
