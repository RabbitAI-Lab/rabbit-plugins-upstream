## Description: <br>
Generate playbook YAML files for the intelligent outbound call platform through natural language guided conversation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[npufwb](https://clawhub.ai/user/npufwb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill to create outbound-call playbook YAML through a guided conversation covering scenarios, SOP phases, intents, constraints, and validation checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated playbook YAML may contain incorrect scenario logic, compliance constraints, or scripts before review. <br>
Mitigation: Review the generated YAML and validation checklist before importing it into the outbound call platform. <br>
Risk: The skill may create or update a local YAML file under playbooks/imported. <br>
Mitigation: Choose the display or copy-paste path when local file writes are not desired, and confirm the playbook_id before saving. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/npufwb/skills/playbook-generator) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [YAML playbook content with Markdown guidance and validation checklist] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write a YAML file under playbooks/imported or display the YAML for manual import.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
