## Description:

A Chinese-oriented talking-head editing skill that turns recorded footage into a publishable cut by deleting or reordering spoken material without adding words, cleaning speech, applying speed, captions, optional B-roll, and delivery checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and editing agents use this skill to produce Chinese talking-head social video cuts with explicit checkpoints for content restructuring, speech cleanup, captions, generated insert selection, export review, and publish-readiness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify ChatCut timelines and write editing lessons to local memory.

Mitigation: Use it only in projects where timeline edits and memory updates are expected, and review each checkpoint before applying downstream edits.

Risk: Optional generated video may consume paid ChatCut or generation quota.

Mitigation: Submit generated clips only after the selected lines, model, duration, and cost have been confirmed.

Risk: Generated B-roll could mislead viewers if used as evidence for real events, data, or testimonials.

Mitigation: Use generated inserts only for metaphor, process, mood, or transitions, and keep testimony, screenshots, revenue claims, and real events on verified source material.

Risk: Published footage can expose personal data, client details, revenue amounts, or AI-generated media without disclosure.

Mitigation: Apply the documented masking checks before export and use platform AI-generation disclosure and service-provided labels when generated media is included.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-cut)
- [Publisher profile](https://clawhub.ai/user/iamzifei)
- [SKILL.md](artifact/SKILL.md)
- [ChatCut 实操](artifact/references/ChatCut实操.md)
- [内容层重组](artifact/references/内容层重组.md)
- [生成素材](artifact/references/生成素材.md)
- [规则卡](artifact/references/规则卡.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with checklists, editing decisions, tool-call instructions, and handoff notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce time-coded editing plans, caption/highlight candidates, generated-video prompts, export verification notes, and memory-update guidance.]

## Skill Version(s):

0.2.8 (source: server release metadata; artifact frontmatter reports 0.4.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
