## Description:

Evaluate and improve code with Topos for complexity reduction, structural security checks, refactor verification, and code-quality goals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[krv-labs](https://clawhub.ai/user/krv-labs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use Topos to assess local repositories, identify structural quality issues, guide focused refactors, and compare results after changes. Its findings are advisory and do not replace tests or dedicated security checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommended installation runs a mutable remote script directly in a shell.

Mitigation: Review the installer before execution and prefer a pinned or signed package when available.

Risk: Installing the MCP integration across all agent tools changes persistent tool configuration.

Mitigation: Run `topos install --all` only when registration in every supported agent tool is intended.

Risk: Structural scores and security findings can miss functional defects or security vulnerabilities.

Mitigation: Treat findings as advisory; review changes and run tests, linters, and dedicated security tooling for important code.

## Reference(s):

- [Topos documentation](https://docs.krv.ai/topos/)
- [Topos agent contract](https://docs.krv.ai/topos/agents.html)
- [Topos ClawHub listing](https://clawhub.ai/krv-labs/skills/topos)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [CLI reports and structured MCP results, with agent guidance in text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes quality verdicts, pillar scores, ranked refactor targets, and before/after assessments; optional dependency-graph generation writes local artifacts.]

## Skill Version(s):

1.0.18 (source: ClawHub release; skill document version: 0.10.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
