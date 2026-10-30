## Description:

Access Workday HR data through an already signed-in browser session and extract selected fields for shell-based workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and Workday users use this skill to retrieve HR information such as org charts, worker profiles, tasks, pay, and benefits for shell-based workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented scope is inconsistent: instructions include other workers’ profiles and manager-facing HR records despite claiming access is limited to the user’s own data.

Mitigation: Limit requests to people and fields explicitly authorized for your role, protect HR outputs, and revoke persistent pairing when finished.

## Reference(s):

- [Workday endpoint examples](artifact/references/endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Shell command examples with JSON data and jq projections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented examples; results can contain sensitive HR information.]

## Skill Version(s):

1.1.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
