## Description: <br>
Memory System gives agents a structured method for storing, retrieving, injecting, and maintaining layered long-term memory across cloud, local, and workspace scopes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to give an agent repeatable guidance for deciding what to remember, where to store it, when to retrieve it, and how to maintain or remove stale memory. It is most relevant for workflows that need persistent preferences, project conventions, or reusable knowledge. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can shape agent behavior around persistent user or project memory without clear consent or rollback controls. <br>
Mitigation: Require explicit user confirmation before writing, injecting, merging, archiving, or deleting memory, and keep reviewable records of memory changes. <br>
Risk: Long-term memory may capture secrets, credentials, regulated personal data, or sensitive project details. <br>
Mitigation: Do not store sensitive data in memory entries; review memory content before persistence and periodically delete or redact inappropriate entries. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/wangjiaocheng/memory-system) <br>
- [Memory Catalog](artifact/references/memory-catalog.md) <br>
- [Memory Requirements](artifact/references/memory-requirements.md) <br>
- [Memory Exemplars](artifact/references/exemplars.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with structured memory records and reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to create, retrieve, inject, merge, archive, or delete memory entries across cloud, local, and workspace scopes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
