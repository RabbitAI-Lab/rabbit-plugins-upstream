## Description:

Use when analyzing, debugging, modifying, reviewing, testing, or designing code. Verify important assumptions, distinguish facts from inference and hypotheses, make the smallest safe change, and verify results whenever practical.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jrd77](https://clawhub.ai/user/jrd77)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to perform rigorous code analysis, debugging, review, modification, testing, and design work with explicit evidence, minimal changes, and practical verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may inspect repository files or run targeted checks while applying the skill.

Mitigation: Use the skill in workspaces where repository inspection and verification commands are appropriate, and review commands before execution in sensitive environments.

Risk: Code-analysis conclusions can be misleading if the agent overstates what static inspection, tests, or documentation prove.

Mitigation: Require reports to distinguish facts, inferences, hypotheses, verification performed, and remaining uncertainty.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jrd77/skills/rigorous-code-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, plain text, code snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state evidence, verification boundaries, and remaining uncertainty when relevant.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
