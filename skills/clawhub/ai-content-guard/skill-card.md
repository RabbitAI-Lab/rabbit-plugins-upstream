## Description:

AI Content Guard checks text, files, webpages, and email for prompt injection, hidden characters, encoded payloads, and AI configuration backdoors, then provides a four-way verdict with redacted evidence and handling guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[a9320](https://clawhub.ai/user/a9320)

### License/Terms of Use:

MIT

## Use Case:

Developers and security reviewers use the skill to screen untrusted text and local files for prompt injection, hidden or encoded content, and AI configuration backdoors before relying on them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks this release suspicious and reports that webpage content may reach a shell command.

Mitigation: Avoid passing untrusted webpage content through any shell-backed path until the data flow and command handling have been reviewed; do not execute content under review.

Risk: The scan reports broad capabilities without a declared tool scope.

Mitigation: Review required file access and any host-provided tool permissions before enabling the skill, and limit scans to explicitly selected content.

Risk: The scan is partial, with one unresolved reference and degraded instruction-pattern analysis.

Mitigation: Treat scan results as incomplete and independently review the unresolved reference and any inputs that may not have been covered.

## Reference(s):

- [Detection rule guide](references/rules.md)
- [Privacy statement](references/privacy.md)
- [Security notes and coverage limits](references/security-notes.md)
- [Scan interpretation guide](references/guidance.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [JSON scan result with a verdict, findings, redacted evidence, and handling guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic scan output; scanned content is not executed.]

## Skill Version(s):

1.3.2 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
