## Description:

调用链路追踪 + 代码标注 + 信任边界标注。生成可视化的代码理解页面，让模块结构和数据流一目了然。

This skill is ready for commercial/non-commercial use.

## Publisher:

[paudyyin](https://clawhub.ai/user/paudyyin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and code reviewers use this skill to turn module explanations into visual HTML walkthroughs with call paths, source annotations, and trust-boundary notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated walkthrough pages may expose source snippets, file paths, or security-boundary notes from the reviewed project.

Mitigation: Review generated HTML before sharing and redact sensitive implementation details.

Risk: Trust-boundary annotations can be incomplete or misleading if the underlying code analysis misses validation, authorization, or external dependency behavior.

Mitigation: Have a project maintainer verify the generated call path and boundary labels before relying on them for review decisions.

## Reference(s):

- [Code Walkthrough ClawHub skill page](https://clawhub.ai/paudyyin/skills/code-walkthrough)

## Skill Output:

**Output Type(s):** [Analysis, Code, Guidance]

**Output Format:** [Self-contained HTML with annotated code walkthrough content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source snippets, file paths, call-flow diagrams, and trust-boundary annotations.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
