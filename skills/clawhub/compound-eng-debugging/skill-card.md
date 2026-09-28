## Description:

Guides systematic root-cause debugging of errors, broken tests, flaky behavior, and regressions with evidence-backed verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to reproduce failures, trace causes, test hypotheses, and verify narrowly scoped repairs. It can also produce an evidence-backed diagnosis without changing code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic reports can reveal local paths, username, Git remote, branch, commit subject, and environment labels.

Mitigation: Review and redact diagnostic reports before sharing them; omit credentials and sensitive project information.

Risk: Active debugging can run reproduction commands or change code.

Mitigation: Authorize commands and repairs explicitly, and keep edits narrowly scoped with fresh verification.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-debugging)
- [Baselines and diagnostic data](references/baseline-and-data-handling.md)
- [Reproduction and investigation](references/reproduction-and-investigation.md)
- [Root cause tracing](references/root-cause-tracing.md)
- [Analysis of competing hypotheses](references/competing-hypotheses.md)
- [Repair and escalation](references/repair-and-escalation.md)
- [Defense-in-depth validation](references/defense-in-depth.md)
- [Specialized debugging patterns](references/specialized-patterns.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Code, Shell commands]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Seven-field debug report covering symptom, cause, fix, evidence, regression, related findings, and status.]

## Skill Version(s):

5.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
