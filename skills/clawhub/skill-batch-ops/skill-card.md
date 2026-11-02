## Description:

Coordinates inventory, batch updates, multi-platform publishing, version alignment, and verification across three or more agent skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to inventory and update multiple agent skills, align versions, publish them across supported platforms, and verify each result. It is intended for batch work on three or more skills rather than single-skill governance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch edits or publishing could introduce incorrect skill content or release unintended changes.

Mitigation: Review the proposed edits and every upload before publishing, and verify each item afterward.

Risk: Publishing credentials could be exposed or used beyond the intended batch.

Mitigation: Use narrowly scoped publishing credentials and isolated verification directories.

Risk: A malformed version field could cause installation or version-selection problems.

Mitigation: Correct and confirm the version field before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/haiyangchenbj/skills/skill-batch-ops)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance, commands, and skill-file edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes per-skill verification guidance.]

## Skill Version(s):

1.0.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
