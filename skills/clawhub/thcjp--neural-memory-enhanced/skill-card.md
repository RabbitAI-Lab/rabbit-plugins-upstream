## Description: <br>
Neural Memory Enhanced helps agents store, recall, and relate local long-term memories through a SQLite-backed neural graph with spreading activation, typed synapses, lifecycle decay, contradiction detection, snapshots, and cross-brain transfer. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users can use this skill to add local, persistent memory workflows for long-running projects, cross-session context recall, decision history, causal tracing, relationship memory, and knowledge graph construction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed to automatically store and re-inject long-term conversation memories without clear user approval, scoping, or deletion controls. <br>
Mitigation: Use it only where long-term capture and later recall of conversation content is acceptable, and add explicit opt-in, review, deletion, and project scoping controls before routine use. <br>
Risk: Stored memories may include secrets, credentials, regulated data, customer data, or unrelated project context. <br>
Mitigation: Avoid using the skill with sensitive or regulated content unless strong data-handling rules are in place, and review stored memories before reuse or transfer. <br>
Risk: Cross-brain memory transfer can move context between projects and may introduce unwanted or conflicting memories. <br>
Mitigation: Filter transfers by type, tag, and date range, review reported conflicts, and keep separate brains for unrelated projects. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/neural-memory-enhanced) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with command examples and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local-memory records, recall results, activation paths, snapshot identifiers, and SQLite-backed memory operations through the referenced neural-memory tooling.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
