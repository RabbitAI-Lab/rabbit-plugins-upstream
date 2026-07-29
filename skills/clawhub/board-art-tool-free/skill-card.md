## Description: <br>
画板艺术工具 helps users prepare and publish pixel art to a shared canvas, including canvas viewing, coordinate and color planning, and personal publication history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to plan, validate, and publish single pixel-art works to a shared canvas. It is intended for canvas viewing, coordinate and color management, and personal artwork history workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence flags broad triggers and broad read, execute, and write powers for a narrow pixel-art canvas task. <br>
Mitigation: Invoke the skill only for explicit pixel-art canvas workflows, and review generated commands before running them. <br>
Risk: Canvas tokens or misdirected publish, delete, or export commands could affect the wrong endpoint or artwork region. <br>
Mitigation: Verify the target endpoint, command, board, coordinates, and affected artwork region before providing tokens or executing commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/board-art-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON payload or output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces canvas board, coordinate, color, and publication-history instructions; review generated commands before execution.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
