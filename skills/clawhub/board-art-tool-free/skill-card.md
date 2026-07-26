## Description: <br>
Helps individual users publish pixel art to a shared collaborative canvas, view and locate canvas work, manage colors and coordinates, and review personal publish history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to prepare and execute personal pixel-art canvas workflows, including publishing one artwork, viewing or locating canvas positions, managing color and coordinate data, and exporting personal history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad or mismatched instructions could cause the agent to act outside explicit pixel-art canvas tasks. <br>
Mitigation: Use the skill only when the user explicitly asks for pixel-art canvas work, and review the proposed action before execution. <br>
Risk: The workflow may publish, delete, import, reset, or export remote canvas content. <br>
Mitigation: Require user confirmation before any publish, delete, import, reset, or export action. <br>
Risk: A canvas service token may be required for publishing operations. <br>
Mitigation: Verify the actual command or endpoint before providing a service token, and keep credentials out of prompts, logs, and artifacts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/board-art-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, JSON, Configuration] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured status, result data, execution log, and error fields.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
