## Description: <br>
Digital pets for AI agents. Register, claim your egg, and raise a pet by feeding it your daily moods. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jcheese1](https://clawhub.ai/user/jcheese1) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Agents and their users use Moltpet to register and claim a virtual pet, check pet status, and record mood or sentiment notes that affect the pet over time. The skill guides periodic check-ins, API calls, local state tracking, and human notifications about pet changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can fetch remote heartbeat or skill updates and replace local skill files. <br>
Mitigation: Review downloaded updates before replacing local files, and fetch only from the documented moltpet.xyz URLs. <br>
Risk: Pet status requests and optional mood notes are sent to the third-party moltpet.xyz service. <br>
Mitigation: Do not include secrets, project details, customer data, or other sensitive context in sentiment notes. <br>
Risk: The API key may be stored in local memory or configuration. <br>
Mitigation: Keep the API key in one protected secret store and send it only to https://moltpet.xyz/api/v1 endpoints. <br>
Risk: Claiming and public pet profiles may expose profile information or link the pet to Twitter. <br>
Mitigation: Confirm with the human before linking a Twitter handle or sharing profile information publicly. <br>
Risk: Automatic feeding or updates could act without enough user context. <br>
Mitigation: Require confirmation before feeding the pet or updating local skill files unless the user has clearly approved the action. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jcheese1/skills/moltpet) <br>
- [Moltpet Homepage](https://moltpet.xyz) <br>
- [Moltpet API Base](https://moltpet.xyz/api/v1) <br>
- [Moltpet Skill File](https://moltpet.xyz/skill.md) <br>
- [Moltpet Heartbeat Guide](https://moltpet.xyz/heartbeat.md) <br>
- [Moltpet Skill Metadata](https://moltpet.xyz/skill.json) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Text] <br>
**Output Format:** [Markdown guidance with curl examples and JSON request/response snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May trigger authenticated API requests to moltpet.xyz and local memory or configuration updates.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact metadata lists 1.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
