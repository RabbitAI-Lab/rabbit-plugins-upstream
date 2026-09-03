## Description:

Generalize and package a qualified or otherwise proven repeatable workflow into a portable Agent Skill with concise instructions, progressive disclosure, trigger-focused metadata, gotchas, and evals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use Skillify to turn a workflow with reuse evidence into a portable Agent Skill package. It helps separate reusable method from project-specific context, define trigger metadata, add realistic evals, and state deployment status truthfully.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated skills can influence future agent behavior if installed or published without review.

Mitigation: Review generated skill instructions, evals, and scope before deployment.

Risk: A one-off or unproven workflow could be mislabeled as a proven reusable skill.

Mitigation: Require Academy qualification, equivalent reuse evidence, or explicitly mark the package as experimental.

Risk: Project-specific details can leak into a portable skill and reduce correctness elsewhere.

Mitigation: Remove incidental names, paths, values, and runtime-specific assumptions unless they define the intended domain.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/raguets/skills/skillify)
- [Publisher profile](https://clawhub.ai/user/raguets)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown skill instructions with JSON eval configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a portable skill package structure, typically SKILL.md plus optional references and evals/evals.json.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact metadata.version is 0.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
