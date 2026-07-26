## Description: <br>
Smart Memory Manager helps agents manage short-term, long-term, and important memories with search, summarization, listing, clearing, saving, and loading workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users use this skill to give long-running agents a searchable memory layer for conversations, RAG workflows, customer-service assistants, and task agents that need retained context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided memories can be retained locally when save, load, or persist=true workflows are used. <br>
Mitigation: Avoid storing secrets, regulated data, or sensitive personal details; use a dedicated memory file path that can be reviewed and deleted. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/smart-memory-manager) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, configuration] <br>
**Output Format:** [Markdown guidance with TypeScript examples and structured action parameters] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to read, save, load, or persist local memory files when requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
