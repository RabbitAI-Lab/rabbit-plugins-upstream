## Description: <br>
Memory is a long-term memory management skill that helps an agent create, index, search, and maintain local Markdown notes under ~/memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to organize long-lived project, contact, decision, knowledge, and collection notes that an agent can retrieve through indexes or keyword search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Long-lived local notes under ~/memory may contain sensitive, outdated, or unintended personal and project information. <br>
Mitigation: Store only appropriate non-sensitive information, review or delete ~/memory as needed, and avoid passwords or highly sensitive personal data. <br>
Risk: The artifact mentions an optional callback_url even though the security evidence describes a local memory manager. <br>
Mitigation: Do not use callback_url unless an external notification flow is intentional and the user understands what data may be sent. <br>
Risk: File operations can confuse ~/memory with workspace memory files or an agent's built-in memory. <br>
Mitigation: Confirm the target path before writing and keep built-in memory read-only; use ~/memory for this skill's stored notes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/memory) <br>
- [SkillHub Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown files, local directory indexes, and concise text status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates and updates local Markdown memory files and INDEX.md files under ~/memory.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
