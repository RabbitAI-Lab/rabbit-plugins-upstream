## Description: <br>
Command-line helper for listing, inspecting, and managing objects, records, and lists in an Attio CRM workspace through the Attio API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[froemic](https://clawhub.ai/user/froemic) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and CRM operators use this skill to install and operate attio-cli, inspect workspace objects and lists, generate a Markdown workspace schema, and run common Attio API operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Attio API keys and generated workspace schema files can expose sensitive CRM data. <br>
Mitigation: Use a least-privileged Attio API key, keep credentials out of shared or committed dotfiles, and treat generated schema files as confidential. <br>
Risk: Create-record and add-list-entry examples can modify the target CRM workspace. <br>
Mitigation: Run write examples only when intentional, and review target object, list, and payload values before execution. <br>
Risk: The skill installs and runs an external attio-cli source. <br>
Mitigation: Inspect or pin the external source before installing it in a trusted workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/froemic/skills/attio-cli) <br>
- [Attio CLI repository](https://github.com/FroeMic/attio-cli) <br>
- [Attio API base URL](https://api.attio.com/v2) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Markdown, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and generated workspace schema output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate a workspace.schema.md file containing CRM object, list, attribute, and field-option details.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.json release version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
