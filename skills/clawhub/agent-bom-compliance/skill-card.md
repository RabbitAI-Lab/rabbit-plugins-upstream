## Description:

Evaluates AI infrastructure scan results against security and regulatory frameworks, checks policies, and generates compliance reports and SBOMs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to assess AI infrastructure scan results against compliance frameworks, enforce policies, and generate SBOMs. Optional CIS checks assess selected cloud accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional CIS checks contact cloud providers using locally configured credentials.

Mitigation: Run cloud checks only with explicit confirmation against accounts you intend to assess.

## Reference(s):

- [Agent-BOM project homepage (skill metadata; import provenance unavailable)](https://github.com/msaad00/agent-bom)
- [Agent-BOM on PyPI](https://pypi.org/project/agent-bom/)
- [Agent-BOM OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)
- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-compliance)

## Skill Output:

**Output Type(s):** [Compliance reports, Policy findings, SBOMs, Shell commands]

**Output Format:** [Markdown guidance and reports; CycloneDX or SPDX JSON SBOMs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cloud CIS checks are optional and require explicit confirmation.]

## Skill Version(s):

0.107.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
