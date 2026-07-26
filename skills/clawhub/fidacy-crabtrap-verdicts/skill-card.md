## Description: <br>
Adds independent, signed Fidacy verdicts to Brex CrabTrap audits, enabling publicly verifiable proof without altering CrabTrap's enforcement flow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fidacy](https://clawhub.ai/user/fidacy) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and engineering teams that run or evaluate CrabTrap use this skill to add signed Fidacy verdicts in observe mode, so agent audit decisions can be verified by external counterparties such as vendors, insurers, auditors, regulators, or dispute reviewers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow depends on the external @fidacy/crabtrap npm package and Fidacy service. <br>
Mitigation: Confirm that the organization trusts the package and service before installing or connecting production audit streams. <br>
Risk: CrabTrap audit events may contain sensitive data when sent for Fidacy assessment. <br>
Mitigation: Review the data flow and avoid sending sensitive audit event content unless that transfer is acceptable for the organization. <br>
Risk: The integration requires a Fidacy engine API key with assess:write scope. <br>
Mitigation: Store the key in the organization's normal secrets manager and limit access to the deployment components that need assessment writes. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/fidacy/skills/fidacy-crabtrap-verdicts) <br>
- [Fidacy signup](https://app.fidacy.com/signup) <br>
- [Fidacy public JWKS](https://api.fidacy.com/.well-known/jwks.json) <br>
- [Fidacy verifier](https://fidacy.com/verify) <br>
- [Fidacy comparison](https://fidacy.com/comparison) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes guidance to install @fidacy/crabtrap, connect it to a CrabTrap SSE event stream, and verify signed verdicts with Fidacy tooling.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
