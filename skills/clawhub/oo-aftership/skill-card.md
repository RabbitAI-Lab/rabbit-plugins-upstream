## Description: <br>
AfterShip lets an agent operate shipment tracking and courier workflows through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and support teams use this skill to inspect and manage AfterShip tracking records and courier data through the oo CLI while relying on live connector schemas. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, complete, retrack, or delete AfterShip tracking records. <br>
Mitigation: Confirm the exact action, target tracking record, payload, and expected effect with the user before running write or destructive commands. <br>
Risk: The skill depends on the oo CLI and an OOMOL-connected AfterShip account. <br>
Mitigation: Run installer, login, or connection setup steps only when needed and only when the user trusts OOMOL for the connector setup. <br>
Risk: Connector input and output schemas may change. <br>
Mitigation: Inspect the live connector schema before building each payload. <br>


## Reference(s): <br>
- [AfterShip homepage](https://www.aftership.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aftership) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands inspect connector schemas and may execute read, write, or destructive AfterShip actions with user confirmation for state changes.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
