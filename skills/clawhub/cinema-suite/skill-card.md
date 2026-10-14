## Description:

A cinema ticketing catalog that maps cinema identities to installable OpenClaw mode skills for capture, replay, coupon binding, and failure handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rascalagnt001](https://clawhub.ai/user/rascalagnt001)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this catalog to route cinema ticketing requests to the matching cinema and mode skill. Related mode skills must be installed separately to perform ticketing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing related mode skills can enable ticketing actions beyond catalog lookup, including capture, replay, coupon binding, and page-world actions.

Mitigation: Review each referenced mode skill separately before installing or enabling it.

## Reference(s):

- [Cinema Agent release on ClawHub](https://clawhub.ai/rascalagnt001/skills/cinema-suite)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands]

**Output Format:** [Markdown and text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides cinema-to-mode routing guidance; related mode skills are required for executable workflows.]

## Skill Version(s):

1.0.2 (source: ClawHub release; bundled package reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
