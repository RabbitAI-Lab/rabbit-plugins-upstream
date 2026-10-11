## Description:

Guides agents to assess code structure, reduce complexity, and verify refactors with Topos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[krv-labs](https://clawhub.ai/user/krv-labs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use Topos to identify structural code-quality issues, prioritize refactors, and assess changes in local repositories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation instructions pipe an unverified remote script directly to a shell.

Mitigation: Review the installer before running it and prefer a pinned release or verified package when available.

Risk: Registering Topos with every supported agent harness may change more local integrations than intended.

Mitigation: Avoid `topos install --all` unless broad registration is desired.

Risk: Structural refactoring advice does not establish functional correctness or complete security coverage.

Mitigation: Review proposed edits, run project tests, and use dedicated security checks for high-stakes code.

## Reference(s):

- [Topos documentation](https://docs.krv.ai/topos/)
- [Topos agent guidance](https://docs.krv.ai/topos/agents.html)
- [ClawHub release](https://clawhub.ai/krv-labs/skills/topos)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Code guidance]

**Output Format:** [Text guidance, CLI reports, and structured MCP results]

**Output Parameters:** [1D; medal verdicts, pillar scores, ranked refactor targets, and change assessments]

**Other Properties Related to Output:** [Dependency-graph generation may write local .gitnexus files; suggested edits need separate review and testing.]

## Skill Version(s):

1.0.17 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
