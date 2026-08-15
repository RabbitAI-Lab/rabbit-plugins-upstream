## Description:

List, select, and install Volcengine skills from the volcengine-skills marketplace so an agent can fill missing Volcengine capability gaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[volc-sdk-team](https://clawhub.ai/user/volc-sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to browse the Volcengine skill catalog, choose the smallest set of missing skills for a task, install exact skills through the skills CLI, and verify installation status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change an agent's installed skills and defaults to global installation.

Mitigation: Use dry-run or project scope where possible, review the selected exact skill names before installation, and verify installed state after the command completes.

Risk: The skill can install from a non-default source when directed.

Mitigation: Use alternate sources only after reviewing and trusting the source, and prefer the catalog's default source for normal use.

Risk: A newly installed skill may not be available in the current agent thread.

Mitigation: Check installation status and start a new thread when the host cannot dynamically load the newly installed skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/volc-sdk-team/skills/volcengine-find-skills)
- [Publisher profile](https://clawhub.ai/user/volc-sdk-team)
- [Bundled Volcengine skills catalog](artifact/references/catalog.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce catalog listings, dry-run install commands, and installation status checks; installation defaults to global scope unless project scope is specified.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
