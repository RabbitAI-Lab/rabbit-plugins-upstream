## Description:

MCP server security registry and trust assessment for looking up server security metadata, running pre-install marketplace checks, batch fleet risk scoring, skill-file trust assessment, and SAST code scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security reviewers use this skill to assess MCP servers and skill files before installation or deployment, including registry lookups, marketplace checks, fleet risk scoring, provenance checks, and SAST-oriented code scanning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional Snyk enrichment can send vulnerability-enrichment requests to a third-party endpoint when SNYK_TOKEN is provided.

Mitigation: Use SNYK_TOKEN only when third-party enrichment is intentional; otherwise rely on the bundled local registry and credential-free checks.

Risk: Trust and scan results may influence install or deployment decisions for MCP servers and skill files.

Mitigation: Review the PyPI and GitHub package before installing and treat registry, trust, and SAST findings as decision support rather than final approval.

## Reference(s):

- [agent-bom source](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or text with command examples and structured security findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local registry lookup results, trust findings, fleet risk scores, provenance verification guidance, and code scan findings.]

## Skill Version(s):

0.99.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
