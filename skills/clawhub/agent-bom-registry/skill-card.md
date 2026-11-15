## Description:

MCP server security registry and trust assessment for looking up servers, checking marketplaces, scoring fleets, assessing skill files, and scanning code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use the skill to check MCP server trust, review packages before installation, assess skill files, score server inventories, and run static code analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A benign scan result does not guarantee that a skill or package is free of risk.

Mitigation: Review the scanned content and findings before acting on installation or trust recommendations.

Risk: Optional Snyk vulnerability enrichment uses an operator-supplied SNYK_TOKEN.

Mitigation: Keep the token in the operator environment and do not print or embed it in skill output.

## Reference(s):

- [Agent BOM project](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Text and structured assessment results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes registry lookups, trust assessments, and scan findings.]

## Skill Version(s):

0.114.0 (source: artifact frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
