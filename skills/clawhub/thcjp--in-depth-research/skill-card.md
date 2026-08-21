## Description:

深度研究引擎 guides agents through scoped, multi-source research with source evaluation, iterative deepening, synthesis, and structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and enterprise teams use this skill to conduct quick through exhaustive research, evaluate sources, reconcile conflicting evidence, and deliver structured findings for decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Command execution, local file access, API keys, and callbacks may expose systems or data if used in an unsuitable environment.

Mitigation: Install only where those capabilities are acceptable, and require explicit user approval before running shell commands or sending results to external URLs.

Risk: The artifact describes command and file-access capabilities inconsistently, making the effective permission scope easy to misunderstand.

Mitigation: Review the effective agent tool permissions before deployment and restrict read, exec, network, and callback behavior to the minimum needed.

Risk: Research outputs may rely on stale, inaccessible, biased, or contradictory sources.

Mitigation: Require final reports to include sources, confidence, caveats, gaps, and methodology so reviewers can assess evidence quality.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/in-depth-research)
- [SkillHub Homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown research reports with optional JSON status and result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include a direct answer, confidence level, key findings, caveats, gaps, source list, and methodology.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
