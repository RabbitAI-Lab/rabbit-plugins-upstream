## Description: <br>
Guides agents through ingesting external document, note, and shared-file knowledge bases into vector databases such as ChromaDB, Pinecone, Weaviate, Qdrant, or Milvus, including prescan, exclusions, batching, index validation, and recovery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[william202404](https://clawhub.ai/user/william202404) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill to prepare, run, and verify knowledge-base ingestion into a selected vector database after confirming the source folder and backend. It is suited to syncing new folders, scheduled ingestion, rebuilding degraded indexes, and recovery after ingestion failures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The ingestion script is not bundled with this artifact. <br>
Mitigation: Review the separately obtained script before execution and confirm it matches the documented interface. <br>
Risk: The selected knowledge-base folder controls what content is indexed. <br>
Mitigation: Verify KB_DIR points only to content intended for ingestion before running any ingestion command. <br>
Risk: Cloud vector database backends may transmit indexed content and require API keys. <br>
Mitigation: Confirm the VECTOR_DB backend, protect credentials, and approve cloud data handling before ingestion. <br>


## Reference(s): <br>
- [Knowledge Base Ingestion on ClawHub](https://clawhub.ai/william202404/skills/knowledge-base-ingestion) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompts for user confirmation before ingestion and reports validation results after indexing.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence; artifact frontmatter reports 3.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
