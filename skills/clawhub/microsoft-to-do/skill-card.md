## Description: <br>
Microsoft To Do API integration with managed OAuth for managing task lists, tasks, checklist items, and linked resources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent read, create, update, and delete Microsoft To Do task lists, tasks, checklist items, and linked resources through Maton-managed OAuth. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Maton API key to access the connected Microsoft To Do account. <br>
Mitigation: Install only when Maton is trusted, store MATON_API_KEY as a secret, and revoke the key when it is no longer needed. <br>
Risk: Create, update, and delete operations can change task lists, tasks, checklist items, linked resources, or OAuth connections. <br>
Mitigation: Require explicit user confirmation of the target resource and intended effect before executing write or delete requests. <br>
Risk: Multiple Microsoft To Do connections can cause actions to run against the wrong account. <br>
Mitigation: Use the Maton-Connection header when multiple accounts are connected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/microsoft-to-do) <br>
- [Microsoft To Do API overview](https://learn.microsoft.com/en-us/graph/api/resources/todo-overview) <br>
- [todoTaskList resource](https://learn.microsoft.com/en-us/graph/api/resources/todotasklist) <br>
- [todoTask resource](https://learn.microsoft.com/en-us/graph/api/resources/todotask) <br>
- [checklistItem resource](https://learn.microsoft.com/en-us/graph/api/resources/checklistitem) <br>
- [linkedResource resource](https://learn.microsoft.com/en-us/graph/api/resources/linkedresource) <br>
- [Maton account](https://maton.ai) <br>
- [Maton settings](https://maton.ai/settings) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with inline bash, Python, JavaScript, HTTP, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and a connected Microsoft To Do OAuth account through Maton.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
