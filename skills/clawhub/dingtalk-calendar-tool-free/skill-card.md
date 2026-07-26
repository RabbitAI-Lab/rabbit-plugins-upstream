## Description: <br>
Uses the mcporter CLI to help an agent manage DingTalk calendar workflows, including creating and updating events, checking schedules and free/busy status, booking meeting rooms, and searching contacts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent operate basic DingTalk calendar and meeting-room workflows from natural language prompts. It is aimed at individual and lightweight use cases rather than batch or team-scale calendar administration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, delete, or book calendar and meeting-room resources through CLI-mediated DingTalk workflows. <br>
Mitigation: Require explicit human review before write actions such as creating, updating, deleting, or booking resources. <br>
Risk: Security evidence flags unclear trigger scope and incomplete privacy disclosure for what may be sent to DingTalk, callback endpoints, or local caches. <br>
Mitigation: Avoid broad data-analysis prompts as triggers, verify DingTalk and callback URLs, and confirm data handling with the publisher before deployment. <br>
Risk: The workflow depends on the external mcporter package and configured DingTalk endpoints. <br>
Mitigation: Verify the mcporter package source and configured DingTalk URLs before granting an agent execution access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/dingtalk-calendar-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return status, result data, logs, and errors from mcporter-mediated DingTalk calendar or contact operations.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
