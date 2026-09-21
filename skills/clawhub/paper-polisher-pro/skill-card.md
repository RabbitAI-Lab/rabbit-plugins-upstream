## Description:

Paper Polisher Pro helps authors run local AI-writing self-checks, academic polishing checks, terminology review, translation-smell checks, AIGC label checks, paragraph attribution, journal prechecks, and quality reports for Chinese and English academic writing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External users, authors, editors, and writing-support agents use this skill to review drafts locally for AI-writing risk signals, terminology consistency, disclosure-label compliance, paragraph-level attribution, translation artifacts, and academic writing quality. It is positioned for author self-review and disclosure compliance, not for misrepresenting AI-generated work as human-written.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes de-AI/retest, attack-generation, and broad-trigger components that can help optimize text against AI detectors.

Mitigation: Use the skill only for author self-review, writing quality, and disclosure compliance; remove or disable those components where policy does not allow detector-optimization workflows.

Risk: The optional freshness cron and apply-style calibration scripts can mutate local detector resources.

Mitigation: Run calibration or freshness maintenance only in a controlled environment after reviewing the intended corpus, outputs, and policy fit.

Risk: Detector outputs have stated boundaries, including no verdict for texts under 100 characters, advisory-only English rules, medical-register overscoring in rules-only mode, and poor document-level mixed human-AI averaging.

Mitigation: Treat results as decision support, use paragraph-level reports where mixed authorship is suspected, and require human review before making academic-integrity judgments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Article Review Workflow](references/article-review-workflow.md)
- [Fusion Configuration](references/fusion_config.json)
- [Model Fingerprints](references/model_fingerprints.json)
- [English AI Pattern Library](references/ai_patterns_en.json)
- [Chinese AI Pattern Library](references/ai_patterns_zh.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, HTML, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands and local text, JSON, or HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on user-provided documents; optional supervised scoring requires separate local ONNX model files.]

## Skill Version(s):

3.6.0 (source: frontmatter, skill.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
