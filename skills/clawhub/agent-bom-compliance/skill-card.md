## Description:

Evaluates AI infrastructure scans against security and regulatory frameworks, enforces policy checks, and generates SBOMs and compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and security engineers use the skill to assess AI infrastructure scan results against security and regulatory frameworks, check custom policies, run requested cloud benchmarks, and generate SBOMs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan examples do not establish the promised limits on file access and offline operation, and the external package's runtime privacy guarantees remain unverified.

Mitigation: Verify a pinned package release, choose an explicitly scoped offline workflow when processing only supplied files, and clarify whether local agent configurations and external vulnerability lookups are permitted. Use read-only cloud credentials for requested benchmarks and select an output path that will not replace an existing report.

## Reference(s):

- [Project homepage](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Files]

**Output Format:** [Compliance findings and reports; CycloneDX or SPDX JSON SBOM files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compliance and policy evaluation runs on supplied scan data; optional CIS benchmark findings require explicitly requested cloud checks.]

## Skill Version(s):

0.113.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
