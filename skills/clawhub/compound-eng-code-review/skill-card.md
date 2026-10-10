## Description:

Guides structured reviews of code changes, pull requests, and diffs, with severity-ranked findings and an optional deep multi-agent review mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to review repository changes and submitted diffs for correctness, security, and maintainability, and to receive evidence-backed findings and a merge-readiness assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review may inspect sensitive repository changes or run tests and git/gh commands.

Mitigation: Review the selected scope and commands before running them; avoid exposing credentials or confidential data.

Risk: External reviewer dispatch may transmit diffs, files, logs, or fixtures to another provider.

Mitigation: Approve the described packet explicitly before dispatch and exclude credential-bearing paths.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-code-review)
- [Review scope and mode selection](artifact/references/scope-and-mode-selection.md)
- [Review report and integration](artifact/references/report-and-integration.md)
- [External review subprocess](artifact/references/external-review-subprocess.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown review report with severity-ranked findings, scope, verification results, and merge-readiness assessment]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include file and line references, residual risks, and action recommendations.]

## Skill Version(s):

5.0.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
