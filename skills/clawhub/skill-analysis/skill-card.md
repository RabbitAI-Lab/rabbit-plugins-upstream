## Description:

Audits agent skills for security and supply-chain risks and produces actionable admission decisions and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jixiang-cc](https://clawhub.ai/user/jixiang-cc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to assess third-party agent skills before installation or deployment, review existing collections, and gate changes in CI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch scans may automatically execute high-risk target Python files, even without an explicit dynamic-execution request.

Mitigation: Review the tool before use and scan untrusted skill directories only in a disposable container or VM; do not assume batch mode is read-only.

Risk: Dynamic review executes third-party code and may use a sandbox that is not a hard security boundary.

Mitigation: Treat --dynamic and automatic dynamic review as code execution; use an isolated, disposable environment without sensitive data.

## Reference(s):

- [Skill Analysis release on ClawHub](https://clawhub.ai/jixiang-cc/skills/skill-analysis)
- [Examples and reporting formats](references/examples.md)
- [Static analysis limitations](references/limitations.md)
- [Threat landscape and rule sources](references/threat-landscape-2026.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, JSON, SARIF, SBOM]

**Output Format:** [Markdown reports or machine-readable JSON, SARIF, and SBOM files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Risk scores, severity findings, and PASS, REVIEW, NEED_REVIEW, or BLOCK recommendations.]

## Skill Version(s):

3.3.6 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
