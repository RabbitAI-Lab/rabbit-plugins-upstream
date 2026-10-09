## Description:

Looks up MCP server security metadata, checks packages before installation, scores server inventories, assesses skill trust, and supports code scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to check MCP server registry entries, assess skills and package trust, score server inventories, and request code scans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the optional third-party agent-bom package adds software to the operator environment.

Mitigation: Review the package before installing it with pipx or pip.

Risk: Optional Snyk enrichment uses a token and sends scan data to a third-party service.

Mitigation: Keep SNYK_TOKEN in the operator environment, never include it in output, and only scan intended files or repositories.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-registry)
- [Project homepage (listed in skill metadata)](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Registry matches, trust assessments, risk scores, and scan findings depend on the requested tool.]

## Skill Version(s):

0.108.3 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
