## Description:

将古诗词、古文名篇、现代散文或小说改编为歌曲，输出带原文化用出处的歌词全文、曲风/编曲方案和可用于 AI 音乐工具的提示。

This skill is ready for commercial/non-commercial use.

## Publisher:

[fslong520](https://clawhub.ai/user/fslong520)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, educators, and agents use this skill to adapt poems, classical prose, modern prose, or fiction into original lyrics with a narrative outline, arrangement guidance, and source mapping for teaching or music-generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic Chinese songwriting requests may invoke the skill when ordinary songwriting was intended.

Mitigation: Invoke the skill by name or with a specific poem/prose adaptation request, and review the narrative outline before generating full lyrics.

Risk: Literary or historical background errors could mislead users, especially in teaching contexts.

Mitigation: Use reliable source material for the original text, author background, and reception history; mark uncertain details as uncertain rather than presenting them as fact.

Risk: Generated lyrics could overuse source text or accidentally copy existing lyrics.

Mitigation: Limit direct quotation from source poems, avoid copying existing song lyrics, and include a source mapping table for adapted lines.

## Reference(s):

- [Skill Source](artifact/SKILL.md)
- [Analysis and Source Research Module](artifact/modules/01-analyze.md)
- [Lyrics Method Module](artifact/modules/02-lyrics.md)
- [Arrangement Guidance Module](artifact/modules/03-music.md)
- [Output Format Module](artifact/modules/04-output.md)
- [Textual Score Module](artifact/modules/05-score.md)
- [Example Adaptation Workflow](artifact/examples/jiangjinjiu.md)
- [ClawHub Skill Page](https://clawhub.ai/fslong520/skills/windchant)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown containing analysis, narrative outline, lyrics, arrangement guidance, AI music prompt text, and source mapping tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Text-only outputs; no executable code or privileged tool actions.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
