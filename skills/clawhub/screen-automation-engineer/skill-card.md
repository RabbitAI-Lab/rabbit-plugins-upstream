## Description:

Provides screen understanding and control through the local Screen Automation Helper, and helps create and maintain automation workflows through natural language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaozs-com](https://clawhub.ai/user/xiaozs-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect visible desktop state, execute supervised screen actions, and turn repeatable UI tasks into maintainable workflows. It is intended for Windows and macOS environments where the local Screen Automation Helper is installed and authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A local helper executable could be selected from an unintended environment-variable or PATH location.

Mitigation: Verify the installed Screen Automation Helper path before use and avoid overrides unless they point to a known trusted binary.

Risk: Screen automation can affect visible desktop applications and may expose sensitive windows or data.

Mitigation: Supervise first runs, confirm the target window and allowed actions, and keep passwords, codes, keys, payment information, and unrelated private content out of scope.

Risk: Screenshot-based visual understanding may send screen content to a configured provider.

Mitigation: Confirm the provider, region, purpose, and selected screen area before allowing screenshot sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiaozs-com/skills/screen-automation-engineer)
- [Screen Automation Helper homepage](https://www.xiaozs.com/sah/)
- [Agent bridge and visual model standard](artifact/references/agent-bridge.md)
- [Workflow development standard](artifact/references/workflow-standard.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and workflow artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include supervised screen-action steps, helper CLI commands, workflow definitions, validation steps, and status summaries.]

## Skill Version(s):

1.1.29 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
