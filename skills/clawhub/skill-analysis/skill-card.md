## Description:

Scans agent skills for security risks and produces admission decisions and shareable audit reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jixiang-cc](https://clawhub.ai/user/jixiang-cc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to assess third-party agent skills before installation, review installed skills, and gate changes in CI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch scans may execute untrusted skill code even without requesting dynamic analysis.

Mitigation: Avoid batch-scanning untrusted skills on your normal machine; use a container or disposable VM.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/jixiang-cc/skills/skill-analysis)
- [Usage examples](references/examples.md)
- [Analysis limitations](references/limitations.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown reports, JSON reports, SARIF findings, SBOM files]

**Output Format:** [Markdown, JSON, SARIF, or CycloneDX-style SBOM]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes an admission verdict, risk score, findings, and suggested actions.]

## Skill Version(s):

3.3.8 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
