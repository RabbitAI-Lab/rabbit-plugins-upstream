## Description:

A cross-session and cross-agent workflow standard that keeps project state in a root-level .workflow directory, requires agents to read state before work, persist progress while working, and leave a handoff anchor when finishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to keep durable project state across AI sessions and across different agent tools. It is intended for project work that needs handoff continuity, task tracking, decision records, and resumable context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow automatically persists project state in .workflow, which can expose confidential project details if users or agents write sensitive information there.

Mitigation: Review .workflow before committing or sharing it, and do not store secrets, credentials, or confidential details in the state files.

Risk: Installer behavior may overwrite or conflict with existing yotta-workflow directories or unrelated data in a chosen target directory.

Mitigation: Prefer pinned npm installs, inspect the target directory first, and avoid install.sh on directories that already contain a yotta-workflow repository or unrelated data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-workflow)
- [npm package: @yottameta/yotta-workflow](https://www.npmjs.com/package/@yottameta/yotta-workflow)
- [Agent Skills standard](https://agentskills.io/)
- [FAQ](references/faq.md)
- [Path model](references/path-model.md)
- [Walkthroughs](references/walkthroughs.md)
- [Exception playbook](references/exception-playbook.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and fixed handoff templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project-state files under .workflow and human-readable handoff anchors when the workflow is followed.]

## Skill Version(s):

0.4.0 (source: frontmatter, package.json, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
