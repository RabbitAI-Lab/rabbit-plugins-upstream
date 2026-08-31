## Description:

Analyzes past skill improvement outcomes to detect regressions and recommend meta-optimizations to the improvement process.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review batches of skill-improvement outcomes, identify regressions and recurring success or failure patterns, and propose strategy adjustments for future improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may persist local execution traces containing file paths, tool targets, decision rationales, and workflow metadata.

Mitigation: Use it only where that local trace history is acceptable, avoid sensitive or regulated repositories unless reviewed, and periodically clear ~/.claude/skills/traces when retention is not needed.

Risk: Meta-analysis recommendations could introduce incorrect or misleading changes to future skill-improvement behavior.

Mitigation: Review proposed strategy adjustments before applying them and scan skills before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-metacognitive-self-mod)
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report with inline JSON, Python, and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proposed improvement-strategy changes and local trace or memory file locations for user review; changes are not auto-applied.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
