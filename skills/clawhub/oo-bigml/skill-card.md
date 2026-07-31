## Description: <br>
BigML enables agents to operate BigML through the OOMOL oo CLI for reading, creating, updating, and deleting BigML resources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to manage BigML models and predictions through an OOMOL-connected BigML account, including listing resources, retrieving model and prediction details, creating predictions, and deleting prediction resources with confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: State-changing BigML actions can create prediction resources or otherwise alter account state. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write. <br>
Risk: The delete_prediction action permanently removes a stored BigML prediction resource. <br>
Mitigation: Get explicit approval for the target prediction before running destructive actions. <br>
Risk: Incorrect request payloads can send unintended data or fail against BigML connector actions. <br>
Mitigation: Fetch the live connector schema before constructing action payloads and validate JSON inputs against that schema. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-bigml) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [BigML homepage](https://bigml.com/) <br>
- [OOMOL BigML connection settings](https://console.oomol.com/app-connections?provider=bigml) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector responses as JSON when commands are run with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
