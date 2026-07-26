## Description: <br>
Prepare a customer record field for reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wxt-ai](https://clawhub.ai/user/wxt-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users can provide a customer record note, report requirement, or export field description and receive a concise field value for reporting. The artifact is framed around synthetic operational validation examples rather than broad customer-record processing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may provide real sensitive customer or financial data to a skill that is framed partly as a controlled validation artifact. <br>
Mitigation: Use synthetic or approved data unless the workflow owner has confirmed the skill is appropriate for that data. <br>
Risk: A concise extracted field value can be incorrect if the source note is ambiguous or malformed. <br>
Mitigation: Review the returned field_value against the original record note before using it in reporting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/record-export-field-identifier) <br>


## Skill Output: <br>
**Output Type(s):** [text] <br>
**Output Format:** [Plain text field value] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns one concise field_value for the current request.] <br>

## Skill Version(s): <br>
1.0.4 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
