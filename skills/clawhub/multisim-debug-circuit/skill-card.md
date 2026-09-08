## Description:

Diagnoses Multisim circuit or simulation failures and guides minimal, reversible fixes for invalid netlists, convergence failures, wrong waveforms, bias errors, or missing outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yxy050208](https://clawhub.ai/user/yxy050208)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to debug Multisim circuits by separating environment failures from circuit defects, reviewing bounded evidence, proposing the smallest reversible design change, and comparing retest results before declaring a fix.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Debugging recommendations could be incorrect if circuit evidence is incomplete or retesting is skipped.

Mitigation: Preserve original designs, inspect netlists and logs, apply only minimal reversible changes, and compare original and candidate retest results before claiming resolution.

Risk: Persisting a candidate change too early could overwrite or commit an unapproved circuit modification.

Mitigation: Require separate user approval before handing a passing candidate to any persistent save or adoption workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yxy050208/skills/multisim-debug-circuit)
- [Publisher profile](https://clawhub.ai/user/yxy050208)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured findings and optional DesignPatch details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a symptoms, evidence, root cause, minimal change, retest result, and residual risk structure.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
