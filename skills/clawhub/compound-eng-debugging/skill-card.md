## Description:

Guides systematic root-cause debugging and verifies repairs for errors, failing tests, flaky behavior, and regressions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to reproduce failures, trace their causes, make scoped repairs when authorized, and verify that the original failure is resolved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic reports or external searches can expose local paths, hostnames, remotes, tokens, or customer data.

Mitigation: Review and redact diagnostic output and search queries before sharing them externally.

Risk: Running tests or applying an unverified repair may affect local project state or introduce regressions.

Mitigation: Keep actions within the user's authorization, scope changes narrowly, and verify repairs against the original failure.

## Reference(s):

- [ia-debugging ClawHub release](https://clawhub.ai/iliaal/skills/compound-eng-debugging)
- [Reproduction and investigation](artifact/references/reproduction-and-investigation.md)
- [Root cause tracing](artifact/references/root-cause-tracing.md)
- [Baseline and diagnostic data handling](artifact/references/baseline-and-data-handling.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown debugging report with optional code changes and test commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports symptom, root cause, fix, evidence, regression, related findings, and status.]

## Skill Version(s):

5.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
