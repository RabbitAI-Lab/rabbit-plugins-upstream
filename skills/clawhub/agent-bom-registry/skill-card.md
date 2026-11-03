## Description:

Provides MCP server security registry lookups, pre-install trust checks, fleet risk scoring, skill-file trust assessments, and SAST code scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and security reviewers use the skill to check MCP server packages and inventories, assess skill files before use, and review code for security issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional Snyk enrichment uses an external service and requires an operator token.

Mitigation: Enable it only when external enrichment is appropriate, and keep the token in the operator environment.

Risk: Separately installed dependencies and runtime privacy guarantees were not audited.

Mitigation: Use a verified package release in an isolated environment and review dependencies and privacy behavior before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-registry)
- [Project homepage](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Structured security assessment and registry lookup results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the server names, package details, inventories, or skill content provided.]

## Skill Version(s):

0.113.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
