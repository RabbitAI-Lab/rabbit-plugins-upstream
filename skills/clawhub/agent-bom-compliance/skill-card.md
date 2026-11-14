## Description:

Evaluates AI infrastructure scan results against security and regulatory frameworks and generates SBOMs and compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security teams use the skill to assess AI infrastructure scan results against security and regulatory frameworks, check custom policies, generate SBOMs and compliance reports, and optionally run explicitly requested CIS checks against cloud accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The SBOM example writes an output file, though the manifest does not declare file-writing behavior.

Mitigation: Before using the SBOM example, check the output path and whether a file there could be overwritten.

## Reference(s):

- [Agent BOM project homepage](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)
- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-compliance)

## Skill Output:

**Output Type(s):** [Analysis, Markdown reports, JSON files]

**Output Format:** [Compliance and policy findings, reports, and CycloneDX or SPDX SBOM files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [SBOM output is written to the path specified by the user.]

## Skill Version(s):

0.114.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
