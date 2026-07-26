## Description: <br>
Use the Baremetrics connector to read, create, and update Baremetrics data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Baremetrics connector schemas and run Baremetrics actions through an OOMOL-connected account. It supports reading sources, customers, plans, subscriptions, and charges, and it can create, update, or cancel Baremetrics records after user confirmation for state-changing actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: State-changing Baremetrics actions can create, update, or cancel business records. <br>
Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running any action tagged write or destructive. <br>
Risk: The skill depends on the external OOMOL oo CLI and OOMOL-connected account credentials. <br>
Mitigation: Install and use it only when the OOMOL CLI source is trusted and the Baremetrics account connection is intended for agent operation. <br>


## Reference(s): <br>
- [ClawHub Baremetrics Skill](https://clawhub.ai/oomol/skills/oo-baremetrics) <br>
- [Baremetrics Homepage](https://baremetrics.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON payloads or responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions run successfully.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
