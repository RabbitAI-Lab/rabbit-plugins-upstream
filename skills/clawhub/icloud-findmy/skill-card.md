## Description: <br>
Query Find My locations and battery status for family devices via iCloud. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liamnichols](https://clawhub.ai/user/liamnichols) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and their agents use this skill to query authorized iCloud Find My devices for location, battery level, and charging status, then answer context or alert questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose precise Find My location and family-device status data. <br>
Mitigation: Use it only for devices and people the user is authorized to locate, and avoid covert or continuous monitoring. <br>
Risk: Apple IDs and iCloud sessions may be stored in local or workspace-accessible locations. <br>
Mitigation: Keep Apple IDs out of shared workspaces and rely on local user-controlled session storage. <br>
Risk: The artifact includes examples that parse location dictionaries with eval(). <br>
Mitigation: Replace eval()-based parsing with safe structured parsing or strict coordinate extraction. <br>


## Reference(s): <br>
- [PyiCloud project](https://github.com/picklepete/pyicloud) <br>
- [ClawHub skill page](https://clawhub.ai/liamnichols/skills/icloud-findmy) <br>
- [Publisher profile](https://clawhub.ai/user/liamnichols) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and natural-language responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the local icloud CLI from PyiCloud and an authorized Apple ID session.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
