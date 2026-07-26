## Description: <br>
Control, organize, diagnose, design, personalize, and answer product knowledge questions for a Yeelight smart home. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yeelight](https://clawhub.ai/user/yeelight) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and smart-home operators use this skill to control, configure, diagnose, and personalize Yeelight homes through the local Yeelight runtime. It supports device and group control, rooms, scenes, automations, lighting design, product knowledge, recommendations, and Yeelight-domain memory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control and configure a user's smart home through the local Yeelight runtime. <br>
Mitigation: Install it only when smart-home control is intended, rely on runtime validation, and review destructive or permission-sensitive confirmations before execution. <br>
Risk: Authentication material may be needed for Yeelight account access. <br>
Mitigation: Keep login and token handling inside the yeelight-home CLI and do not paste secrets into chat. <br>
Risk: Explicit Yeelight preferences and operation lessons may be stored locally by the runtime. <br>
Mitigation: Store only explicit Yeelight-domain preferences through the runtime and disclose when memory or lessons are saved. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/yeelight/skills/yeelight-smart-home) <br>
- [Reference Router](references/README.md) <br>
- [Device Control](references/device-control.md) <br>
- [Home Room Area](references/home-room-area.md) <br>
- [Groups](references/groups.md) <br>
- [Scenes](references/scenes.md) <br>
- [Automations](references/automations.md) <br>
- [Lighting Design](references/lighting-design.md) <br>
- [Product Knowledge](references/product-knowledge.md) <br>
- [Safety And Confirmation](references/safety-and-confirmation.md) <br>
- [Runtime Status And Errors](references/runtime-status-and-errors.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown or concise text, with shell commands or configuration details when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runtime-backed responses should report actual success, partial completion, clarification, authentication requirements, blocked actions, or safe alternatives.] <br>

## Skill Version(s): <br>
0.1.14 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
