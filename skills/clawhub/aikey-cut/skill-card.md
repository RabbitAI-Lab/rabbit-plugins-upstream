## Description:

AI KEY·口播剪辑 helps agents turn talking-head footage into a publishable cut by restructuring spoken content without adding words, cleaning speech, applying speed and captions, and preparing optional B-roll or generated insert prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and agent operators use this skill to guide Chinese talking-head video editing from filmed material to a publishable timeline, including content deletion/reordering, speech cleanup, captions, optional B-roll, and export checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can edit a ChatCut timeline and write editing feedback memory.

Mitigation: Review account defaults and proposed timeline changes before applying them, and keep memory writes scoped to confirmed editing feedback.

Risk: Generated video or export steps may consume paid credits or produce unwanted deliverables.

Mitigation: Approve generation or export only after the proposed cost, clip count, model, duration, and output target match the project.

Risk: Generated B-roll could misrepresent testimony, real events, data, or screenshots.

Mitigation: Use generated footage only for metaphor, process, mood, or transition shots; do not use it as evidence, and keep AI-generation disclosure enabled for publication.

Risk: Video material may expose private customer, account, revenue, or screenshot details.

Mitigation: Mask sensitive visual information before publishing and verify the final exported file frame-by-frame for captions, B-roll, and masking.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/aikey-cut)
- [ChatCut实操.md](artifact/references/ChatCut实操.md)
- [内容层重组.md](artifact/references/内容层重组.md)
- [生成素材.md](artifact/references/生成素材.md)
- [规则卡.md](artifact/references/规则卡.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with editing checklists, tool-use steps, configuration reminders, and prompt drafts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose ChatCut timeline edits, export checks, local transcription steps, and generated B-roll prompts; paid generation or export actions require user confirmation.]

## Skill Version(s):

0.4.4 (source: server release metadata; artifact frontmatter says 0.4.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
