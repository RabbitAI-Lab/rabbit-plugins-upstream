## Description:

Evaluates AI infrastructure scan results against security and regulatory frameworks, checks policies, and generates compliance reports and SBOMs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to check scan results against compliance frameworks, evaluate policies, produce SBOMs, and optionally run cloud CIS benchmarks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional CIS checks can read cloud account configuration using existing SDK credentials.

Mitigation: Confirm the intended cloud provider and account before explicitly running a CIS check; use operator-configured credentials and do not share secrets in prompts or output.

Risk: Installing the external agent-bom package introduces a third-party software dependency.

Mitigation: Verify the package source before installing it in a sensitive environment.

## Reference(s):

- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom package on PyPI](https://pypi.org/project/agent-bom/)
- [agent-bom OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands]

**Output Format:** [Markdown guidance and shell commands; JSON compliance reports and CycloneDX or SPDX SBOMs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cloud benchmark checks require explicit invocation and locally configured provider credentials.]

## Skill Version(s):

0.108.2 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
