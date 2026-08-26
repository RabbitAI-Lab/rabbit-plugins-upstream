## Description:

让AI像人一样分层看图，不再扫一眼就下结论。4层视觉理解法：整体扫视→识别精度敏感区→专门细看关键细节→如实输出。解决AI看图时漏读数字、错认状态、忽视小字等常见问题。当用户要求分析图片、识别图中内容、读取图中文字/数字、对比图片细节时触发。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lilei0311](https://clawhub.ai/user/lilei0311)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to apply a four-layer visual inspection process when reading images, screenshots, UI states, labels, text, numbers, or detailed differences. It is intended to reduce missed small text, wrong numeric reads, and premature conclusions during image analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broad trigger may activate for casual image descriptions where detailed inspection is unnecessary.

Mitigation: Use the full four-layer process for precision-sensitive image tasks and allow lighter review for decorative or low-stakes images.

Risk: Small text, dense labels, and ambiguous digits can still be uncertain even after closer inspection.

Mitigation: Have the agent explicitly state uncertainty for unclear regions and recheck precision-sensitive areas before finalizing an answer.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lilei0311/skills/pixel-gaze)
- [Agent frontend self-review case](artifact/references/case-agent-self-review.md)
- [Product label reading case](artifact/references/case-product-label.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, analysis]

**Output Format:** [Markdown or plain text guidance describing structured visual inspection steps and findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-only workflow; no external API, OCR tool, credentials, persistence, or file access is introduced by the skill.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
