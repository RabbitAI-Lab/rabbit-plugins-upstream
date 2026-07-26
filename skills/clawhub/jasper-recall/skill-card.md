## Description: <br>
Local retrieval-augmented generation system for AI agents using ChromaDB and sentence-transformers, supporting multi-agent shared memory and privacy controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[emberdesire](https://clawhub.ai/user/emberdesire) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use Jasper Recall to index local memory files, search past sessions semantically, and expose public-only recall flows for sandboxed or multi-agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent local memory can expose sensitive session history or private notes if configured too broadly. <br>
Mitigation: Review memory locations and sharing tags before indexing, run privacy checks before syncing public entries, and use public-only collections for sandboxed agents. <br>
Risk: HTTP recall access can expose private memories to untrusted callers if private queries are enabled or the server is bound outside localhost. <br>
Mitigation: Keep the server bound to localhost, avoid setting RECALL_ALLOW_PRIVATE for shared hosts, and require explicit review before external exposure. <br>
Risk: Auto-recall and shell command construction can introduce privacy leakage or command-injection exposure. <br>
Mitigation: Leave autoRecall disabled until command execution uses argument-array subprocess calls and only enable it with publicOnly in untrusted contexts. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/emberdesire/skills/jasper-recall) <br>
- [README](README.md) <br>
- [Multi-Agent Mesh Documentation](docs/MULTI-AGENT-MESH.md) <br>
- [Shared Agent Memory Spec](docs/SHARED-MEMORY-SPEC.md) <br>
- [npm Package](https://www.npmjs.com/package/jasper-recall) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended to help agents install, configure, search, index, and operate a local memory system.] <br>

## Skill Version(s): <br>
0.4.0 (source: server release evidence, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
