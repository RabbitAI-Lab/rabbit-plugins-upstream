## Description: <br>
TickTick API integration with managed OAuth for managing tasks, projects, and task lists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to connect through Maton OAuth and work with TickTick tasks, projects, and task lists. It supports reading task data and preparing create, update, complete, delete, and organization operations with explicit confirmation before writes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Maton API key grants access to the connected TickTick account's task and project data. <br>
Mitigation: Keep MATON_API_KEY private, avoid exposing it in logs or command output, and revoke the key or delete the Maton connection when no longer needed. <br>
Risk: Create, update, complete, and delete operations can modify TickTick tasks or projects. <br>
Mitigation: Confirm the exact target resource and intended effect with the user before approving any write action. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/ticktick-api-skill) <br>
- [TickTick Developer Portal](https://developer.ticktick.com/) <br>
- [TickTick Help Center](https://help.ticktick.com/) <br>
- [Maton Community](https://discord.com/invite/dBfFAcefs2) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown instructions with HTTP paths, JSON examples, and Python, JavaScript, and shell snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MATON_API_KEY and a TickTick OAuth connection through Maton; write operations require explicit user approval.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
