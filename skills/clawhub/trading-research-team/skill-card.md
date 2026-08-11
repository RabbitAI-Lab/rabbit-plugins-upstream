## Description:

Builds and back-tests trading strategy hypotheses with explicit risk limits and a written rejection log.

This skill is ready for commercial/non-commercial use.

## Publisher:

[t3ratech](https://clawhub.ai/user/t3ratech)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading research teams use this agent configuration bundle to coordinate strategy hypothesis generation, market-data review, back-testing, risk review, and decision logging before trading work proceeds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill combines autonomous trading authority with shell execution and external tool invocation.

Mitigation: Use least-privilege trading credentials, restrict shell commands, and require explicit human approval for orders or fund-affecting actions.

Risk: The artifact under-documents approval limits and safety boundaries for high-impact trading actions.

Mitigation: Define clear approval thresholds, audit trails, kill-switch controls, and readiness checks before deployment.

## Reference(s):

- [Trading Research Team on ClawHub](https://clawhub.ai/t3ratech/skills/trading-research-team)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text guidance with possible inline shell commands and configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces research workflows, role coordination guidance, risk review notes, and written decision logs.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
