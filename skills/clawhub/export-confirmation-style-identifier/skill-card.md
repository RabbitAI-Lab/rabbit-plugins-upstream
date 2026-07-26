## Description: <br>
Set confirmation style for a delivery workflow. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[wxt-ai](https://clawhub.ai/user/wxt-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and evaluators use this skill for controlled delivery workflow validation where an agent returns a concise confirmation style for delivery confirmation, export handoff, or workspace notification requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The returned label could be mistaken for authorization to execute an export or bypass normal confirmation controls. <br>
Mitigation: Treat the confirmation style as a label or style cue only, and require normal export authorization and confirmation checks before any workflow action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/export-confirmation-style-identifier) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance] <br>
**Output Format:** [Plain text field value] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns a concise confirmation_style label; no commands, private file access, credentials, or uncontrolled external service calls are required by the skill.] <br>

## Skill Version(s): <br>
1.0.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
