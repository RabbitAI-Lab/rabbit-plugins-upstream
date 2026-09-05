## Description:

A Chinese middle-school physics tutoring skill that coaches students through experiment design, variable control, data analysis, error analysis, and lab-conclusion evaluation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students and learning-support agents use this skill to guide Chinese middle-school physics lab reasoning without simply giving complete experiment answers. It supports questions about apparatus, procedures, controlled variables, readings, data tables, error sources, and conclusion wording.

### Deployment Geography for Use:

Mainland China by default; deployment elsewhere requires localized emergency-help guidance, curriculum alignment, and minor-consent review.

## Known Risks and Mitigations:

Risk: Use outside Mainland China may rely on mismatched emergency-help channels, curriculum assumptions, or minor-consent defaults.

Mitigation: Localize emergency-help guidance, verify curriculum alignment, and review consent requirements before deployment in another region.

Risk: Student profile memory and cross-skill sharing can expose sensitive learning data if enabled without the intended consent controls.

Mitigation: Keep memory and sharing disabled unless consent is confirmed, and honor view, correct, delete, export, pause, and sharing-control requests.

Risk: Unclear experiment images or tables can lead to incorrect coaching if OCR or multimodal interpretation is unreliable.

Mitigation: Ask the student to transcribe table headers, row values, apparatus details, and the question when the image or data table is unclear.

Risk: Learning-frustration conversations can include safety signals that exceed the skill's tutoring role.

Mitigation: Stop tutoring flow when crisis signals appear, provide localized emergency or trusted-adult referral, and record only the referral fact if a safety record is needed.

## Reference(s):

- [物理实验方法深度手册](artifact/references/physics-experiment-methods.md)
- [物理数据分析方法手册](artifact/references/physics-data-analysis.md)
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-lab-coach)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown conversational tutoring guidance with occasional structured handoff or profile-control snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese K12 physics-lab coaching; OCR and memory-dependent behavior must degrade when platform support is unavailable.]

## Skill Version(s):

2.1.6 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
