## Description:

Guides agents in measuring and improving code structure, complexity, and security heuristics with Topos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[krv-labs](https://clawhub.ai/user/krv-labs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use Topos to identify code-quality issues, prioritize refactors, and check structural improvements against project goals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The suggested installer runs a remotely hosted script in the shell, which may change without notice.

Mitigation: Review the installer source first and prefer a pinned or package-manager installation when available.

Risk: Installing across all supported agent harnesses can persistently change their integrations.

Mitigation: Avoid topos install --all unless broad registration is intentional; verify configured integrations afterward.

Risk: Assessments read local repository code and git state and may create .gitnexus graph artifacts.

Mitigation: Run only in repositories you intend to inspect and account for generated graph artifacts.

Risk: Structural scores do not establish functional correctness or complete security coverage.

Mitigation: Review proposed edits, run project tests, and use dedicated security checks where appropriate.

## Reference(s):

- [Topos documentation](https://docs.krv.ai/topos/)
- [Topos agent contract](https://docs.krv.ai/topos/agents.html)
- [Topos ClawHub release](https://clawhub.ai/krv-labs/skills/topos)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code]

**Output Format:** [Markdown guidance and commands; structured assessment results when Topos is run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes quality scores and refactor targets; graph generation can create .gitnexus artifacts.]

## Skill Version(s):

1.0.21 (source: server-resolved ClawHub release; artifact frontmatter: 0.12.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
