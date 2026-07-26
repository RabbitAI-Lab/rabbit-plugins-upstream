## Description: <br>
Manage vector storage and similarity search using TOS Vectors service. Use when working with embeddings, semantic search, RAG systems, recommendation engines, or when the user mentions vector databases, similarity search, or TOS Vectors operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jneless](https://clawhub.ai/user/jneless) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to configure and operate Volcengine TOS Vectors for vector buckets, indexes, batch vector operations, similarity search, RAG retrieval, and recommendation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide uploads or indexing of vector data and metadata to a remote TOS Vectors service. <br>
Mitigation: Use least-privilege or test credentials and avoid indexing confidential raw content unless approved. <br>
Risk: The skill includes delete operations for vectors, indexes, and buckets. <br>
Mitigation: Confirm the exact bucket, index, and vector targets before running deletion commands. <br>
Risk: RAG examples may send retrieved context to the configured LLM provider. <br>
Mitigation: Use approved LLM providers and review retrieved context for sensitive data before generation. <br>


## Reference(s): <br>
- [TOS Vectors API Reference](artifact/REFERENCE.md) <br>
- [TOS Vectors Workflows](artifact/WORKFLOWS.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Python examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include executable examples that require TOS credentials and target Volcengine TOS Vectors resources.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
