## Description: <br>
CAN (Clock Address Naming) helps agents create a verifiable content-addressed index for data flows by recording timestamp, content hash, and human-readable label entries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, independent users, enterprise teams, and automation workflows use this skill to tag agent outputs, API responses, files, or events with WHEN/WHERE/WHAT records for integrity checks, lookup, and audit trails. The artifact says it is not intended for real-time streaming data processing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Workflow metadata may be sent to xc.cx without clear privacy or retention details. <br>
Mitigation: Use the local three-field evaluation path for sensitive work, and avoid sending labels, timestamps, hashes, file-derived identifiers, callback URLs, or operational logs to xc.cx unless this exposure is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/can) <br>
- [CAN evaluate endpoint](https://xc.cx/can/evaluate) <br>
- [CAN log endpoint](https://xc.cx/can/log) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local three-field evaluations, endpoint request examples, audit-log guidance, and troubleshooting notes.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
