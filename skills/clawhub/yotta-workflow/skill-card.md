## Description:

Helps agents resume project work across sessions by reading project state, updating tasks and decisions, and leaving a handoff anchor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to preserve project progress, tasks, decisions, and handoffs between sessions or agents. It keeps state in the project's .workflow directory rather than relying on conversation memory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent project records or handoff anchors may disclose private project details or an absolute local path when shared.

Mitigation: Review .workflow contents and handoff anchors before sharing them externally.

Risk: Installing the skill across multiple agents may broaden access to project records beyond the intended agent.

Mitigation: Use targeted --agent or --dir installation unless multi-agent installation is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-workflow)
- [Project homepage (listed in ClawHub metadata)](https://github.com/YottaMeta/yotta-workflow)
- [Workflow FAQ](references/faq.md)
- [Project path model](references/path-model.md)
- [Exception recovery guide](references/exception-playbook.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown project-state files and text handoff anchors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State is written under the selected project's .workflow directory.]

## Skill Version(s):

0.4.3 (source: ClawHub release metadata, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
