## Description:

Helps assess MCP server trust through registry lookups, pre-install checks, fleet scoring, skill-file analysis, and code scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to check MCP servers before installation, assess server inventories and skill files, and request code-scan guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional vulnerability enrichment may send data to Snyk when configured.

Mitigation: Enable it only when appropriate, and keep the optional token in the operator environment rather than skill output.

Risk: Skill-file analysis may read files explicitly supplied by the user.

Mitigation: Review file selections before analysis and avoid submitting sensitive files unnecessarily.

Risk: Installing the external agent-bom package introduces supply-chain exposure.

Mitigation: Review the package source and pin a trusted release before installation when assurance matters.

## Reference(s):

- [Project homepage (publisher-listed; import provenance unavailable)](https://github.com/msaad00/agent-bom)
- [agent-bom package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Registry matches, trust assessments, risk scores, and scan findings vary by input.]

## Skill Version(s):

0.107.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
