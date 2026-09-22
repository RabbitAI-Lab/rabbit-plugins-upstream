## Description:

Desktop Control lets OpenClaw agents operate a trusted Windows desktop with screenshots, window management, mouse and keyboard control, OCR, UI automation, and script orchestration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunsettide](https://clawhub.ai/user/sunsettide)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users can give an agent controlled access to their own trusted Windows desktop for local automation tasks such as screenshots, window control, text entry, OCR-based clicking, and multi-step scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants an agent full interactive control of mouse, keyboard, screenshots, windows, scripts, and macros on the host desktop.

Mitigation: Install only on a trusted Windows machine and use it only for authorized sessions where this level of control is acceptable.

Risk: Generated scripts and goal-driven automation may perform broad desktop actions and should be treated as potentially network-enabled despite local-only claims.

Mitigation: Prefer confirm or review modes before running generated scripts, and inspect proposed actions before execution.

Risk: Prompts, context, macros, logs, screenshots, or cached desktop data may expose sensitive information.

Mitigation: Avoid placing secrets in prompts, context, macros, or automated input, and inspect DesktopControl logs and cache directories if sensitive data may have been used.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sunsettide/skills/desktop-control)
- [Desktop Control homepage](https://github.com/sunsettide/desktop-control)
- [README](README.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON parameters; command responses may include JSON, text, base64 screenshots, or saved files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Targets Windows 10/11 with Python 3.9+ and local desktop session access.]

## Skill Version(s):

1.1.3 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
