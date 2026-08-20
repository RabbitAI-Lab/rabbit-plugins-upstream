## Description:

Meta Evolver helps an agent assess a local skill ecosystem, plan capability improvements, record outcomes, and iteratively adjust its own evolution strategy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to inspect a local skills directory, generate a strategy for capability gaps, package related skills, and record or reflect on improvement attempts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can scan local skill folders and write strategy or pattern files.

Mitigation: Run it in a separate workspace or sandbox and review generated files before applying changes to a real skills directory.

Risk: Bulk frontmatter and finalize scripts can rewrite multiple installed skills or add learner files.

Mitigation: Back up the skills directory first and review diffs before using bulk repair, finalize, or package commands.

Risk: Self-improvement guidance may introduce incorrect or unwanted changes into other skills.

Mitigation: Treat generated plans as proposals and require human review before adopting code or workflow changes.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with command examples and generated local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify local strategy, pattern, frontmatter, learner, and package files when its scripts are run.]

## Skill Version(s):

1.0.14 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
