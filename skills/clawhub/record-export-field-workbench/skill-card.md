## Description: <br>
Assemble a reporting export row. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wxt-ai](https://clawhub.ai/user/wxt-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and reporting teams use this skill to turn an approved cell_value supplied in the current request into a concise exported_cell for a reporting export row. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unapproved or unintended input could be formatted into a reporting export cell. <br>
Mitigation: Use only approved cell_value input that the user intentionally provides in the current request. <br>
Risk: The exported cell could be copied into reports without review. <br>
Mitigation: Review exported_cell before adding it to downstream reporting exports. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/record-export-field-workbench) <br>


## Skill Output: <br>
**Output Type(s):** [text] <br>
**Output Format:** [Concise text field value] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces the exported_cell field from the user-supplied cell_value.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
