## Description:

Volcengine Skills Finder helps agents list, select, check, and install exact Volcengine skills from the bundled marketplace catalog when a task needs missing Volcengine capability coverage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[volc-sdk-team](https://clawhub.ai/user/volc-sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to browse the Volcengine skills catalog, choose the minimum skills for a task, install exact missing skills, and verify installation status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install new agent skills globally using unpinned remote tooling or mutable sources.

Mitigation: Review before installing, prefer dry-run first, use project scope where possible, avoid arbitrary --source values, and install only exact skills from reviewed or pinned Volcengine sources.

Risk: A newly installed skill may not be available in the current agent thread.

Mitigation: Verify installation state and start a new thread with the original task context when the host cannot dynamically load the newly installed skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/volc-sdk-team/skills/volcengine-find-skills)
- [Bundled catalog](artifact/references/catalog.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-capable command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose dry-run commands and exact skill names before installation.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
