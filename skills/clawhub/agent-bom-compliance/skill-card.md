## Description:

Evaluate AI infrastructure scan results against security and regulatory frameworks, enforce policy-as-code rules, and generate SBOMs and compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers, security engineers, and compliance teams use the skill to evaluate scan results against security and regulatory frameworks, check custom policies, run selected cloud CIS benchmarks, and generate SBOMs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Example commands may access local agent settings and contact vulnerability services beyond the skill's stated file and network limits.

Mitigation: Review and pin the external package version, restrict discovery to intended inputs, verify network behavior, choose an output path that will not overwrite existing files, and use read-only cloud credentials only for explicitly requested checks.

## Reference(s):

- [Project homepage](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON files, Compliance guidance]

**Output Format:** [Compliance summaries and findings in text or Markdown; SBOMs in CycloneDX or SPDX JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Frameworks, policies, and input data depend on the request; optional CIS checks require configured cloud access.]

## Skill Version(s):

0.113.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
