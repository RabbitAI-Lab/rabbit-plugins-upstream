## Description:

This skill helps an agent repair PowerPoint font issues by locally editing a user-provided PPTX file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, document automation teams, and agent users can use this skill when they need a Chinese-capable workflow for repairing PPTX font problems in local PowerPoint files. It is best suited to narrow PPTX repair tasks rather than broad document conversion or encrypted-file recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may modify local PPTX files during repair.

Mitigation: Run it only on files you are prepared to modify and keep a backup copy before use.

Risk: The security review notes broad references to API keys, external service calls, generic file processing, and command execution without clear boundaries.

Mitigation: Avoid providing API keys unless the destination service and data flow are understood, and require explicit approval before command execution or network/API use.

Risk: The release is marked suspicious by the authoritative security evidence.

Mitigation: Review the skill before installation and limit use to trusted PPTX inputs in a controlled agent environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/pptx-pdf-font-fix)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [SkillHub listing](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON-shaped result examples and command/configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe local file changes, execution status, repair metadata, and troubleshooting steps.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
