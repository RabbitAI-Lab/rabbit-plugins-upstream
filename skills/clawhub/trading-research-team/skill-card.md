## Description:

Builds and back-tests trading strategy hypotheses with explicit risk limits and a written rejection log.

This skill is ready for commercial/non-commercial use.

## Publisher:

[t3ratech](https://clawhub.ai/user/t3ratech)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading researchers use this bundle to generate strategy hypotheses, gather market inputs, run back-tests, complete risk review, and record accept or reject decisions before deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An autonomous trading role may be connected to live trading systems without clear approval gates or safety limits.

Mitigation: Use the bundle for controlled research and simulation by default; require explicit human approval before any live account access.

Risk: Broad local-system authority could allow commands or file access beyond the needs of trading research.

Mitigation: Restrict command execution and file access, add audit logging, and enforce position, loss, and kill-switch limits before installation in sensitive environments.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured agent guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces coordinated trading-research role guidance, evaluation prompts, and risk-review workflow notes.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata; artifact text states Version 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
