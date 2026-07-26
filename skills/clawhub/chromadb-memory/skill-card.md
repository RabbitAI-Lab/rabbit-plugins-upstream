## Description: <br>
Provides self-hosted long-term memory for agents by embedding user messages with local Ollama and retrieving relevant ChromaDB memories for automatic or manual recall. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msensintaffar](https://clawhub.ai/user/msensintaffar) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to give an agent self-hosted long-term memory. It supports automatic recall before each agent turn and manual semantic search over an indexed ChromaDB collection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic memory recall can add stored sensitive information to agent context. <br>
Mitigation: Avoid indexing secrets or sensitive documents, periodically review or delete stored memories, and set autoRecall to false when manual search is preferred. <br>
Risk: Exposed ChromaDB or Ollama endpoints can leak memory data or embedding requests. <br>
Mitigation: Keep ChromaDB and Ollama local or on a trusted private network. <br>
Risk: A floating ChromaDB Docker image can introduce unexpected behavior changes. <br>
Mitigation: Pin the ChromaDB Docker image version instead of using latest. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/msensintaffar/skills/chromadb-memory) <br>
- [Artifact README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Injected context text, Markdown guidance, JSON configuration, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May add retrieved ChromaDB memories to agent context; defaults to three auto-recall results above the configured minimum score.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release evidence; artifact files report 1.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
