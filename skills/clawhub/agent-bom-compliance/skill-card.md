## Description:

Evaluate scan results against security and regulatory frameworks, enforce policy-as-code rules, and generate SBOMs and compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security/compliance teams use this skill to assess AI infrastructure scan results against security and regulatory frameworks, apply policy-as-code checks, and produce SBOMs and compliance reports. Optional CIS checks query cloud accounts when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Example commands can inspect local agent settings and contact public services beyond what the privacy description discloses.

Mitigation: Review scan inputs, discovery scope, and network settings; preview discovery paths, use offline mode when needed, choose the report destination, and provide only scoped read-only cloud access for confirmed CIS checks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/msaad00/skills/agent-bom-compliance)
- [Project Repository](https://github.com/msaad00/agent-bom)
- [PyPI Package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Files, JSON, Markdown, Guidance]

**Output Format:** [JSON (CycloneDX or SPDX SBOMs and structured results), Markdown, and text reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on selected frameworks, policies, and scan inputs.]

## Skill Version(s):

0.110.0 (source: frontmatter, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
