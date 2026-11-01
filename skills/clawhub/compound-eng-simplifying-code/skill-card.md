## Description:

Simplifies, polishes, and declutters code without changing behavior. Use when asked to simplify, clean up, refactor, declutter, remove dead code or AI slop, or improve readability, including analysis-only simplification reports and code pasted inline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to make code easier to read and maintain while preserving its behavior, interfaces, side effects, and domain intent. It also supports analysis-only simplification reports and code shared inline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Code cleanup proposals or edits could unintentionally change behavior or remove an operational safeguard.

Mitigation: Define the project scope and review the diff and verification results; retain external-hazard guards unless their preconditions are reproduced and shown to be handled.

Risk: Referenced maintainer utilities and companion skills were not bundled or assessed.

Mitigation: Assess those utilities and companion skills separately before relying on their behavior.

## Reference(s):

- [Simplification patterns](artifact/references/simplification-patterns.md)
- [Orchestrated simplification](artifact/references/orchestrated-simplification.md)
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-simplifying-code)

## Skill Output:

**Output Type(s):** [Code, Markdown, Analysis]

**Output Format:** [Code edits or Markdown simplification reports and guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves behavior and interfaces; analysis-only requests produce proposals without edits.]

## Skill Version(s):

5.1.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
