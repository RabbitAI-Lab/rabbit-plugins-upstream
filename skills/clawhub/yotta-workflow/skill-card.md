## Description:

A cross-session, cross-project workflow standard that guides AI agents to read project state on start, persist logs, tasks, and decisions in a project-root .workflow directory while working, and leave a handoff anchor on finish.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and teams use this skill to keep AI-assisted project work resumable across sessions and agents by maintaining Markdown state files, task lists, decision records, logs, and handoff anchors in a shared .workflow directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to create and retain project state under .workflow, so logs or decisions may accidentally contain secrets or sensitive project details.

Mitigation: Review what agents write to .workflow, avoid storing secrets there, and manage that directory with the same access controls and ignore rules used for sensitive project notes.

Risk: Unpinned npx installation examples can introduce supply-chain risk if a package version changes unexpectedly.

Mitigation: Prefer a pinned package version or a reviewed local checkout before installing or updating the skill.

Risk: Running the installer against shared or untrusted skill directories can write files into locations other users or tools may later consume.

Mitigation: Run installation only against trusted agent skill directories that the user controls and review generated files before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-workflow)
- [Path model](references/path-model.md)
- [FAQ](references/faq.md)
- [Complex walkthroughs](references/walkthroughs.md)
- [Exception playbook](references/exception-playbook.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-workflow)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands]

**Output Format:** [Markdown instructions with file paths, checklists, handoff templates, and optional installation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project-state workflow guidance and may direct an agent to create or update .workflow Markdown files in the project root.]

## Skill Version(s):

0.4.1 (source: frontmatter, package.json, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
