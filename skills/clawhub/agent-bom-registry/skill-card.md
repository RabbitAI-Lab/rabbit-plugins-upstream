## Description:

MCP server security registry and trust assessment for looking up servers in a 1,295-entry metadata registry, checking marketplaces before installation, scoring server fleets, assessing skill files, and running SAST code scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use the skill to look up MCP server security metadata, assess marketplace and fleet risk, inspect skill-file trust, and run code scans before adopting tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation adds an external Python package whose runtime was not supplied for inspection.

Mitigation: Review the package and its dependencies before installation, and scope scans to the intended files.

Risk: Optional Snyk enrichment sends vulnerability lookup requests to a third-party service and requires SNYK_TOKEN.

Mitigation: Review Snyk’s data handling before enabling enrichment and keep SNYK_TOKEN in the operator environment; do not print or embed it in skill output.

## Reference(s):

- [ClawHub release](https://clawhub.ai/msaad00/skills/agent-bom-registry)
- [Project homepage](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Structured text and Markdown security assessment results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected registry lookup, scan, or trust assessment.]

## Skill Version(s):

0.113.2 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
