## Description:

Provides screen understanding and control for local UI and browser tasks, and helps create and maintain automation workflows through natural language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaozs-com](https://clawhub.ai/user/xiaozs-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent users use this skill to complete bounded screen, browser, and workflow automation tasks on local Windows or macOS systems. It is intended for user-directed automation where the target window, success criteria, permissions, and verification steps are clear.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control local windows, browser sessions, clipboard, and reusable automation workflows.

Mitigation: Use it only for clearly bounded tasks, confirm the target window and success criteria, and review workflow install or remove actions before allowing them.

Risk: Screenshots, credentials, or private page content may be exposed if a task is authorized too broadly.

Mitigation: Avoid sending screenshots or credentials unless the Provider, scope, and purpose are clear, and keep raw credentials out of prompts, workflow files, logs, and final outputs.

Risk: Automation may report command success even when the visible business result has not been achieved.

Mitigation: Require observation after actions and verify visible results before treating the task or workflow run as complete.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xiaozs-com/skills/screen-automation-engineer)
- [Screen Automation Helper Homepage](https://www.xiaozs.com/sah/)
- [Agent Bridge and Vision Model Standard](references/agent-bridge.md)
- [Browser Enhancement Testing Standard](references/browser-enhancement-testing.md)
- [Automation Workflow Development Standard](references/workflow-standard.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, workflow definitions, code snippets, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should stay within the user's authorized task scope and avoid exposing credentials, screenshots, or private page content unless the provider, scope, and purpose are clear.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
