## Description: <br>
Use this skill to search and read Amplitude analytics data through an OOMOL-connected Amplitude account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to query Amplitude event segmentation, user activity, visible events, and user search through the oo CLI after connecting an Amplitude account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill operates against an external Amplitude account and can return account analytics data in command output. <br>
Mitigation: Review the external service access before use and grant only the Amplitude permissions needed for the task. <br>
Risk: Payloads built without the current connector schema can fail or query unintended data. <br>
Mitigation: Inspect the live action schema with `oo connector schema` before constructing each `oo connector run` payload. <br>
Risk: Future write or destructive connector actions could change or remove Amplitude data. <br>
Mitigation: Confirm the exact target, payload, and effect with the user before running any action tagged `[write]` or `[destructive]`. <br>


## Reference(s): <br>
- [ClawHub Amplitude Skill](https://clawhub.ai/oomol/skills/oo-amplitude) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Amplitude](https://amplitude.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may include JSON results from the oo CLI with data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
