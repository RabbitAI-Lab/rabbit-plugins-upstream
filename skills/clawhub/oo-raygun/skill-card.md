## Description: <br>
Raygun lets agents operate a Raygun account through OOMOL's connector for reading applications, deployments, and crash reporting data and managing deployments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Raygun applications, deployments, and crash reporting error groups, and to create, update, or delete deployment records after explicit confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The connector can create, update, or delete Raygun deployment records. <br>
Mitigation: Confirm the exact target, payload, and expected effect with the user before running any write or destructive action. <br>
Risk: The OOMOL connector acts on the user's connected Raygun account. <br>
Mitigation: Review the Raygun scopes on the OOMOL connection and install the skill only when that account access is intended. <br>
Risk: Raygun connector action schemas may change over time. <br>
Mitigation: Inspect the live action schema before constructing payloads so requests match the current contract. <br>


## Reference(s): <br>
- [Raygun Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-raygun) <br>
- [Raygun Homepage](https://raygun.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads; connector responses are JSON when --json is used.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires live schema inspection before each action; write and destructive actions require explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
