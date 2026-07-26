## Description: <br>
Self-Improving Agent gives agents a three-layer memory framework for session context, task digests, long-term lessons, failure review, memory compression, and reusable sub-skill extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jianghg01](https://clawhub.ai/user/jianghg01) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to add structured memory, failure review, historical lesson retrieval, and workflow-to-skill extraction behavior to a general-purpose agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent memory can store profile-like observations or sensitive lessons and re-inject them into future sessions. <br>
Mitigation: Decide where memory files are stored, require explicit consent for L2 and L3 writes, and review what is injected into future sessions. <br>
Risk: Skill-changing behavior can make durable changes to the agent's future behavior. <br>
Mitigation: Avoid granting skill-management or broad file-write access unless durable behavior changes are intended and reviewed. <br>


## Reference(s): <br>
- [Memory Schema](memory-schema.md) <br>
- [Review Templates](review-templates.md) <br>
- [Skill Extraction Protocol](skill-extraction.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration, Code] <br>
**Output Format:** [Markdown instructions and templates with optional JSON memory exports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or create persistent memory entries and skill drafts when the host agent provides storage or skill-management tools.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
