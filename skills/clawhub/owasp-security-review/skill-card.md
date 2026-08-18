## Description:

Performs severity-rated security audits against OWASP-focused review categories to identify code vulnerabilities, insecure configuration, dependency issues, and possible secret exposure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heroinyan-stack](https://clawhub.ai/user/heroinyan-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to inspect codebases, configuration, dependencies, and secrets for actionable security findings. It is intended to produce an audit report with severity, affected file locations, remediation guidance, and compliance mapping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill inspects source code, configuration, dependency manifests, and possible secrets, so generated reports may contain sensitive paths, weaknesses, or credentials.

Mitigation: Use it only in workspaces where this inspection is acceptable, and review reports before sharing them outside the intended audience.

Risk: Security review output may be incomplete or include findings that need human validation.

Mitigation: Treat results as review guidance and verify material findings, exploitability, and remediation changes before relying on them for release or compliance decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heroinyan-stack/skills/owasp-security-review)

## Skill Output:

**Output Type(s):** [markdown, guidance, code, shell commands]

**Output Format:** [Markdown security audit report with tables, findings, code snippets, remediation examples, and reference links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are grouped by severity and include OWASP category, CWE ID, affected file and line, impact, remediation, and priority where available.]

## Skill Version(s):

1.0.0 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
