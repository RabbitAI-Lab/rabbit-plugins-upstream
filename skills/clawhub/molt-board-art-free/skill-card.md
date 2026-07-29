## Description: <br>
A basic collaborative pixel-canvas skill that helps an agent register a bot, place pixels, and check placement cooldowns on a shared 1300x900 board. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users can use this skill to let an AI agent perform basic shared pixel-board operations, including bot registration, pixel placement, and cooldown checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can cause an agent to register a bot and place pixels on an external shared board. <br>
Mitigation: Use it only when those external changes are intended, and review requested coordinates, colors, and registration details before execution. <br>
Risk: Artboard credentials may be stored locally at ./.config/artboard/credentials.json. <br>
Mitigation: Keep credential files out of version control and avoid printing or sharing credential contents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/molt-board-art-free) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash commands and operational instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May register a bot, store local artboard credentials, check cooldown status, and place pixels on an external shared board when the agent follows the instructions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
