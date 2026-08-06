## Description:

Mandatory risk-driven verification workflow for maintained-code changes. Use when implementing, fixing, refactoring, deleting, migrating, or reviewing code to identify all materially affected behavior, map failure risks to sufficient tests, execute required evidence, and report unresolved test gaps and residual risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wujiaming88](https://clawhub.ai/user/wujiaming88)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to verify maintained-code changes with risk-driven impact analysis, test selection, executed evidence, and explicit reporting of unresolved gaps and residual risk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verification workflows can take extra agent time because they require repository inspection and relevant test execution.

Mitigation: Use the skill when structured code-change verification is needed and expect a more deliberate evidence-gathering workflow.

Risk: An agent could overstate verification if tests were not actually executed or if evidence gaps are hidden.

Mitigation: Require the skill's Gate status rows, Change Impact table, Test Portfolio table, exact executed commands, unresolved gaps, and residual risk in the final handoff.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wujiaming88/skills/test-code-change)
- [Change Impact and Risk Analysis](references/impact-analysis.md)
- [Scientific Test Method Selection](references/test-method-selection.md)
- [Change Test Evidence](references/evidence-report-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with traceability tables and command evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires exact Gate status rows, Change Impact traceability, Test Portfolio traceability, executed evidence, unresolved gaps, and residual risk.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
