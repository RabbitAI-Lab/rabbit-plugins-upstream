## Description: <br>
Create, list, update, and record Fulcra annotations through the Fulcra Life API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arc-claw-bot](https://clawhub.ai/user/arc-claw-bot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to create reusable Fulcra annotation definitions and record user-approved moments, booleans, numeric values, and scale ratings from agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Fulcra notes, health or behavior logs, timestamps, values, and tags may contain private user data. <br>
Mitigation: Keep private records and credentials out of chat and logs, send device authorization details only through the trusted user channel, and expose only the minimal fields needed for confirmation. <br>
Risk: Annotation writes can create or record user data in a Fulcra account. <br>
Mitigation: Confirm writes explicitly, use dry-run or list commands before changes, and trust success only after readback verification. <br>
Risk: The security review notes documentation inconsistencies around update and delete workflows. <br>
Mitigation: Prefer the bundled list, create, record, and recent helper path, and avoid update or delete guidance until the publisher makes that workflow consistent. <br>


## Reference(s): <br>
- [Fulcra Annotations on ClawHub](https://clawhub.ai/arc-claw-bot/skills/fulcra-annotations) <br>
- [Fulcra Annotation API Notes](artifact/references/api-notes.md) <br>
- [Fulcra API Base](https://api.fulcradynamics.com) <br>
- [Fulcra OpenAPI Document](https://api.fulcradynamics.com/openapi.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON script responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3.11 or newer, uv, an authenticated Fulcra account, and network access to https://api.fulcradynamics.com.] <br>

## Skill Version(s): <br>
1.0.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
