## Description: <br>
Identify the project handle from an intake note. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wxt-ai](https://clawhub.ai/user/wxt-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Project delivery teams use this skill to extract a concise project code from client briefs, delivery notes, or project updates supplied in the current request. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided intake notes may contain sensitive client or project details. <br>
Mitigation: Only provide note text that is acceptable for the normal agent workflow, and avoid pasting sensitive client details unless that use is approved. <br>
Risk: A concise project code extracted from ambiguous notes may be incorrect. <br>
Mitigation: Review the returned project_code before using it in delivery tracking, routing, or other operational records. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/project-code-notes-identifier) <br>
- [Publisher profile](https://clawhub.ai/user/wxt-ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance] <br>
**Output Format:** [Structured text field containing a concise project code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces the project_code value from the user-provided note.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
