## Description:

Formats, reviews, and proposes fixes for InterSystems IRIS/Cache ObjectScript code using rules for naming, methods, locks, transactions, traps, layout, blank lines, and comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yaoxin521123](https://clawhub.ai/user/yaoxin521123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers working with InterSystems IRIS/Cache ObjectScript use this skill to check style compliance, identify code quality issues, and generate a complete corrected version of supplied code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can produce full corrected code that may change behavior if applied without domain review.

Mitigation: Review the generated ObjectScript changes before merging or deploying them.

Risk: The artifact references an optional npx install command, which can execute package-managed code during installation.

Mitigation: Install only through a trusted ClawHub/OpenClaw path or a pinned and verified CLI version.

Risk: The style guide is strict and Chinese-language, so teams with different local IRIS/ObjectScript conventions may receive unsuitable formatting recommendations.

Mitigation: Confirm the project's coding standard before accepting the proposed formatting and naming changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yaoxin521123/skills/iris-code-formatter)
- [IRIS code formatter usage guide](IRIS 代码格式化 Skill 使用说明.md)
- [IRIS code standard reference index](references/README.md)
- [Variable naming rules](references/代码规范 - 变量.md)
- [Method naming rules](references/代码规范 - 方法.md)
- [Formatting rules](references/代码规范 - 格式.md)
- [Locking rules](references/代码规范 - 锁.md)
- [Transaction rules](references/代码规范 - 事务.md)
- [Trap handling rules](references/代码规范 - 陷阱.md)
- [Blank line rules](references/代码规范 - 空行.md)
- [Comment rules](references/代码规范 - 注释.md)

## Skill Output:

**Output Type(s):** [markdown, code, guidance]

**Output Format:** [Markdown review report with ObjectScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a full corrected version of the user-provided code for human review before applying changes.]

## Skill Version(s):

3.1.0 (source: server release metadata; artifact frontmatter and changelog: 3.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
