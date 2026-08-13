## Description:

AI科技资讯深度追踪与分析工作流，每日自动采集AI前沿动态和GitHub热门项目，生成3000-5000字技术深度文章并发布到公众号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zlszhonglongshen](https://clawhub.ai/user/zlszhonglongshen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical writers, and AI media operators use this skill to gather AI news, verify GitHub trends, synthesize technical insight, and draft a publishable long-form technical article.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated content may be saved under /root/articles or published to an external article API or Feishu archive without an explicit confirmation step.

Mitigation: Run the workflow in draft mode by default, require manual approval before external POST or document creation, and redirect saved files to a workspace-controlled path.

Risk: The workflow produces technical analysis from current search, GitHub, and paper signals, which can be incomplete or misleading if sources are stale or weak.

Mitigation: Review source summaries, verify cited projects and papers, and edit generated analysis before publication.

## Reference(s):

- [AI科技洞察罗盘 on ClawHub](https://clawhub.ai/zlszhonglongshen/skills/ai-tech-insight-compass)
- [Publisher profile: zlszhonglongshen](https://clawhub.ai/user/zlszhonglongshen)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown article with structured source summaries, code examples, technical tags, and optional publishing commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Targets 3000-5000 Chinese characters or words of technical article content, at least four code examples, at least five technical tags, and optional local save or external publishing steps.]

## Skill Version(s):

1.0.0 (source: workflow.json and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
