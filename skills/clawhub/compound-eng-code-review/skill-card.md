## Description: <br>
Structured code reviews with severity-ranked findings and deep multi-agent mode for reviewing code, auditing quality, or critiquing PRs, MRs, and diffs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to perform structured reviews of code changes, PRs, MRs, and diffs. It helps agents resolve review scope, choose standard or deep review mode, rank findings by severity and confidence, and produce actionable review output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is expected to inspect repository diffs and local work-in-progress, which may expose sensitive code or private implementation details to the reviewing agent. <br>
Mitigation: Use it only in repositories where the agent is authorized to inspect the review scope, and review generated comments before sharing them externally. <br>
Risk: Optional auto-fix or external reviewer behavior can affect code or route review work through additional tools. <br>
Mitigation: Confirm the agent setup requires approval for gated fixes and external reviewer execution before using those modes. <br>
Risk: Review findings may be incomplete or incorrect even when the security scan verdict is clean. <br>
Mitigation: Require human review of cited evidence and run relevant project checks before relying on findings for merge decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-code-review) <br>
- [ia-code-review Specification](SPEC.md) <br>
- [Action Routing - 4-Tier Fix Classification](references/action-routing.md) <br>
- [What to Check - Review Category Checklists](references/check-categories.md) <br>
- [Deep Review Process](references/deep-review.md) <br>
- [Driving a long-running external reviewer subprocess](references/external-review-subprocess.md) <br>
- [False Positive Suppression](references/false-positive-suppression.md) <br>
- [Language-Specific Review Profiles](references/language-profiles.md) <br>
- [PR sizing and large-diff strategy](references/pr-sizing.md) <br>
- [Reliability Patterns](references/reliability-patterns.md) <br>
- [Review Traps Catalog](references/review-traps-catalog.md) <br>
- [Scope and comparison-range resolution](references/scope-resolution.md) <br>
- [Security Detection Patterns](references/security-patterns.md) <br>
- [Security Test Coverage Checklist](references/security-test-coverage.md) <br>
- [Severity Levels and Confidence Rubric](references/severity-and-confidence.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Guidance, Shell commands, Code] <br>
**Output Format:** [Markdown review with severity-ranked findings, quoted evidence, fix guidance, residual risks, and a merge-readiness verdict.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Findings are numbered sequentially as CR-001 and capped at 10 per severity; clean reviews explicitly state that no actionable findings were found.] <br>

## Skill Version(s): <br>
4.3.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
