## Description:

Agent-bom compliance helps agents evaluate AI infrastructure scan results against security and regulatory frameworks, enforce policy rules, generate SBOMs, and produce compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, security engineers, and compliance teams use this skill to turn AI infrastructure scan results, SBOMs, and policy files into compliance checks and reports across OWASP, NIST, SOC 2, ISO 27001, CMMC, EU AI Act, AISVS, and related frameworks. It also supports explicit, optional read-only CIS benchmark checks for cloud accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned package installation can resolve to a different release over time.

Mitigation: Install a pinned version such as agent-bom==0.104.0 or use reviewed source before deploying the skill.

Risk: Optional CIS benchmark checks use cloud SDK credentials and call provider APIs.

Mitigation: Run CIS checks only when explicitly requested, use least-privilege credentials, and verify the provider and account before execution.

Risk: User-provided SBOMs and policy files may contain sensitive inventory or control information.

Mitigation: Run the skill in a controlled workspace and review generated reports before sharing them outside the intended audience.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-compliance)
- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON files]

**Output Format:** [Markdown or text guidance with command examples; generated SBOM and compliance outputs may use CycloneDX, SPDX, or framework-specific report formats.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional CIS checks use locally configured cloud credentials and read-only provider API calls only when explicitly invoked.]

## Skill Version(s):

0.104.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
