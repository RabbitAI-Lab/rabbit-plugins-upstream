## Description:

A cross-session workflow that guides AI agents to read and maintain project state under `.workflow` and leave a handoff anchor at session end.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

AI agents and developers use this workflow when starting, resuming, or finishing multi-step project work. It keeps project progress, tasks, decisions, and handoff notes together so another session or agent can continue from the project state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project notes and handoff anchors may contain project details and absolute paths.

Mitigation: Review `.workflow` files and handoff text before sharing them.

Risk: Project notes remain after uninstalling the skill.

Mitigation: Remove the project's `.workflow` directory separately when you want to delete its saved state.

## Reference(s):

- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-workflow)
- [Project repository](https://github.com/YottaMeta/yotta-workflow)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-workflow)
- [Path model](references/path-model.md)
- [FAQ](references/faq.md)
- [Walkthroughs](references/walkthroughs.md)
- [Exception playbook](references/exception-playbook.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Text]

**Output Format:** [Project state Markdown files and a self-contained handoff message]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped state stored under `.workflow` at the confirmed project root.]

## Skill Version(s):

0.4.4 (source: frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
