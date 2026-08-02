## Description: <br>
Nutrient DWS (nutrient.io) connector skill for reading, creating, updating, and deleting data through the OOMOL oo CLI instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Nutrient DWS connector schemas, run supported actions, estimate Build API credit usage, manage restricted JWT auth tokens, and retrieve sanitized account information through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate the user's connected Nutrient DWS account through OOMOL. <br>
Mitigation: Confirm the intended account and requested action before use, especially when a command changes account state. <br>
Risk: The create_auth_token and delete_auth_token actions can create or revoke JWT access. <br>
Mitigation: Inspect the live action schema, review the exact payload or token ID, and get explicit user confirmation before running either action. <br>


## Reference(s): <br>
- [Nutrient DWS homepage](https://www.nutrient.io/api/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [State-changing connector actions require user confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
