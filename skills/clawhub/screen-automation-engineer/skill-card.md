## Description:

Helps agents inspect and operate local Windows and macOS application windows, then create and maintain supervised screen automation workflows from natural-language goals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaozs-com](https://clawhub.ai/user/xiaozs-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and end users use this skill when they need an agent to confirm a target window, inspect visible UI state, and either complete a supervised screen task or turn a repeated task into a maintainable workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Desktop automation may operate the wrong window or take unintended UI actions if the target or page state is ambiguous.

Mitigation: Confirm the target window, observe state before each change, validate after each action, and stop when the target or result cannot be verified.

Risk: Automation can affect accounts, data, payments, publishing, deletion, or other irreversible decisions.

Mitigation: Keep logins, authorization, payments, publishing, deletion, and other irreversible decisions under direct user control, with the first real run supervised.

Risk: Generated workflows may be invalid or drift when the target application changes.

Mitigation: Run local status, capability, health, inspect, and validate checks, then perform supervised acceptance before repeated or batch execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiaozs-com/skills/screen-automation-engineer)
- [Publisher profile](https://clawhub.ai/user/xiaozs-com)
- [Server-resolved GitHub source](https://github.com/xiaozs-com/screen-automation-engineer)
- [Product homepage](https://www.xiaozs.com/sah/)
- [Workflow standard](artifact/references/workflow-standard.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, workflow files, optional Python extensions, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include workflow.md packages, optional workflow.py code, validation commands, and result summaries.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
