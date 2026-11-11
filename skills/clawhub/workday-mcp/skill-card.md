## Description:

Connects an agent to a signed-in Workday session to retrieve HR data and perform documented, confirmation-gated actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and managers use it to retrieve Workday people, compensation, benefits, and performance information, and to complete documented feedback, request, and enrollment actions that require confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious because documented tools can change sensitive Workday information despite a read-only claim.

Mitigation: Avoid installation unless the documented write actions are needed, and verify their confirmation safeguards before use.

Risk: The scan was partial because several local references were missing, leaving behavior behind those references unverified.

Mitigation: Review the missing implementation references and confirm the relevant safeguards before relying on the skill.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chrischall/skills/workday-mcp)
- [workday-mcp package on npm](https://www.npmjs.com/package/workday-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge project](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON and text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May contain personal and employment information, including compensation, benefits, and performance details.]

## Skill Version(s):

1.7.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
