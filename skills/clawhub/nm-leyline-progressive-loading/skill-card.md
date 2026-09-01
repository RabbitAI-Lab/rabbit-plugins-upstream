## Description:

Implements hub-and-spoke lazy loading to minimize token usage in large skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to design modular agent skills that load reference modules on demand based on user intent, artifacts, and token budget.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing and repository-mutation examples could be applied to the wrong package index, branch, or credentials if copied without review.

Mitigation: Confirm the target repository, package index, branch, and credentials before using examples, and prefer TestPyPI before any public PyPI upload.

Risk: Module selection can omit needed context when triggers, token estimates, or loading paths are stale.

Mitigation: Validate module triggers, token costs, and loading paths before relying on the skill in a large or long-running agent workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-progressive-loading)
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code blocks and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [On-demand module-selection guidance for managing large skill context.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter says 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
