## Description: <br>
Voyage AI CLI helps agents use the vai command-line tool for embeddings, reranking, MongoDB Atlas Vector Search storage and search, model listing, similarity comparison, bulk ingestion, demos, and concept guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mrlynn](https://clawhub.ai/user/mrlynn) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to generate and store embeddings, rerank results, manage Atlas Vector Search indexes, and run semantic retrieval workflows with the vai CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands may use API keys and MongoDB connection strings for external services. <br>
Mitigation: Use least-privilege Voyage AI and MongoDB credentials, and avoid entering real API keys directly into shell history. <br>
Risk: Embedding, reranking, storage, search, and ingest workflows may send document content or metadata to configured external services and persist data in MongoDB Atlas. <br>
Mitigation: Do not process sensitive documents unless that external processing and storage is intended and approved. <br>
Risk: Store, ingest, index create, and index delete workflows can change database state. <br>
Mitigation: Test these commands against non-production databases before using them with production collections or indexes. <br>


## Reference(s): <br>
- [Model Catalog](references/models.md) <br>
- [Vector Search Patterns](references/vector-search.md) <br>
- [voyageai-cli repository](https://github.com/mrlynn/voyageai-cli) <br>
- [MongoDB AI API](https://ai.mongodb.com/v1/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration notes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose commands that call external AI APIs or MongoDB Atlas and require VOYAGE_API_KEY, with MONGODB_URI needed for storage, search, index, ingest, and connectivity workflows.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release metadata and OpenClaw frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
