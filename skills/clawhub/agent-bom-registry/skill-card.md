## Description:

Looks up MCP server security metadata, checks packages before installation, assesses skill trust, scores server fleets, and supports code scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to check MCP server registry entries, assess skill files and packages before installation, and review scan findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the skill's third-party agent-bom package runs external software.

Mitigation: Review the package before installation and run it only on files or repositories you intend to analyze.

Risk: Optional Snyk enrichment uses an access token and makes a third-party network call.

Mitigation: Leave SNYK_TOKEN unset unless enrichment is needed; keep the token in the operator environment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-registry)
- [Project homepage (listed in skill metadata)](https://github.com/msaad00/agent-bom)
- [agent-bom package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Registry matches, trust assessments, risk scores, and scan findings]

## Skill Version(s):

0.108.4 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
