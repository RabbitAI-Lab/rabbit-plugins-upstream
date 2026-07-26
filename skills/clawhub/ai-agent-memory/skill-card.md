## Description: <br>
Unlimited organized memory for your AI agent. Store, search, and organize projects, contacts, decisions, and knowledge across categories. Never lose context again. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[certainlogicai](https://clawhub.ai/user/certainlogicai) <br>

### License/Terms of Use: <br>
Business Source License 1.1 <br>


## Use Case: <br>
External users and developers use this skill to give an AI agent a persistent, local markdown memory system for projects, contacts, decisions, knowledge, and custom collections. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Files saved under ~/memory/ can persist private or sensitive notes on disk. <br>
Mitigation: Avoid storing passwords, API keys, financial identifiers, health records, regulated data, or unnecessary third-party personal details; delete local memory files when they are no longer needed. <br>
Risk: Syncing from built-in memory can copy personal context or stale information into persistent local files. <br>
Mitigation: Review anything copied from built-in memory before syncing and keep syncing explicit rather than automatic. <br>
Risk: Poor indexing or broad notes can make local memory hard to audit or remove later. <br>
Mitigation: Use clear categories, maintain INDEX.md files, and archive or delete old entries deliberately. <br>


## Reference(s): <br>
- [Memory Templates](memory-template.md) <br>
- [Organization Patterns](patterns.md) <br>
- [Setup - Memory](setup.md) <br>
- [Troubleshooting](troubleshooting.md) <br>
- [ClawHub skill page](https://clawhub.ai/certainlogicai/skills/ai-agent-memory) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown files and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates and updates local files under ~/memory/ when the agent follows the skill.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter and _meta.json say 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
