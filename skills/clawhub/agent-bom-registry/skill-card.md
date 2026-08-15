## Description:

MCP server security registry and trust assessment skill for looking up servers in a 1081-entry registry, running pre-install marketplace checks, batch fleet risk scoring, skill trust assessment, and SAST code scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to check MCP server trust signals, assess skill files, run pre-install marketplace checks, and scan code with security-oriented tooling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional Snyk enrichment may send code-scan information to a third-party service when SNYK_TOKEN is configured.

Mitigation: Use the bundled local registry mode when external sharing is not acceptable, and configure SNYK_TOKEN only in operator-controlled environments.

Risk: Security scan and trust results can be mistaken for a complete approval decision.

Mitigation: Review findings before deployment and combine them with the organization's security and procurement checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-registry)
- [Project homepage](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands]

**Output Format:** [Markdown with inline command examples and structured analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include security findings, registry lookup results, fleet risk scoring, and optional SAST scan output.]

## Skill Version(s):

0.100.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
