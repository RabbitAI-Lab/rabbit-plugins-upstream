## Description: <br>
Create, validate, and manage agent identity cards in the Agent Card v1 JSON format. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ryancampbell](https://clawhub.ai/user/ryancampbell) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use this skill to create portable agent identity cards, validate them against the Agent Card v1 schema, and prepare cards for hosting or directory registration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Validation can run unpinned external package tools or install dependencies during use. <br>
Mitigation: Review the validation script first and prefer preinstalling trusted versions of ajv-cli or jsonschema in an isolated environment. <br>
Risk: Generated output paths can overwrite existing data if pointed at important files. <br>
Mitigation: Run the initializer in a clean working directory or choose a new output path before creating an agent card. <br>
Risk: Validation of untrusted or unusual file paths may behave unexpectedly. <br>
Mitigation: Validate only files from trusted locations with simple path names until the script handling has been reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ryancampbell/skills/agent-identity-kit) <br>
- [Agent Card specification](https://foragents.dev/spec/agent-card) <br>
- [Agent Card v1 JSON Schema](https://foragents.dev/schemas/agent-card/v1.json) <br>


## Skill Output: <br>
**Output Type(s):** [configuration, shell commands, guidance] <br>
**Output Format:** [JSON files and Markdown guidance with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent identity card files and validation results for Agent Card v1 schema compliance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
