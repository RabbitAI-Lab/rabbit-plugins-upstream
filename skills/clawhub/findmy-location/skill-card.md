## Description: <br>
Find My Location tracks a shared contact via Apple Find My and returns location context such as address, city, home/work/out status, and screenshot-backed vision fallback when needed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[poiley](https://clawhub.ai/user/poiley) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External macOS users can use this skill to query an Apple Find My shared contact and receive a human-readable or JSON summary of the contact's current location context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose precise shared-contact location data. <br>
Mitigation: Use it only for contacts who knowingly share location through Apple Find My, and avoid retaining or redistributing location output beyond the task. <br>
Risk: The skill requires screen-reading and UI-control permissions, and the optional Hammerspoon click server can broaden local UI-control exposure. <br>
Mitigation: Grant permissions only on a trusted macOS account, avoid or restrict the localhost click server, close sensitive windows before running, and delete temporary screenshots after use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/poiley/skills/findmy-location) <br>
- [peekaboo screen reading CLI](https://github.com/steipete/peekaboo) <br>
- [Hammerspoon](https://www.hammerspoon.org/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files, Configuration] <br>
**Output Format:** [Human-readable text or JSON with an optional screenshot file path] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May indicate that vision analysis is needed for a captured map screenshot.] <br>

## Skill Version(s): <br>
1.1.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
