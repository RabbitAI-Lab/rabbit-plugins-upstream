## Description:

yotta-anti-shallow is a general-purpose agent ruleset that prompts AI assistants to analyze complex tasks before acting, declare uncertainty, and self-check results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineers, writers, analysts, and other agent users apply this skill when they want more rigorous handling of complex work such as development, troubleshooting, architecture, documentation, data analysis, and open-ended Q&A. The skill is intended to improve response discipline by requiring analysis, uncertainty disclosure, and completion checks where the task warrants them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The ruleset can broadly affect complex agent tasks by changing response flow, adding analysis requirements, and requiring self-checks.

Mitigation: Install it only for agents where this quality posture is desired, and verify behavior on representative tasks after installation.

Risk: Installer helpers can copy the skill into user-level, custom, or multiple agent skill directories.

Mitigation: Prefer a pinned npm version or manual installation for reproducibility, inspect the target directory before using --dir, and avoid --global unless multi-agent installation is intentional.

Risk: The skill can add process overhead or confirmation steps for L3+ tasks.

Mitigation: Use the documented close or explicit-instruction channels for workflows where the user wants a direct result, while keeping the hard floor against guessing or false completion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-anti-shallow)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-anti-shallow)
- [agentskills.io standard](https://agentskills.io/)
- [README.md](README.md)
- [README.zh-CN.md](README.zh-CN.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text responses with analysis, uncertainty, and self-check sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require user confirmation for L3+ tasks and includes confidence labels for speculative claims.]

## Skill Version(s):

1.3.5 (source: server release evidence; artifact files report 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
