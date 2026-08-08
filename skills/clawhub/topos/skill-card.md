## Description:

Structural code quality metrics, lattice verification, and refactor loops for agent-written code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[krv-labs](https://clawhub.ai/user/krv-labs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI coding agents use Topos to assess local repositories for structural code quality, identify refactor targets, and verify whether changes improve SIMPLE, COMPOSABLE, and SECURE scores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can run a remote installer and install npm package code locally.

Mitigation: Review the install script and npm package source before installation, especially in managed or production environments.

Risk: Optional MCP setup can register local tools in supported agent harnesses.

Mitigation: Run the documented status command after setup and keep MCP registration limited to intended environments.

Risk: Topos inspects local repositories and can create .gitnexus graph artifacts.

Mitigation: Run it only on repositories the user intends to analyze and account for generated .gitnexus artifacts in workspace hygiene.

Risk: Structural refactor guidance may change software behavior even when quality scores improve.

Mitigation: Run project tests, linters, and review after each edit; treat Topos results as structural signals rather than proof of functional correctness.

Risk: SECURE medal findings are structural heuristics, not full security assurance.

Mitigation: Pair Topos with dedicated security tooling for high-stakes code and explicitly review any remaining SECURE findings.

## Reference(s):

- [Topos documentation](https://docs.krv.ai/topos/)
- [Topos agent contract](https://docs.krv.ai/topos/agents.html)
- [ClawHub skill listing](https://clawhub.ai/krv-labs/skills/topos)
- [Publisher profile](https://clawhub.ai/user/krv-labs)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [CLI tables, ranked file lists, Markdown guidance, and MCP structured JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local .gitnexus graph artifacts when dependency graph generation is requested; does not require external credentials.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 0.4.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
