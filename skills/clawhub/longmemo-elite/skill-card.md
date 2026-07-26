## Description: <br>
Longmemo Elite helps agents maintain long-term workspace memory across sessions using write-ahead logging, hybrid retrieval, tiered storage, and cost controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to set up durable memory practices for cross-session project work, multi-agent collaboration, preference retention, and recall of prior decisions or lessons. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Conversation-derived memory may persist private, regulated, or secret information in workspace files. <br>
Mitigation: Do not store secrets, regulated data, or private user details, and review memory files before committing or sharing a repository. <br>
Risk: Optional cloud backup and automatic extraction can sync or derive memory through third-party services. <br>
Mitigation: Keep cloud backup and automatic extraction disabled unless the provider and data types have been explicitly approved. <br>
Risk: The skill can encourage agents to create and maintain durable memory records without enough user control. <br>
Mitigation: Install only when durable workspace memory is desired, and require human review of retained memory records. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/longmemo-elite) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with JSON configuration examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update workspace memory files and configuration when used by an agent.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
