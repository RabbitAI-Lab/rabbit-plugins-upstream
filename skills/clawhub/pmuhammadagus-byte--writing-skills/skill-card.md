## Description:

Writing Skills helps agents create, edit, and verify process-documentation skills using a test-driven RED-GREEN-REFACTOR workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to create, revise, and verify reusable agent skills. It focuses on pressure scenarios, baseline failures, compliance checks, and validation before deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill encourages agents to inspect local skill directories during discovery workflows.

Mitigation: Use it with skill directories you trust and review local files before following generated guidance or commands.

Risk: The artifact contains duplicate frontmatter and version signals, which can affect parser compatibility.

Mitigation: Validate the skill with the intended runtime parser or artifact/scripts/validate_skill.py, and reconcile metadata before deployment if strict parsing is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/writing-skills)
- [Agent Skills specification](https://agentskills.io/specification)
- [Skill authoring best practices](artifact/anthropic-best-practices.md)
- [Testing Skills With Subagents](artifact/testing-skills-with-subagents.md)
- [CLAUDE.md skill testing example](artifact/examples/CLAUDE_MD_TESTING.md)
- [Graphviz conventions](artifact/graphviz-conventions.dot)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown prose with checklists, tables, code blocks, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local skill files, validation scripts, and Graphviz rendering commands when relevant.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
