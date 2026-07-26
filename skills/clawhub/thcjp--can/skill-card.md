## Description: <br>
Can helps agents create verifiable content addresses for data-flow events using timestamp, content-hash, and human-readable name fields. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Can to label content, verify integrity, find records by hash, and maintain append-only audit trails for agent outputs, API responses, files, and messages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill mixes a local audit-log workflow with instructions to send records, hashes, timestamps, and callback URLs to an external service without enough privacy or retention disclosure. <br>
Mitigation: Review before installing; for sensitive material, prefer the local self-evaluation and hashing path, and only use the external service when its retention and visibility behavior is acceptable. <br>
Risk: The external evaluation and log endpoints may expose submitted metadata or make audit records visible outside the user's environment. <br>
Mitigation: Avoid sending confidential records, labels, hashes, timestamps, or callback URLs to the service unless the publisher and endpoint are trusted for that data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/can) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Clawdis homepage](https://skillhub.cn) <br>
- [CAN evaluate endpoint](https://xc.cx/can/evaluate) <br>
- [CAN log endpoint](https://xc.cx/can/log) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline JSON and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include CAN or NOT status results, parsed summaries, content hashes, timestamps, audit-log entries, error codes, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
