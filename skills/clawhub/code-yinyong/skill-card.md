## Description:

从用户指定的 Java 方法向上追溯调用方，生成调用图直到 HTTP 接口或 RPC 方法等入口尽头；搜索范围限于当前 Git 仓库，不跨服务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[extraskittles](https://clawhub.ai/user/extraskittles)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to trace upstream callers of a Java method within the current Git repository and summarize the resulting entry points, caller graph, and supporting evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect proprietary Java source files in the current repository and include absolute file paths in its response.

Mitigation: Use it only in repositories where sharing source structure, paths, and summarized code relationships is acceptable.

Risk: Static caller tracing can be incomplete for dynamic dispatch, reflection, framework proxies, asynchronous events, or stale indexes.

Mitigation: Review the evidence paths and confidence labels, and verify uncertain branches with repository search before acting on the graph.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/extraskittles/skills/code-yinyong)
- [Publisher profile](https://clawhub.ai/user/extraskittles)
- [examples.md](examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Chinese Markdown with Mermaid diagrams, summary tables, evidence paths, and occasional shell commands for repository search.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only repository analysis; may include absolute source file paths and line numbers.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
