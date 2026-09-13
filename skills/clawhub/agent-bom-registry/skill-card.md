## Description:

Provides MCP server security registry lookup and trust assessment for server metadata, marketplace checks, fleet risk scoring, skill-file trust checks, and SAST code scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to check MCP server trust, scan skill files, and review package or fleet risk before installation or deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the agent-bom Python package from PyPI runs third-party package code in the local environment.

Mitigation: Pin a reviewed version and install with pipx or another isolated environment before use.

Risk: Optional Snyk enrichment requires an authenticated SNYK_TOKEN and may contact a third-party API.

Mitigation: Provide SNYK_TOKEN only when Snyk enrichment is intended, keep it in the operator environment, and avoid printing or embedding token values in outputs.

Risk: Security registry lookups and SAST results can be incomplete or stale.

Mitigation: Treat findings as decision support and review high-impact installation or deployment decisions before acting.

## Reference(s):

- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard for agent-bom](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-registry)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or text responses with commands, configuration guidance, and structured security findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference bundled registry data, user-provided SKILL.md content, optional Semgrep findings, and optional Snyk enrichment when explicitly configured.]

## Skill Version(s):

0.104.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
