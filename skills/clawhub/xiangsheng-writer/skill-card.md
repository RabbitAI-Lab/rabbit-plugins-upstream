## Description:

编写有趣的中国相声。用户给定一个主题（或说"写段相声/编个段子/相声创作/把这段话写成相声"）时，按 定调→梁子→包袱库→结构→写稿→自审 流程引导完成，产出可上台的完整台词本。也用于修改、润色、诊断已有相声稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

BSD-3-Clause

## Use Case:

External users and content creators use this skill to draft, revise, and diagnose Chinese xiangsheng scripts from a topic, following a staged workflow for tone, structure, punchline planning, dialogue, self-review, and delivery notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad comedy-writing prompts may trigger the xiangsheng workflow when the user intended a different format.

Mitigation: Confirm the intended form or continue only when the request clearly asks for xiangsheng, crosstalk, a skit-like dialogue, or revision of an existing xiangsheng draft.

Risk: Generated scripts may contain unsuitable satire, weak originality, or content that needs audience-specific review.

Mitigation: Review outputs for style, originality, appropriateness, and the skill's stated boundaries before public use.

Risk: Completed scripts may be saved locally under `xiangsheng/`.

Mitigation: Review saved files and paths before sharing, publishing, or retaining generated drafts.

## Reference(s):

- [xiangsheng-writer ClawHub page](https://clawhub.ai/skills/xiangsheng-writer)
- [相声技法手册](references/techniques.md)
- [经典段子研读笔记](references/classics.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown script text with dialogue lines, pacing marks, performance notes, alternative endings, and structure notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save completed scripts locally under xiangsheng/<topic>-<date>.md when used in an agent environment.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
