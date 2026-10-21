## Description:

Helps agents look up MCP server security metadata, check packages before installation, score server fleets, assess skill-file trust, and run code security scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to assess MCP servers and skill files before installation or deployment and to review code scan findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party Python package may be unsuitable for sensitive environments without review.

Mitigation: Review the package and source before installation in sensitive environments.

Risk: Optional Snyk enrichment uses an access token and external vulnerability lookups.

Mitigation: Leave enrichment disabled unless external lookups are acceptable; keep SNYK_TOKEN in the operator environment and out of outputs.

Risk: Scanning local code or skill files exposes their contents to the scanner process.

Mitigation: Scan only files approved for local processing.

## Reference(s):

- [Agent BOM project homepage](https://github.com/msaad00/agent-bom)
- [Agent BOM package](https://pypi.org/project/agent-bom/)
- [Agent BOM OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown with optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Registry lookups, trust assessments, risk scores, and code scan findings depend on the requested check.]

## Skill Version(s):

0.109.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
