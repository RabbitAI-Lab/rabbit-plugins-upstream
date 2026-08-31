## Description:

Improves code quality across duplication, efficiency, and architectural fit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review living codebases for duplication, algorithmic inefficiency, clean-code issues, architectural misfit, error-handling gaps, and AI-generated overengineering. It can produce prioritized refactoring plans and, when explicitly requested, apply selected low-risk fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect broad repository scope and may make broad code changes when execution modes are requested.

Mitigation: Run it on a controlled branch, review the generated plan before execution, and require tests or manual review before accepting changes.

Risk: The insight-generation module can post code-analysis findings externally.

Mitigation: Do not use external posting unless the exact findings, destination, and approval are reviewed first.

Risk: All-wave or persistent execution modes may continue beyond a small refactoring scope.

Mitigation: Set explicit scope, stop conditions, and approval gates before enabling broad execution modes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-pensive-code-refinement)
- [Source Homepage from ClawHub Metadata](https://github.com/athola/claude-night-market/tree/master/plugins/pensive)
- [Algorithm Efficiency Module](artifact/modules/algorithm-efficiency.md)
- [Architectural Fit Module](artifact/modules/architectural-fit.md)
- [Clean Code Checks Module](artifact/modules/clean-code-checks.md)
- [Duplication Analysis Module](artifact/modules/duplication-analysis.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown with code snippets, shell commands, findings, plans, and optional code edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include prioritized findings, evidence references, refactoring plans, and repository changes when execution is explicitly requested.]

## Skill Version(s):

1.9.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
