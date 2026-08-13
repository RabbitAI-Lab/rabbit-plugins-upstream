## Description:

webclaw3 lets an agent automate and scrape pages through the user's own logged-in Chrome session, then turn successful browser workflows into repeatable local skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use webclaw3 to perform browser automation, authenticated web data extraction, page interaction, and recurring workflow generation from their own Chrome session. It is especially suited to tasks where login state, dynamic pages, or site-specific interaction are required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill controls the user's logged-in Chrome session and can interact with authenticated websites.

Mitigation: Install and run it only when that level of browser access is acceptable; supervise sensitive sessions and stop the local services when not needed.

Risk: The security review flags high-power local components and local file-handling behavior.

Mitigation: Review and scan the skill before deployment, keep local services running only while needed, and protect the ~/.webclaw3 access key and configuration files.

Risk: CDP fallback increases browser-control exposure and may trigger Chrome authorization prompts.

Mitigation: Use the extension relay as the normal path and enable CDP fallback only when the extension channel is unavailable and the user accepts the added risk.

Risk: The evidence guidance warns against the qoderclicn curl-to-bash setup path unless independently trusted.

Mitigation: Avoid that installation path unless it has been independently verified for the target environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fatmind/skills/webclaw3-browser-automation)
- [webclaw3 website](https://webclaw3.com)
- [GitHub repository link declared by skill](https://github.com/fatmind/webclaw3)
- [Setup guide](references/setup.md)
- [Distillation workflow](references/brief.md)
- [Repair workflow](references/repair.md)
- [CDP fallback guide](references/cdp-fallback.md)
- [Using webclaw3 in Claude Code](docs/claude-code.md)
- [Using webclaw3 in workbuddy](docs/workbuddy.md)
- [Using webclaw3 in qoderwork](docs/qoderwork.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, configuration steps, generated local skill files, and structured browser-task results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce reusable local automation skills and setup or repair instructions; browser actions run against the user's local Chrome session.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; package.json version 0.6.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
