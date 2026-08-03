## Description: <br>
Hippocampus Memory Engine helps agents maintain an external memory knowledge base, unify scattered memories for retrieval, generate visualizations, and sync memory outputs to Obsidian or GitHub-related destinations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wzx11223344](https://clawhub.ai/user/wzx11223344) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to build and maintain a local long-term memory workflow for agent conversations, knowledge files, retrieval, visualization, and Obsidian-oriented exports. It is most relevant when an agent needs to consolidate distributed memory sources and reuse them across later tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can cause agents to store conversation content and local memory files into a long-term knowledge base. <br>
Mitigation: Review what content will be persisted before running memory ingest or sync commands, and avoid storing sensitive or unnecessary personal data. <br>
Risk: The full sync workflow can clear and rebuild memory layers and exports. <br>
Mitigation: Keep backups of the knowledge base and prefer incremental sync for routine updates unless a full rebuild is intentionally needed. <br>
Risk: The skill references hardcoded local paths and exports to Obsidian or GitHub-related outputs. <br>
Mitigation: Confirm local paths and destination repositories or vaults before executing commands that write or export memory data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wzx11223344/skills/hippocampus-memory-engine) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, Python snippets, and configuration-oriented instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct an agent to persist, rebuild, export, or retrieve local memory data when the user requests memory maintenance.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
