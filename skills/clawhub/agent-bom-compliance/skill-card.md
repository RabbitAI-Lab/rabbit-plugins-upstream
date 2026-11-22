## Description:

Evaluates AI infrastructure scan results against security and regulatory frameworks, enforces policy-as-code rules, and generates SBOMs and compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use the skill to evaluate AI systems against standards such as OWASP, NIST, and the EU AI Act, enforce custom policies, and generate CycloneDX or SPDX SBOMs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SBOM generation may create an output file even though the manifest declares no file writes.

Mitigation: Choose the output location before generating an SBOM and avoid unintentionally overwriting an existing file.

## Reference(s):

- [Project repository](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Files]

**Output Format:** [Compliance findings and policy results, with SBOMs in CycloneDX or SPDX JSON formats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [SBOM generation may write an output file; choose its location and avoid unintentionally overwriting an existing file.]

## Skill Version(s):

0.115.5 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
