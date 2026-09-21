## Description:

Add governance to experiment workflows -- PIN-protected destructive ops, standardized metrics registry with thresholds, compare-scores ranking with gating, and competition rules audit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[diamond2nv](https://clawhub.ai/user/diamond2nv)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and MLOps engineers use this skill to add governance checks to experiment workflows, including PIN protection for destructive operations, standardized metric reporting, score comparison with gates, and competition-rules audit guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automation can bypass PIN protection for destructive experiment commands when --force is used.

Mitigation: Review before installing for real ClearML workflows, avoid making --force the default, and require a secure PIN or separate approval path for stop, cancel, delete, or PIN-clear operations.

## Reference(s):

- [expflow project homepage](https://github.com/diamond2nv/expflow)
- [ClawHub skill page](https://clawhub.ai/diamond2nv/skills/experiment-lifecycle-governance)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code blocks and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes CLI patterns, metric registry examples, audit checks, and operational guardrails for experiment governance.]

## Skill Version(s):

0.7.1 (source: evidence release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
