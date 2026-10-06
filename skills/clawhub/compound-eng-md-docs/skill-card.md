## Description:

Helps maintain project documentation and agent context files by checking claims against the repository before making changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to create or refresh README.md, AGENTS.md, and related project documentation using verified repository details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes to AGENTS.md or CLAUDE.md can alter future agent behavior.

Mitigation: Review planned edits carefully; use dry-run or preserve mode for a preview or narrower changes.

Risk: Incorrect documentation can mislead contributors.

Mitigation: Check proposed commands, paths, and claims against the repository before accepting updates.

## Reference(s):

- [Documentation workflows](artifact/references/documentation-workflows.md)
- [Context content and writing](artifact/references/context-content-and-writing.md)
- [Monorepo handling](artifact/references/monorepo.md)

## Skill Output:

**Output Type(s):** [Markdown files, Guidance]

**Output Format:** [Markdown documentation and a text change summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run previews and backs up existing files before overwriting.]

## Skill Version(s):

5.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
