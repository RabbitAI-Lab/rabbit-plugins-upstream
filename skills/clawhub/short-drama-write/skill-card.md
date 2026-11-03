## Description:

编写或修订可拍摄的中文短剧、漫剧单集 Markdown 剧本，也负责保留作者原文并规范化现成剧本。用户提出“写/改一集短剧”“把大纲写成剧本”“优化场景/对白”“去模板感”“去 AI 味润色”“续写下一集”或提供剧本要求进入后续制作时使用；不负责资产、分镜、媒体提示词或终审。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

中文短剧编剧和创作者可用此技能，将单集构想、大纲或现有剧本写成或修订为可表演、可拍摄的剧本。它帮助整理场景、动作、对白与必要的制作标签，并保留作者原文进行定点修改。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Screenplay edits can affect user-authored material.

Mitigation: Limit file access to the screenplay and relevant project inputs, and keep a backup before revisions.

Risk: Optional timing checks create local index files that may remain after use.

Mitigation: Use the documented temporary paths and remove generated index files when they are no longer needed.

Risk: Host filesystem permissions were not verified.

Mitigation: Restrict access to the screenplay and relevant project inputs while using the skill.

## Reference(s):

- [短剧写作发布页](https://clawhub.ai/worldwonderer/skills/short-drama-write)
- [发布者主页](https://clawhub.ai/user/worldwonderer)
- [剧本格式](references/screenplay-format.md)
- [剧作手艺](references/script-craft.md)
- [对白手艺](references/dialogue-craft.md)
- [阶段契约](references/stage-contract.md)

## Skill Output:

**Output Type(s):** [Markdown, Screenplay text, Writing guidance]

**Output Format:** [Chinese Markdown screenplay with scene headings, performable action and dialogue, and optional production tags]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces or revises the requested episode script at 剧集/<EP>/剧本.md; targeted revisions preserve unrelated author text.]

## Skill Version(s):

1.0.13 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
