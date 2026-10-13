## Description:

Helps agents inspect and control local windows and create maintainable screen automation workflows using natural language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaozs-com](https://clawhub.ai/user/xiaozs-com)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers use this skill to complete user-directed tasks in local windows and browsers, or turn repeated tasks into verifiable automation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Screen actions may affect the wrong window or make irreversible changes.

Mitigation: Verify the target window and permissions first, then confirm irreversible actions and check the resulting state.

Risk: Screenshots sent to an external visual-model provider may reveal private information.

Mitigation: Explain the provider, screen area and purpose, and obtain explicit confirmation before sending screenshots.

Risk: Installing or removing workflows can change future automation behavior.

Mitigation: Review the workflow and its permissions before installation or removal.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/xiaozs-com/skills/screen-automation-engineer)
- [Screen Automation Assistant](https://www.xiaozs.com/sah/)
- [Workflow development standard](artifact/references/workflow-standard.md)
- [Agent and visual-model integration standard](artifact/references/agent-bridge.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Text and Markdown, including workflow steps and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workflow results and saved files depend on the installed desktop assistant and granted capabilities.]

## Skill Version(s):

1.2.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
