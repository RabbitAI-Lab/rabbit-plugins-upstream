## Description:

Routes industrial and operational-technology troubleshooting tasks to the appropriate iaiops edition and MCP profile for read-first diagnostics and governed device access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Industrial operators and engineers use this skill to select an iaiops edition and MCP profile for equipment connectivity, diagnostics, and downtime analysis while keeping control-system changes subject to human approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inconsistent substation and energy routing could direct users to the wrong package.

Mitigation: Review energy routing before installation or use in power-system environments; verify the external iaiops-energy package before installing it.

Risk: Writing to industrial control systems can have high-impact operational consequences.

Mitigation: Keep operations read-first and require explicit human approval before any real device write.

## Reference(s):

- [iaiops release on ClawHub](https://clawhub.ai/zw008/skills/iaiops)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes to a specialized edition and MCP profile; recommendations are advisory.]

## Skill Version(s):

0.31.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
