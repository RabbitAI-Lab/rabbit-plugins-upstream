## Description:

Evaluate scan results against security and regulatory frameworks, enforce policy-as-code, and generate SBOMs and compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, security engineers, and compliance teams use the skill to assess AI infrastructure scan results against security frameworks, apply custom policy checks, run requested cloud benchmarks, and produce compliance reports or SBOMs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags that setup examples may permit broader local scanning and external lookups than the privacy description explains.

Mitigation: Review scan scope and network behavior for the installed version, select inputs explicitly, choose an output path that will not overwrite an existing report, and use scoped read-only credentials only for requested cloud checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-compliance)
- [Project homepage](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Configuration guidance]

**Output Format:** [Compliance findings and reports; CycloneDX or SPDX JSON SBOMs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cloud benchmark checks are optional and use locally configured credentials only when explicitly requested.]

## Skill Version(s):

0.112.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
