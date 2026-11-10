## Description:

基于文件系统初始化和继续短剧或漫剧项目，提供 creator-first 五文档路由、本地 Dashboard、制作形态与 Look Development 决策。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Short-drama creators and production teams use this skill to initialize or resume file-based drama projects, route work to the appropriate creative stage, inspect project progress, and export current materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has detected file, network, and shell capabilities, and host permission enforcement is unclear.

Mitigation: Review the agent host’s permissions and limit file, network, and command access to what the project task requires.

Risk: Inspection was partial, with parser limits and unresolved references leaving some components outside the available coverage.

Mitigation: Review unresolved references and assess companion skills separately before enabling them.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/worldwonderer/skills/short-drama)
- [Creator-first workflow](references/creator-workflow.md)
- [Runtime preflight and safe project writes](references/runtime-preflight.md)

## Skill Output:

**Output Type(s):** [Markdown, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown guidance, shell commands, and project JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Files and guidance vary with the requested project stage and available materials.]

## Skill Version(s):

1.0.37 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
