## Description:

Assesses architecture decisions, ADR compliance, and coupling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review architecture changes, ADR coverage, module coupling, design invariants, and principle-level risks before merging substantial system changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may suggest local shell commands for repository inspection and may produce architecture recommendations that affect project direction.

Mitigation: Review proposed commands before execution and require human review for architecture decisions, especially invariant conflicts, ADR changes, and merge-blocking recommendations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-pensive-architecture-review)
- [Source Homepage from ClawHub Metadata](https://github.com/athola/claude-night-market/tree/master/plugins/pensive)
- [FPF Framework](https://github.com/ailev/FPF)
- [quint-code](https://github.com/m0n0x41d/quint-code)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with structured findings, checklists, diagrams, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ADR audit findings, coupling analysis, invariant conflict options, principle checks, risk summaries, and follow-up actions.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
