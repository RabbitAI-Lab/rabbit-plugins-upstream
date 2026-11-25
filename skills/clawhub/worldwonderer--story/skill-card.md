## Description:

网络小说工具箱主入口。根据用户需求自动路由到对应 skill，并可启动本地 Dashboard。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

面向网文作者，用自然语言或 /story、$story 入口匹配写作、拆文、审稿、导入和查资料等需求，并转交给相应工具。作者也可用它启动本地 Dashboard 管理写作项目文件。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags unauthenticated network access to workspace file operations, and notes that some components were only partially analyzed.

Mitigation: Keep Dashboard access local as directed by the skill, review the server behavior before enabling network access, and limit its workspace to files intended for Dashboard access.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/worldwonderer/skills/story)
- [Release notes](https://github.com/zenstory-ai/oh-story-claudecode/releases)
- [Changelog](https://github.com/zenstory-ai/oh-story-claudecode/blob/main/CHANGELOG.md)
- [URL listed in skill metadata (not verified as provenance)](https://github.com/zenstory-ai/oh-story-claudecode)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes requests to companion skills; Dashboard can read, edit, and delete supported workspace files.]

## Skill Version(s):

1.0.58 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
